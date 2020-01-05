from tkinter import*
from tkinter import ttk
from tkinter import filedialog


root = Tk()

def doaction():
    print("action")

def mfileopen():
    file1 = filedialog.askopenfile()
    label4 = Label(text=file1).place(x=60, y=100)
    file2 = file1.name
    f = open(file2)
    label5 = Label(text=f.read()).place(x=60, y=150)


root.title("Shabdha- Automatic Audio Replacement Tool")
root.geometry("750x550")


# ****main menu *****************************************************

menu = Menu(root)
root.config(menu=menu)

fileMenu = Menu(menu)
menu.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="New Project", command=doaction)

editMenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Redo", command=doaction)

veiwMenu = Menu(menu)
menu.add_cascade(label="Veiw", menu=veiwMenu)
editMenu.add_command(label="xxx", command=doaction)

helpMenu = Menu(menu)
menu.add_cascade(label="Help", menu=editMenu)
editMenu.add_command(label="?Help", command=doaction)

# ************* buttons***********************************************



# label = Label(text=file1).place(x=60, y=60)

button1 = Button(text='Add', fg='white', bg='green', font=10,command=mfileopen).place(x=55, y=50)
button2 = Button(text='Remove', fg='white', bg='orange', font=10).place(x=120, y=50)
button3 = Button(text='Analyse', fg='white', bg='green', font=10).place(x=650, y=500)


# *********** radio ********************************************************
theLabel = Label(root, text="Language").place(x=100, y=300)

r =IntVar()
Radiobutton(root, text='Tamil', variable=r, value=1).place(x=100, y=320)
Radiobutton(root, text='Sinhala', variable=r, value=2).place(x=100, y=340)
Radiobutton(root, text='English', variable=r, value=3).place(x=100, y=360)

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







root.mainloop()