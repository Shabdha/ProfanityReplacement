from tkinter import*
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from pygame import mixer


import thinkdsp
import thinkplot
import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
from scipy.fftpack import fft
from scipy.io import wavfile
from pydub import AudioSegment


#our files imports
import Preprocessing as pr
import transcribe_enhanced_model as tr
import NLP as nlp


root = Tk()
mixer.init()

# import file


def browse_file():
    global filename
    filename = filedialog.askopenfilename()
    print(filename)

    # Audio preprocessing
    pr.noise_reductionM1(filename)
    # conversion from other formats to wav

def new_window1(words):
    global win1
    try:
        if win1.state() == "normal": win1.focus()
    except:
        win1 = Toplevel()
        win1.geometry("300x300+500+200")
        win1["bg"] = "white"
        lb = Label(win1, text=words)
        lb.pack()

def analyse():
    path=filename
    tr.transcribe_file_with_enhanced_model(path, "en-US")
    words=nlp.profanity()
    new_window1(words)
    '''try:
        if Tamil:
            tr.transcribe_file_with_enhanced_model(path,"ta-LK")
        elif English:
            tr.transcribe_file_with_enhanced_model(path,"en-US")
        elif Sinhala:
            tr.transcribe_file_with_enhanced_model(path,"si-LK")
        else:
            messagebox.showinfo("Language Error", "Select a language to Analyse")
    except:
        messagebox.showinfo("Language Error", "Select a language to Analyse")
'''
def play_music():

  try:
    paused

  except NameError:
    try:
        mixer.music.load(filename)
        mixer.music.play()

    except:
        messagebox.showerror("error")

  else:
    mixer.music.unpause()



def stop_music():
    mixer.music.stop()


def set_vol(val):
    volume = int(val)/100
    mixer.music.set_volume(volume)


def pause_music():
    global paused
    paused = TRUE
    mixer.music.pause()


def rewind_music():
    play_music()

#def mute_music():
 #   volumeBtn.configure(image=mutePhoto)


def doaction():
    print("action")


root.title("Shabdha- Automatic Audio Replacement Tool")
root.geometry("750x560")
root.iconbitmap(r'melody.ico')

# ****main menu *****************************************************

menu = Menu(root)
root.config(menu=menu)

fileMenu = Menu(menu)
menu.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="New Project", command=doaction)
fileMenu.add_command(label="Open", command=doaction)
fileMenu.add_command(label="Save", command=doaction)
fileMenu.add_command(label="Save as", command=doaction)
fileMenu.add_command(label="Import", command=doaction)
fileMenu.add_command(label="Export", command=doaction)
fileMenu.add_command(label="Setting", command=doaction)
fileMenu.add_command(label="Exit", command=doaction)

editMenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Undo", command=doaction)
editMenu.add_command(label="Redo", command=doaction)

viewMenu = Menu(menu)
menu.add_cascade(label="Veiw", menu=viewMenu)
viewMenu.add_command(label="Maximize", command=doaction)
viewMenu.add_command(label="Minimize", command=doaction)

helpMenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpMenu)
helpMenu.add_command(label="Help?", command=doaction)

# ************* buttons***********************************************


button1 = Button(text='Add', fg='white', bg='green', font=10, command=browse_file).place(x=55, y=50)
button2 = Button(text='Remove', fg='white', bg='orange', font=10).place(x=120, y=50)
button3 = Button(text='Analyse', fg='white', bg='green', font=10, command=analyse).place(x=650, y=500)


# *********** radio ********************************************************
theLabel = Label(root, text="Language").place(x=100, y=300)

r =IntVar()
Tamil = Radiobutton(root, text='Tamil', variable=r, value=1).place(x=100, y=320)
Sinhala = Radiobutton(root, text='Sinhala', variable=r, value=2).place(x=100, y=340)
English = Radiobutton(root, text='English', variable=r, value=3).place(x=100, y=360)

# *******************check boxes ***********************************************

theLabel2 = Label(root, text="Objectionable Word Type").place(x=400, y=300)

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()

Checkbutton(root, text="Vain reference to deity", variable=var1).place(x=400, y=320)
Checkbutton(root, text="Ethnic and racial slurs", variable=var2).place(x=400, y=340)
Checkbutton(root, text="cursing", variable=var3).place(x=400, y=360)
Checkbutton(root, text="Strong profanity", variable=var4).place(x=400, y=380)
Checkbutton(root, text="User Define", variable=var5).place(x=400, y=400)

# ******************* text box *************************************

# theLabel3 = Label(root, text="User define word").place(x=700, y=300)


# ************ music player ******************
playPhoto = PhotoImage(file='play.png')
playBtn = Button(root, image=playPhoto, command=play_music).place(x=200, y=200)
# playBtn.pack()

stopPhoto = PhotoImage(file='stop.png')
stopBtn = Button(root, image=stopPhoto, command=stop_music).place(x=280, y=200)
# stopBtn.pack()

pausePhoto = PhotoImage(file='pause.png')
pauseBtn = Button(root, image=pausePhoto, command=pause_music).place(x=240, y=200)

rewindPhoto = PhotoImage(file='rewind.png')
rewindBtn = Button(root, image=rewindPhoto, command=rewind_music).place(x=320, y=200)

volumePhoto = PhotoImage(file='volume.png')
label = Label(root, image=volumePhoto).place(x=386, y=200)

scale = Scale(root, from_=0, to=100, orient=HORIZONTAL, command=set_vol)
scale.set(70)
mixer.music.set_volume(0.7)
scale.place(x=420, y=200)

root.mainloop()







filename="blood_audio.wav"