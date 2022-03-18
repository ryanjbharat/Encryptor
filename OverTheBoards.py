from tkinter import *
# from babel.dates import format_date, format_datetime, format_time
from tkcalendar import Calendar, DateEntry
from time import sleep
import json

root = Tk()

root.title("OverTheBoards")

greeting = "For a custom greeting, select 'Get Custom Greeting'!"

roster = [
    "Hoban Washburne",
    "River Tam",
    "Shepard Book",
    "Adelai Niska",
    "Warwick Harrow",
    "Malcolm Reynolds",
    "Inara Serra",
    "Simon Tam",
    "Yolanda Saffron",
    "Fess Higgins",
    "Jayne Cobb",
    "Kaylee Frye",
    "Zoe Washburne",
    "Jubal Early",
    "Atherton Wing",
    "Sheppard Badger",
    "Tracey Smith",
    "Lieutenant Womack",
    "Sheriff Bourne",
    "Clarke Nandi",
    "Magistrate Higgins",
    "Patience Whitefall",
    "Stitch Hessian"
]

positions = [
    "1 - LW",
    "1 - C ",
    "1 - RW",
    "2 - LW",
    "2 - C ",
    "2 - RW",
    "3 - LW",
    "3 - C ",
    "3 - RW",
    "4 - LW",
    "4 - C ",
    "4 - RW",
    "1 - LD",
    "1 - RD",
    "2 - LD",
    "2 - RD",
    "3 - LD",
    "3 - RD",
    "1 - G ",
    "2 - G",
    "Scratch",
    "Scratch",
    "Scratch"
]

position_dict = {
    0: "LW1",
    1: "C_1",
    2: "RW1",
    3: "LW2",
    4: "C_2",
    5: "RW2",
    6: "LW3",
    7: "C_3",
    8: "RW3",
    9: "LW4",
    10: "C_4",
    11: "RW4",
    12: "LD1",
    13: "RD1",
    14: "LD2",
    15: "RD2",
    16: "LD3",
    17: "RD3",
    18: "G_1",
    19: "G_2",
    20: "SC1",
    21: "SC2",
    22: "SC3"
}

position_list = [
    "LW1",
    "C_1",
    "RW1",
    "LW2",
    "C_2",
    "RW2",
    "LW3",
    "C_3",
    "RW3",
    "LW4",
    "C_4",
    "RW4",
    "LD1",
    "RD1",
    "LD2",
    "RD2",
    "LD3",
    "RD3",
    "G_1",
    "G_2",
    "SC1",
    "SC2",
    "SC3"
]


# roster frame creation
FLW0 = Frame(root, borderwidth=2, relief=RIDGE, padx=75)
FC_0 = Frame(root, borderwidth=2, relief=RIDGE, padx=75)
FRW0 = Frame(root, borderwidth=2, relief=RIDGE, padx=75)

FLW1 = Frame(root)
FC_1 = Frame(root)
FRW1 = Frame(root)

FLW2 = Frame(root)
FC_2 = Frame(root)
FRW2 = Frame(root)

FLW3 = Frame(root)
FC_3 = Frame(root)
FRW3 = Frame(root)

FLW4 = Frame(root)
FC_4 = Frame(root)
FRW4 = Frame(root)

FLD0 = Frame(root, borderwidth=2, relief=RIDGE, padx=75)
FRD0 = Frame(root, borderwidth=2, relief=RIDGE, padx=75)

FLD1 = Frame(root)
FRD1 = Frame(root)

FLD2 = Frame(root)
FRD2 = Frame(root)

FLD3 = Frame(root)
FRD3 = Frame(root)

FG_0 = Frame(root, borderwidth=2, relief=RIDGE, padx=75)
FG_1 = Frame(root)
FG_2 = Frame(root)

FSC0 = Frame(root, pady=50)
FSC1 = Frame(root)
FSC2 = Frame(root)
FSC3 = Frame(root)

# button and additional frame creation
FImp = Frame(root)
FExp = Frame(root)
FSave = Frame(root)
FDate = Frame(root)
FInfo = Frame(root)
FGreet = Frame(root)
FGetGreet = Frame(root)

