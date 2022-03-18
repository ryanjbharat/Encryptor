from tkinter import *

root = Tk()


# Create Labels
myLabel1 = Label(root, text="Hello world!")
myLabel2 = Label(root, text="My name is Jacob")

# put onto screen
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=2)

root.mainloop()
