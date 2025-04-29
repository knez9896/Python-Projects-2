Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from tkinter import *
>>> win = Tk()
>>> b1 = Button(win, text="One")
>>> b2 = Button(win, text="Two")
>>> b1.grid (row=0, column=0)
>>> b2.grid (row=1, column=1)
>>> 1 = Label(win, text="This is a label")
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
>>> l = Label(win, text="This is a label")
>>> l.grid(row=1, column=0)
>>> win = Tk()
>>> f = Frame(win)
>>> b1 = Button(f, text="One")
>>> b2 = Button(f, text="Two")
>>> b3 = Button(f, text="Three")
>>> b1.pack(side=LEFT)
>>> b2.pack(side=LEFT)
>>> b3.pack(side=LEFT)
>>> l = Label(win, text="This label is over all buttons")
>>> l.pack()
>>> f.pack()
>>> b1.configure(text="Uno")
>>> def but1():
...     print("Button one was pushed")
... 
...     
>>> b1.configure(command=but1)
>>> Button one was pushed
win = Tk()
>>> v = StringVar()
>>> e = Entrz(win, textvariable = v)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    e = Entrz(win, textvariable = v)
NameError: name 'Entrz' is not defined. Did you mean: 'Entry'?
>>> e = Entry(win, textvariable = v)
>>> e.pack()
>>> v.get()
''
>>> v.get()
''
>>> v.set("this is set by the program")