# position labels and spacers
LW0 = Label(FLW0, text="Left Wing")
C_0 = Label(FC_0, text="Center")
RW0 = Label(FRW0, text="Right Wing")
LD0 = Label(FLD0, text="Left D")
RD0 = Label(FRD0, text="Right D")
G_0 = Label(FG_0, text="Goalie")
SC0 = Label(FSC0, text="Scratches:")

# player name labels
LW1 = Label(FLW1, text=roster[0])
C_1 = Label(FC_1, text=roster[1])
RW1 = Label(FRW1, text=roster[2])

LW2 = Label(FLW2, text=roster[3])
C_2 = Label(FC_2, text=roster[4])
RW2 = Label(FRW2, text=roster[5])

LW3 = Label(FLW3, text=roster[6])
C_3 = Label(FC_3, text=roster[7])
RW3 = Label(FRW3, text=roster[8])

LW4 = Label(FLW4, text=roster[9])
C_4 = Label(FC_4, text=roster[10])
RW4 = Label(FRW4, text=roster[11])

LD1 = Label(FLD1, text=roster[12])
RD1 = Label(FRD1, text=roster[13])

LD2 = Label(FLD2, text=roster[14])
RD2 = Label(FRD2, text=roster[15])

LD3 = Label(FLD3, text=roster[16])
RD3 = Label(FRD3, text=roster[17])

G_1 = Label(FG_1, text=roster[18])
G_2 = Label(FG_2, text=roster[19])

SC1 = Label(FSC1, text=roster[20])
SC2 = Label(FSC2, text=roster[21])
SC3 = Label(FSC3, text=roster[22])


# position selection create pos_var
pos_varFLW1 = StringVar(root)
pos_varFC_1 = StringVar(root)
pos_varFRW1 = StringVar(root)
pos_varFLW2 = StringVar(root)
pos_varFC_2 = StringVar(root)
pos_varFRW2 = StringVar(root)
pos_varFLW3 = StringVar(root)
pos_varFC_3 = StringVar(root)
pos_varFRW3 = StringVar(root)
pos_varFLW4 = StringVar(root)
pos_varFC_4 = StringVar(root)
pos_varFRW4 = StringVar(root)
pos_varFLD1 = StringVar(root)
pos_varFRD1 = StringVar(root)
pos_varFLD2 = StringVar(root)
pos_varFRD2 = StringVar(root)
pos_varFLD3 = StringVar(root)
pos_varFRD3 = StringVar(root)
pos_varFG_1 = StringVar(root)
pos_varFG_2 = StringVar(root)
pos_varFSC1 = StringVar(root)
pos_varFSC2 = StringVar(root)
pos_varFSC3 = StringVar(root)

# set default dropdown to correct position
pos_varFLW1.set(positions[0])
pos_varFC_1.set(positions[1])
pos_varFRW1.set(positions[2])
pos_varFLW2.set(positions[3])
pos_varFC_2.set(positions[4])
pos_varFRW2.set(positions[5])
pos_varFLW3.set(positions[6])
pos_varFC_3.set(positions[7])
pos_varFRW3.set(positions[8])
pos_varFLW4.set(positions[9])
pos_varFC_4.set(positions[10])
pos_varFRW4.set(positions[11])
pos_varFLD1.set(positions[12])
pos_varFRD1.set(positions[13])
pos_varFLD2.set(positions[14])
pos_varFRD2.set(positions[15])
pos_varFLD3.set(positions[16])
pos_varFRD3.set(positions[17])
pos_varFG_1.set(positions[18])
pos_varFG_2.set(positions[19])
pos_varFSC1.set(positions[20])
pos_varFSC2.set(positions[21])
pos_varFSC3.set(positions[22])

# create dropdown button object
dropdownFLW1 = OptionMenu(FLW1, pos_varFLW1, *positions)
dropdownFC_1 = OptionMenu(FC_1, pos_varFC_1, *positions)
dropdownFRW1 = OptionMenu(FRW1, pos_varFRW1, *positions)

