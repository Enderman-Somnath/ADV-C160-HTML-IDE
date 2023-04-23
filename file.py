#Linking
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
root = Tk()

#Configuring Window
root.geometry("1280x768")
root.title("Notepad")
root.configure(background="grey")

exit1 = ImageTk.PhotoImage(Image.open("exit.jpg"))
open1 = ImageTk.PhotoImage(Image.open("open.png"))
savefile = ImageTk.PhotoImage(Image.open("save.png"))

label1filename = Label(root,text="File Name",fg="black",bg="grey",bd=0)
label1filename.place(relx=0.4,rely=0.1,anchor=CENTER)
filenameinput = Entry(root)
filenameinput.place(relx=0.5,rely=0.1,anchor=CENTER)
notepad = Text(root,bg="dark blue",fg="white")
notepad.place(relx=0.5,rely=0.5,anchor=CENTER)
#Buttons
OpenButton = Button(root,image=open1)
OpenButton.place(rely=0.1,relx=0.1,anchor=CENTER)
SaveButton = Button(root,image=savefile)
SaveButton.place(rely=0.1,relx=0.2,anchor=CENTER)
ExitButton = Button(root,image=exit1)
ExitButton.place(rely=0.1,relx=0.3,anchor=CENTER)
root.mainloop()
