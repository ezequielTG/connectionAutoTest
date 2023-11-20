from tkinter import *


def build_label(col_ab, row, win, txt):
    label = Label(win, width=10, height=2, text=txt, font='Arial 14', anchor=W)
    label.grid(column=col_ab, row=row, padx=8, pady=5, sticky=NSEW)
    return label


def build_entry(col_ent, row, win):
    entry = Entry(win, width=16, font='Arial 14')
    entry.grid(column=col_ent, row=row, padx=10, pady=5)
    return entry