dropdownFLW2 = OptionMenu(FLW2, pos_varFLW2, *positions)
dropdownFC_2 = OptionMenu(FC_2, pos_varFC_2, *positions)
dropdownFRW2 = OptionMenu(FRW2, pos_varFRW2, *positions)

dropdownFLW3 = OptionMenu(FLW3, pos_varFLW3, *positions)
dropdownFC_3 = OptionMenu(FC_3, pos_varFC_3, *positions)
dropdownFRW3 = OptionMenu(FRW3, pos_varFRW3, *positions)

dropdownFLW4 = OptionMenu(FLW4, pos_varFLW4, *positions)
dropdownFC_4 = OptionMenu(FC_4, pos_varFC_4, *positions)
dropdownFRW4 = OptionMenu(FRW4, pos_varFRW4, *positions)

dropdownFLD1 = OptionMenu(FLD1, pos_varFLD1, *positions)
dropdownFRD1 = OptionMenu(FRD1, pos_varFRD1, *positions)

dropdownFLD2 = OptionMenu(FLD2, pos_varFLD2, *positions)
dropdownFRD2 = OptionMenu(FRD2, pos_varFRD2, *positions)

dropdownFLD3 = OptionMenu(FLD3, pos_varFLD3, *positions)
dropdownFRD3 = OptionMenu(FRD3, pos_varFRD3, *positions)

dropdownFG_1 = OptionMenu(FG_1, pos_varFG_1, *positions)
dropdownFG_2 = OptionMenu(FG_2, pos_varFG_2, *positions)

dropdownFSC1 = OptionMenu(FSC1, pos_varFSC1, *positions)
dropdownFSC2 = OptionMenu(FSC2, pos_varFSC2, *positions)
dropdownFSC3 = OptionMenu(FSC3, pos_varFSC3, *positions)

# grid creation with frames
FLW0.grid(row=2, column=0)
FC_0.grid(row=2, column=2)
FRW0.grid(row=2, column=4)

FLW1.grid(row=3, column=0)
FC_1.grid(row=3, column=2)
FRW1.grid(row=3, column=4)

FLW2.grid(row=4, column=0)
FC_2.grid(row=4, column=2)
FRW2.grid(row=4, column=4)

FLW3.grid(row=5, column=0)
FC_3.grid(row=5, column=2)
FRW3.grid(row=5, column=4)

FLW4.grid(row=6, column=0)
FC_4.grid(row=6, column=2)
FRW4.grid(row=6, column=4)

FLD0.grid(row=7, column=1)
FRD0.grid(row=7, column=3)

FLD1.grid(row=8, column=1)
FRD1.grid(row=8, column=3)

FLD2.grid(row=9, column=1)
FRD2.grid(row=9, column=3)

FLD3.grid(row=10, column=1)
FRD3.grid(row=10, column=3)

FG_0.grid(row=11, column=2)
FG_1.grid(row=12, column=2)
FG_2.grid(row=13, column=2)

FSC0.grid(row=14, column=0)
FSC1.grid(row=14, column=1)
FSC2.grid(row=14, column=2)
FSC3.grid(row=14, column=3)

# packing
LW0.pack()
C_0.pack()
RW0.pack()

LW1.pack(side=LEFT)
C_1.pack(side=LEFT)
RW1.pack(side=LEFT)

LW2.pack(side=LEFT)
C_2.pack(side=LEFT)
RW2.pack(side=LEFT)

LW3.pack(side=LEFT)
C_3.pack(side=LEFT)
RW3.pack(side=LEFT)

LW4.pack(side=LEFT)
C_4.pack(side=LEFT)
RW4.pack(side=LEFT)

LD0.pack()
RD0.pack()

LD1.pack(side=LEFT)
RD1.pack(side=LEFT)

LD2.pack(side=LEFT)
RD2.pack(side=LEFT)

LD3.pack(side=LEFT)
RD3.pack(side=LEFT)

G_0.pack(side=LEFT)
G_1.pack(side=LEFT)
G_2.pack(side=LEFT)

SC0.pack()
SC1.pack(side=LEFT)
SC2.pack(side=LEFT)
SC3.pack(side=LEFT)

