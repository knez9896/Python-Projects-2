Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from tkinter import *
>>> win = Tk()
>>> lb = Listbox(win, height=3)
>>> lb.pack()
>>> lb.insert(END, "first entry")
>>> lb.insert(END, "second entry")
>>> lb.insert(END, "third entry")
>>> lb.insert(END, "fourth entry")
>>> sb = Scrollbar(win, orient=VERTICAL)
>>> sb.pack(side=LEFT, fill=Y)
>>> sb.configure(command=lb.yview)
>>> lb.configure(yscrollcommand=sb.set)
>>> lb.curselection()
(1,)
