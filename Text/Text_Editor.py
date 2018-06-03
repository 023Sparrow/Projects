#!/usr/bin/python
# -*- coding: UTF-8 -*-

from tkinter import *
class Application(Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.text1 = Text(width=20, height=20)
        self.text1.pack(expand=YES, fill=BOTH)         #to make the textbox fill entire window
        menubar = Menu(self)
        filemenu = Menu(menubar)
        editmenu = Menu(menubar)
        toolsmenu = Menu(menubar) 
        filemenu.add_command(label = 'New', command = self.newDoc)
root = Tk()
app = Application(master=root)
app.mainloop()