dropdownFLW1.pack(side=RIGHT)
dropdownFC_1.pack(side=RIGHT)
dropdownFRW1.pack(side=RIGHT)

dropdownFLW2.pack(side=RIGHT)
dropdownFC_2.pack(side=RIGHT)
dropdownFRW2.pack(side=RIGHT)

dropdownFLW3.pack(side=RIGHT)
dropdownFC_3.pack(side=RIGHT)
dropdownFRW3.pack(side=RIGHT)

dropdownFLW4.pack(side=RIGHT)
dropdownFC_4.pack(side=RIGHT)
dropdownFRW4.pack(side=RIGHT)

dropdownFLD1.pack(side=RIGHT)
dropdownFRD1.pack(side=RIGHT)

dropdownFLD2.pack(side=RIGHT)
dropdownFRD2.pack(side=RIGHT)

dropdownFLD3.pack(side=RIGHT)
dropdownFRD3.pack(side=RIGHT)

dropdownFG_1.pack(side=RIGHT)
dropdownFG_2.pack(side=RIGHT)

dropdownFSC1.pack(side=RIGHT)
dropdownFSC2.pack(side=RIGHT)
dropdownFSC3.pack(side=RIGHT)

# functions for position switching

def position_switch_LW1(*args):
    # ignore choosing current player position
    if pos_varFLW1.get() == positions[0]:
        return

    # find correct position to switch with
    for x in range(len(positions)):
        if pos_varFLW1.get() == positions[x]:
            
            # switch roster positions, call config to update the Labels
            roster[0], roster[x] = roster[x], roster[0]
            LW1.config(text=roster[0])
            eval(position_dict.get(x)+".config(text=roster[x])")
            pos_varFLW1.set(positions[0])
            eval("pos_varF"+position_dict.get(x)+".set(positions[x])")
            break


def position_switch_C_1(*args):
    # ignore choosing current player position
    if pos_varFC_1.get() == positions[1]:
        return

    # find correct position to switch with
    for x in range(len(positions)):
        if pos_varFC_1.get() == positions[x]:
            
            # switch roster positions, call config to update the Labels
            roster[1], roster[x] = roster[x], roster[1]
            C_1.config(text=roster[1])
            eval(position_dict.get(x)+".config(text=roster[x])")
            pos_varFC_1.set(positions[1])
            eval("pos_varF"+position_dict.get(x)+".set(positions[x])")
            break


def position_switch_RW1(*args):
    # ignore choosing current player position
    if pos_varFRW1.get() == positions[2]:
        return

    # find correct position to switch with
    for x in range(len(positions)):
        if pos_varFRW1.get() == positions[x]:
            
            # switch roster positions, call config to update the Labels
            roster[2], roster[x] = roster[x], roster[2]
            RW1.config(text=roster[2])
            eval(position_dict.get(x)+".config(text=roster[x])")
            pos_varFRW1.set(positions[2])
            eval("pos_varF"+position_dict.get(x)+".set(positions[x])")
            break


def position_switch_LW2(*args):
    # ignore choosing current player position
    if pos_varFLW2.get() == positions[3]:
        return

    # find correct position to switch with
    for x in range(len(positions)):
        if pos_varFLW2.get() == positions[x]:
            
            # switch roster positions, call config to update the Labels
            roster[3], roster[x] = roster[x], roster[3]
            LW2.config(text=roster[3])
            eval(position_dict.get(x)+".config(text=roster[x])")
            pos_varFLW2.set(positions[3])
            eval("pos_varF"+position_dict.get(x)+".set(positions[x])")
            break


def position_switch_C_2(*args):
    # ignore choosing current player position
    if pos_varFC_2.get() == positions[4]:
        return

    # find correct position to switch with
    for x in range(len(positions)):
        if pos_varFC_2.get() == positions[x]:
            
            # switch roster positions, call config to update the Labels
            roster[4], roster[x] = roster[x], roster[4]
            C_2.config(text=roster[4])
            eval(position_dict.get(x)+".config(text=roster[x])")
            pos_varFC_2.set(positions[4])
            eval("pos_varF"+position_dict.get(x)+".set(positions[x])")
            break


