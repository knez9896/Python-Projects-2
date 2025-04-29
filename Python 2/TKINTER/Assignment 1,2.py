Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from tkinter import *
>>> win = Tk()
>>> b1 = Button(win, text="One")
>>> b2 = Button(win, text= "Two")
>>> b1.pack()
>>> b2.pack()
>>> b1.pack(side=LEFT)
>>> b2.pack(side=LEFT)
>>> b1.pack(side = LEFT, padx = 10)
>>> b2.pack(side = LEFT, padx = 10)
