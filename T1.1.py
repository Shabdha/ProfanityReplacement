from tkinter import*

def doaction():
    print("action")

window2 = Tk()

window2.title("Shabdha- Automatic Audio Replacement Tool")
window2.geometry("750x550")

# ****main menu *****************************************************
menu = Menu(window2)
window2.config(menu=menu)

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

button1 = Button(text='Back', fg='white', bg='green', font=10).place(x=200, y=500)
button2 = Button(text='Ok', fg='white', bg='green', font=10).place(x=300, y=500)
button3 = Button(text='Cancel', fg='white', bg='orange', font=10).place(x=400, y=500)









window2.mainloop()