def position_switch_RW2(*args):
    # ignore choosing current player position
    if pos_varFRW2.get() == positions[5]:
        return

    # find correct position to switch with
    for x in range(len(positions)):
        if pos_varFRW2.get() == positions[x]:
            
            # switch roster positions, call config to update the Labels
            roster[5], roster[x] = roster[x], roster[5]
            RW2.config(text=roster[5])
            eval(position_dict.get(x)+".config(text=roster[x])")
            pos_varFRW2.set(positions[5])
            eval("pos_varF"+position_dict.get(x)+".set(positions[x])")
            break


def position_switch_LW3(*args):
    # ignore choosing current player position
    if pos_varFLW3.get() == positions[6]:
        return

    # find correct position to switch with
    for x in range(len(positions)):
        if pos_varFLW3.get() == positions[x]:
            
            # switch roster positions, call config to update the Labels
            roster[6], roster[x] = roster[x], roster[6]
            LW3.config(text=roster[6])
            eval(position_dict.get(x)+".config(text=roster[x])")
            pos_varFLW3.set(positions[6])
            eval("pos_varF"+position_dict.get(x)+".set(positions[x])")
            break


def position_switch_C_3(*args):
    # ignore choosing current player position
    if pos_varFC_3.get() == positions[7]:
        return

    # find correct position to switch with
    for x in range(len(positions)):
        if pos_varFC_3.get() == positions[x]:
            
            # switch roster positions, call config to update the Labels
            roster[7], roster[x] = roster[x], roster[7]
            C_3.config(text=roster[7])
            eval(position_dict.get(x)+".config(text=roster[x])")
            pos_varFC_3.set(positions[7])
            eval("pos_varF"+position_dict.get(x)+".set(positions[x])")
            break


def position_switch_RW3(*args):
    # ignore choosing current player position
    if pos_varFRW3.get() == positions[8]:
        return

    # find correct position to switch with
    for x in range(len(positions)):
        if pos_varFRW3.get() == positions[x]:
            
            # switch roster positions, call config to update the Labels
            roster[8], roster[x] = roster[x], roster[8]
            RW3.config(text=roster[8])
            eval(position_dict.get(x)+".config(text=roster[x])")
            pos_varFRW3.set(positions[8])
            eval("pos_varF"+position_dict.get(x)+".set(positions[x])")
            break


def position_switch_LW4(*args):
    # ignore choosing current player position
    if pos_varFLW4.get() == positions[9]:
        return

    # find correct position to switch with
    for x in range(len(positions)):
        if pos_varFLW4.get() == positions[x]:
            
            # switch roster positions, call config to update the Labels
            roster[9], roster[x] = roster[x], roster[9]
            LW4.config(text=roster[9])
            eval(position_dict.get(x)+".config(text=roster[x])")
            pos_varFLW4.set(positions[9])
            eval("pos_varF"+position_dict.get(x)+".set(positions[x])")
            break


def position_switch_C_4(*args):
    # ignore choosing current player position
    if pos_varFC_4.get() == positions[10]:
        return

    # find correct position to switch with
    for x in range(len(positions)):
        if pos_varFC_4.get() == positions[x]:
            
            # switch roster positions, call config to update the Labels
            roster[10], roster[x] = roster[x], roster[10]
            C_4.config(text=roster[10])
            eval(position_dict.get(x)+".config(text=roster[x])")
            pos_varFC_4.set(positions[10])
            eval("pos_varF"+position_dict.get(x)+".set(positions[x])")
            break


def position_switch_RW4(*args):
    # ignore choosing current player position
    if pos_varFRW4.get() == positions[11]:
        return

    # find correct position to switch with
    for x in range(len(positions)):
        if pos_varFRW4.get() == positions[x]:
            
            # switch roster positions, call config to update the Labels
            roster[11], roster[x] = roster[x], roster[11]
            RW4.config(text=roster[11])
            eval(position_dict.get(x)+".config(text=roster[x])")
            pos_varFRW4.set(positions[11])
            eval("pos_varF"+position_dict.get(x)+".set(positions[x])")
            break


