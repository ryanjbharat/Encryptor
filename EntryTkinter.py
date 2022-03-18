from tkinter import *

root = Tk()

e = Entry(root, width=50, borderwidth=5)
e.pack()
e.insert(0, "Enter your name: ")


def myCLick():
    hello = "Hello " + e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()


myButton = Button(root, text="Enter your name.", padx=50, pady=10, command=myCLick)
myButton.pack()


root.mainloop()
