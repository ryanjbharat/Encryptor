from tkinter import *

root = Tk()

def myCLick():
    myLabel = Label(root, text="Look at me! Button was clicked!")
    myLabel.pack()


myButton = Button(root, text="Click me!", padx=50, pady=10, command=myCLick)
myButton.pack()


root.mainloop()