def position_switch_LD1(*args):
    # ignore choosing current player position
    if pos_varFLD1.get() == positions[12]:
        return

    # find correct position to switch with
    for x in range(len(positions)):
        if pos_varFLD1.get() == positions[x]:
            
            # switch roster positions, call config to update the Labels
            roster[12], roster[x] = roster[x], roster[12]
            LD1.config(text=roster[12])
            eval(position_dict.get(x)+".config(text=roster[x])")
            pos_varFLD1.set(positions[12])
            eval("pos_varF"+position_dict.get(x)+".set(positions[x])")
            break


def position_switch_RD1(*args):
    # ignore choosing current player position
    if pos_varFRD1.get() == positions[13]:
        return

    # find correct position to switch with
    for x in range(len(positions)):
        if pos_varFRD1.get() == positions[x]:
            
            # switch roster positions, call config to update the Labels
            roster[13], roster[x] = roster[x], roster[13]
            RD1.config(text=roster[13])
            eval(position_dict.get(x)+".config(text=roster[x])")
            pos_varFRD1.set(positions[13])
            eval("pos_varF"+position_dict.get(x)+".set(positions[x])")
            break


def position_switch_LD2(*args):
    # ignore choosing current player position
    if pos_varFLD2.get() == positions[14]:
        return

    # find correct position to switch with
    for x in range(len(positions)):
        if pos_varFLD2.get() == positions[x]:
            
            # switch roster positions, call config to update the Labels
            roster[14], roster[x] = roster[x], roster[14]
            LD2.config(text=roster[14])
            eval(position_dict.get(x)+".config(text=roster[x])")
            pos_varFLD2.set(positions[14])
            eval("pos_varF"+position_dict.get(x)+".set(positions[x])")
            break


def position_switch_RD2(*args):
    # ignore choosing current player position
    if pos_varFRD2.get() == positions[15]:
        return

    # find correct position to switch with
    for x in range(len(positions)):
        if pos_varFRD2.get() == positions[x]:
            
            # switch roster positions, call config to update the Labels
            roster[15], roster[x] = roster[x], roster[15]
            RD2.config(text=roster[15])
            eval(position_dict.get(x)+".config(text=roster[x])")
            pos_varFRD2.set(positions[15])
            eval("pos_varF"+position_dict.get(x)+".set(positions[x])")
            break


def position_switch_LD3(*args):
    # ignore choosing current player position
    if pos_varFLD3.get() == positions[16]:
        return

    # find correct position to switch with
    for x in range(len(positions)):
        if pos_varFLD3.get() == positions[x]:
            
            # switch roster positions, call config to update the Labels
            roster[16], roster[x] = roster[x], roster[16]
            LD3.config(text=roster[16])
            eval(position_dict.get(x)+".config(text=roster[x])")
            pos_varFLD3.set(positions[16])
            eval("pos_varF"+position_dict.get(x)+".set(positions[x])")
            break


def position_switch_RD3(*args):
    # ignore choosing current player position
    if pos_varFRD3.get() == positions[17]:
        return

    # find correct position to switch with
    for x in range(len(positions)):
        if pos_varFRD3.get() == positions[x]:
            
            # switch roster positions, call config to update the Labels
            roster[17], roster[x] = roster[x], roster[17]
            RD3.config(text=roster[17])
            eval(position_dict.get(x)+".config(text=roster[x])")
            pos_varFRD3.set(positions[17])
            eval("pos_varF"+position_dict.get(x)+".set(positions[x])")
            break


def position_switch_G_1(*args):
    # ignore choosing current player position
    if pos_varFG_1.get() == positions[18]:
        return

    # find correct position to switch with
    for x in range(len(positions)):
        if pos_varFG_1.get() == positions[x]:
            
            # switch roster positions, call config to update the Labels
            roster[18], roster[x] = roster[x], roster[18]
            G_1.config(text=roster[18])
            eval(position_dict.get(x)+".config(text=roster[x])")
            pos_varFG_1.set(positions[18])
            eval("pos_varF"+position_dict.get(x)+".set(positions[x])")
            break


