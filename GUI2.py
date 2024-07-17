# import tkinter as tk
from tkinter import *


def on_click():
    lbs = tv_thb.get() / 36
    tv_lbs.set(f'{lbs:.2f} USD')
    lbs2 = tv_us.get() * 36
    tv_lbs2.set(f'{lbs2:.2f} THB')


root = Tk()
root.option_add("*Font", "impact 20")
tv_thb = DoubleVar()
tv_lbs = StringVar()
tv_us = DoubleVar()
tv_lbs2 = StringVar()

Entry(root, textvariable=tv_thb, width=7, justify="right").pack(side=LEFT, padx=10)
Label(root, text="THB").pack(side=LEFT, padx=10)
Button(root, text=" = ", bg="green", command=on_click).pack(side=LEFT)
Label(root, textvariable=tv_lbs).pack(side=LEFT)
Entry(root, textvariable=tv_us, width=7, justify="right").pack(side=LEFT, padx=10)
Label(root, text="USD").pack(side=LEFT, padx=10)
Button(root, text=" = ", bg="green", command=on_click).pack(side=LEFT)
Label(root, textvariable=tv_lbs2).pack(side=LEFT)
root.mainloop()