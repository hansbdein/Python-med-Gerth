# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 11:22:39 2022

@author: Hans
"""

import tkinter



class Counter:
    def do_quit(self):
        self.root.destroy()
    def add(self, x):
        self.counter += x
        self.count.set(self.counter)
    def __init__(self, message):
        self.counter = 0
        self.root = tkinter.Toplevel() # new window
        self.root.title("Counter")
        self.label = tkinter.Label(self.root, text=message)
        self.label.grid(row=0, columnspan=3)
        self.minus_button = tkinter.Button(self.root, text="-", command=lambda: self.add(-1))
        self.minus_button.grid(row=1, column=0)
        self.count = tkinter.IntVar()
        self.count_label = tkinter.Label(self.root, textvariable=self.count)
        self.count_label.grid(row=1, column=1)
        self.plus_button = tkinter.Button(self.root, text="+", command=lambda: self.add(+1))
        self.plus_button.grid(row=1, column=2)
        
class Counter_app:
    def __init__(self):
        self.counters = 0
        self.root = tkinter.Tk()
        self.create = tkinter.Button(self.root, text="Create counter", command=self.new_counter)
        self.create.pack()
    def new_counter(self):
        Counter("Counter " + chr(ord('A') + self.counters))
        self.counters += 1
        
        
Counter_app()
tkinter.mainloop()