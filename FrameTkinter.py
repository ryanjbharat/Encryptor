from tkinter import *

root = Tk()

l1 = Label(root, text="hello")
l2 = Label(root, text="world")
f1 = Frame(root)
b1 = Button(f1, text="One button")
b2 = Button(f1, text="Another button")

l1.grid(row=0, column=0)
l2.grid(row=0, column=1)
f1.grid(row=1, column=1, sticky="nsew")

b1.pack(side="top")
b2.pack(side="top")

root.mainloop()