def position_switch_G_2(*args):
    # ignore choosing current player position
    if pos_varFG_2.get() == positions[19]:
        return

    # find correct position to switch with
    for x in range(len(positions)):
        if pos_varFG_2.get() == positions[x]:
            
            # switch roster positions, call config to update the Labels
            roster[19], roster[x] = roster[x], roster[19]
            G_2.config(text=roster[19])
            eval(position_dict.get(x)+".config(text=roster[x])")
            pos_varFG_2.set(positions[19])
            eval("pos_varF"+position_dict.get(x)+".set(positions[x])")
            break


def position_switch_SC1(*args):
    # ignore choosing current player position
    if pos_varFSC1.get() == positions[20]:
        return

    # find correct position to switch with
    for x in range(len(positions)):
        if pos_varFSC1.get() == positions[x]:
            
            # switch roster positions, call config to update the Labels
            roster[20], roster[x] = roster[x], roster[20]
            SC1.config(text=roster[20])
            eval(position_dict.get(x)+".config(text=roster[x])")
            pos_varFSC1.set(positions[20])
            eval("pos_varF"+position_dict.get(x)+".set(positions[x])")
            break


def position_switch_SC2(*args):
    # ignore choosing current player position
    if pos_varFSC2.get() == positions[21]:
        return

    # find correct position to switch with
    for x in range(len(positions)):
        if pos_varFSC2.get() == positions[x]:
            
            # switch roster positions, call config to update the Labels
            roster[21], roster[x] = roster[x], roster[21]
            SC2.config(text=roster[21])
            eval(position_dict.get(x)+".config(text=roster[x])")
            pos_varFSC2.set(positions[21])
            eval("pos_varF"+position_dict.get(x)+".set(positions[x])")
            break


def position_switch_SC3(*args):
    # ignore choosing current player position
    if pos_varFSC3.get() == positions[22]:
        return

    # find correct position to switch with
    for x in range(len(positions)):
        if pos_varFSC3.get() == positions[x]:
            
            # switch roster positions, call config to update the Labels
            roster[22], roster[x] = roster[x], roster[22]
            SC3.config(text=roster[22])
            eval(position_dict.get(x)+".config(text=roster[x])")
            pos_varFSC3.set(positions[22])
            eval("pos_varF"+position_dict.get(x)+".set(positions[x])")
            break




# link function to dropdown
pos_varFLW1.trace('w', position_switch_LW1)
pos_varFC_1.trace('w', position_switch_C_1)
pos_varFRW1.trace('w', position_switch_RW1)
pos_varFLW2.trace('w', position_switch_LW2)
pos_varFC_2.trace('w', position_switch_C_2)
pos_varFRW2.trace('w', position_switch_RW2)
pos_varFLW3.trace('w', position_switch_LW3)
pos_varFC_3.trace('w', position_switch_C_3)
pos_varFRW3.trace('w', position_switch_RW3)
pos_varFLW4.trace('w', position_switch_LW4)
pos_varFC_4.trace('w', position_switch_C_4)
pos_varFRW4.trace('w', position_switch_RW4)
pos_varFLD1.trace('w', position_switch_LD1)
pos_varFRD1.trace('w', position_switch_RD1)
pos_varFLD2.trace('w', position_switch_LD2)
pos_varFRD2.trace('w', position_switch_RD2)
pos_varFLD3.trace('w', position_switch_LD3)
pos_varFRD3.trace('w', position_switch_RD3)
pos_varFG_1.trace('w', position_switch_G_1)
pos_varFG_2.trace('w', position_switch_G_2)
pos_varFSC1.trace('w', position_switch_SC1)
pos_varFSC2.trace('w', position_switch_SC2)
pos_varFSC3.trace('w', position_switch_SC3)


# https://stackoverflow.com/questions/3221956/how-do-i-display-tooltips-in-tkinter
class CreateToolTip(object):
    """
    Class defining how a tooltip is created.
    """
    def __init__(self, widget, text='widget info'):
        self.waittime = 100     #miliseconds
        self.wraplength = 180   #pixels
        self.widget = widget
        self.text = text
        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.leave)
        self.widget.bind("<ButtonPress>", self.leave)
        self.id = None
        self.tw = None

    def enter(self, event=None):
        self.schedule()

    def leave(self, event=None):
        self.unschedule()
        self.hidetip()

    def schedule(self):
        self.unschedule()
        self.id = self.widget.after(self.waittime, self.showtip)

    def unschedule(self):
        id = self.id
        self.id = None
        if id:
            self.widget.after_cancel(id)

    def showtip(self, event=None):
        x = y = 0
        x, y, cx, cy = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 20
        # creates a toplevel window
        self.tw = Toplevel(self.widget)
        # Leaves only the label and removes the app window
        self.tw.wm_overrideredirect(True)
        self.tw.wm_geometry("+%d+%d" % (x, y))
        label = Label(self.tw, text=self.text, justify='left',
                       background="#ffffff", relief='solid', borderwidth=1,
                       wraplength = self.wraplength)
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tw
        self.tw= None
        if tw:
            tw.destroy()


info = Label(FInfo, text="Choose Date of Game:")
FInfo.grid(row=1, column=0)

info.pack()


# Date Selector Creation
calendar = DateEntry(FDate, width=12, background='darkblue', foreground='white', borderwidth=2)

FDate.grid(row=1, column=1, padx=10, pady=10)
calendar.pack()


# function for exporting roster to a txt file
def export_roster():
    # create dictionary with positions and players
    i = 0
    export_dict = {key: None for key in position_list}
    for key in position_list:
        export_dict[key] = roster[i]
        i += 1

    # create json object, write to file
    json_object = json.dumps(export_dict, indent=4)
    with open("roster_export.txt", "w") as outfile:
        outfile.write(json_object)


# Export Roster Button
ExportRoster = Button(FExp, text="Export Roster", command=export_roster, padx=50, pady=10)

# Set position and pack
FExp.grid(row=15, column=4)
ExportRoster.pack()


# function for importing roster from a txt file
def import_roster():
    print("Roster import will happen here.")


# Import Roster Button
ImportRoster = Button(FImp, text="Import Roster\n(Non-Functional)", command=import_roster, padx=50, pady=10)

# Set position and pack
FImp.grid(row=15, column=2)
ImportRoster.pack()

# access teammate's microservice and get a greeting
def random_greeting():
    global greeting
    global GreetingDisplay

    # trigger microservice
    with open('comm_file.txt', 'w') as greet_file:
        greet_file.write("start")

    sleep(0.3)

    # read from microservice text file
    with open('comm_file.txt', 'r') as greet_file:
        greeting_text = greet_file.readline()

    # set value to greeting variable and update the display
    greeting = greeting_text
    GreetingDisplay.config(text=greeting)
    return


# create GetGreeting button
GetGreeting = Button(FGetGreet, text="Get Custom Greeting", command=random_greeting, padx=50, pady=10)
FGetGreet.grid(row=15, column=0)
GetGreeting.pack()

# create GreetingDisplay label
GreetingDisplay = Label(FGreet, text=greeting)
FGreet.grid(row=1, column=3)
GreetingDisplay.pack()

# microservice function to watch roster_export.txt for "start", call export_roster when selected
# def watch_file():
#     start = "start"
#     file_text = ""
#
#     while file_text != start:
#         with open('roster_export.txt', 'r') as infile:
#             file_text = infile.readline()
#
#     export_roster()
#     return


# Create microservice button
# FMicro = Frame(root)
# microButton = Button(FMicro, text="Start Export Microservice", command=watch_file, padx=50, pady=10)
# FMicro.grid(row=15, column=3)
# microButton.pack()

# Create Tooltip Text
ImportRoster_TTP = CreateToolTip(ImportRoster, "WARNING: Importing a roster will overwrite current roster. Please ensure you have saved your data.")
# Microservice_TTP = CreateToolTip(microButton, "WARNING: Program will not function until microservice call is completed.")

# main loop
root.mainloop()
