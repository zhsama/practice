#!/usr/bin/env python
# encoding: utf-8
'''

@Author  : Zhsama
@Contact : a602693793@gmail.com 
@File    : gui.py
@Time    : 2018/10/10 19:31
@software: PyCharm

'''

from tkinter import *

# top = tkinter.Tk()
# hello = tkinter.Label(top, text='Hello World!')
# hello.pack()
# button = tkinter.Button(top, text='Quit', command=top.quit, bg='red', fg='white')
# button.pack(fill=tkinter.X, expand=1)
# tkinter.mainloop()

# def resize(ev=None):
#     label.config(font='Helvetica -%d bold' % scale.get())
#
#
# top = Tk()
# top.geometry('250x150')
#
# label = Label(top, text='Hello World!', font='Helvetica -12 bold')
# label.pack(fill=Y, expand=1)
#
# scale = Scale(top, from_=10, to=40, orient=HORIZONTAL, command=resize)
# scale.set(12)
# scale.pack(fill=X, expand=1)
#
# quit = Button(top, text="QUIT", command=top.quit, activeforeground='white', activebackground='red')
# quit.pack()
#
# mainloop()

# from functools import partial as pto
# from tkinter import Tk, Button, X
# from tkinter.messagebox import showinfo, showwarning, showerror
#
# WARN = 'warn'
# CRIT = 'crit'
# REGU = 'regu'
#
# SIGNS = {
#     'do not enter': CRIT,
#     'railroad crossing': WARN,
#     '55nspeed limit': REGU,
#     'wrong way': CRIT,
#     'merging traffic': WARN,
#     'one way': REGU,
# }
#
# critCB = lambda: showerror('Error', 'Error Button Pressed!')
# warnCB = lambda: showwarning('Warning',
#                              'Warning Button Pressed!')
# infoCB = lambda: showinfo('Info', 'Info Button Pressed!')
#
# top = Tk()
# top.title('Road Signs')
# Button(top, text='QUIT', command=top.quit,
#        bg='red', fg='white').pack()
#
# MyButton = pto(Button, top)
# CritButton = pto(MyButton, command=critCB, bg='white', fg='red')
# WarnButton = pto(MyButton, command=warnCB, bg='goldenrod1')
# ReguButton = pto(MyButton, command=infoCB, bg='white')
#
# for eachSign in SIGNS:
#     signType = SIGNS[eachSign]
#     cmd = '%sButton(text=%r%s).pack(fill=X, expand=True)' % (
#         signType.title(), eachSign,
#         '.upper()' if signType == CRIT else '.title()')
#     eval(cmd)
#
# top.mainloop()


# !/usr/bin/env python

# import os
# from time import sleep
# from tkinter import *
#
#
# class DirList:
#
#     def __init__(self, initdir=None):
#         self.top = Tk()
#         self.label = Label(self.top, text='Directory Lister' + ' v1.1')
#         self.label.pack()
#
#         self.cwd = StringVar(self.top)
#
#         self.dirl = Label(self.top, fg='blue', font=('Helvetica', 12, 'bold'))
#         self.dirl.pack()
#
#         self.dirfm = Frame(self.top)
#         self.dirsb = Scrollbar(self.dirfm)
#         self.dirsb.pack(side=RIGHT, fill=Y)
#         self.dirs = Listbox(self.dirfm, height=15,
#                             width=50, yscrollcommand=self.dirsb.set)
#         self.dirs.bind('<Double-1>', self.setdirandgo)
#         self.dirsb.config(command=self.dirs.yview)
#         self.dirs.pack(side=LEFT, fill=BOTH)
#         self.dirfm.pack()
#
#         self.dirn = Entry(self.top, width=50,
#                           textvariable=self.cwd)
#         self.dirn.bind('<Return>', self.dols)
#         self.dirn.pack()
#
#         self.bfm = Frame(self.top)
#         self.clr = Button(self.bfm, text='Clear', command=self.clrdir, activeforeground='white',
#                           activebackground='blue')
#         self.ls = Button(self.bfm, text='List Directory', command=self.dols, activeforeground='white',
#                          activebackground='green')
#         self.quit = Button(self.bfm, text='Quit', command=self.top.quit, activeforeground='white',
#                            activebackground='red')
#         self.clr.pack(side=LEFT)
#         self.ls.pack(side=LEFT)
#         self.quit.pack(side=LEFT)
#         self.bfm.pack()
#
#         if initdir:
#             self.cwd.set(os.curdir)
#             self.dols()
#
#     def clrdir(self, ev=None):
#         self.cwd.set('')
#
#     def setdirandgo(self, ev=None):
#         self.last = self.cwd.get()
#         self.dirs.config(selectbackground='red')
#         check = self.dirs.get(self.dirs.curselection())
#         if not check:
#             check = os.curdir
#         self.cwd.set(check)
#         self.dols()
#
#     def dols(self, ev=None):
#         error = ''
#         tdir = self.cwd.get()
#         if not tdir: tdir = os.curdir
#
#         if not os.path.exists(tdir):
#             error = tdir + ': no such file'
#         elif not os.path.isdir(tdir):
#             error = tdir + ': not a directory'
#
#         if error:
#             self.cwd.set(error)
#             self.top.update()
#             sleep(2)
#             if not (hasattr(self, 'last') and self.last):
#                 self.last = os.curdir
#             self.cwd.set(self.last)
#             self.dirs.config(selectbackground='LightSkyBlue')
#             self.top.update()
#             return
#
#         self.cwd.set('FETCHING DIRECTORY CONTENTS...')
#         self.top.update()
#         dirlist = os.listdir(tdir)
#         dirlist.sort()
#         os.chdir(tdir)
#         self.dirl.config(text=os.getcwd())
#         self.dirs.delete(0, END)
#         self.dirs.insert(END, os.curdir)
#         self.dirs.insert(END, os.pardir)
#         for eachFile in dirlist:
#             self.dirs.insert(END, eachFile)
#         self.cwd.set(os.curdir)
#         self.dirs.config(selectbackground='LightSkyBlue')
#
#
# def main():
#     d = DirList(os.curdir)
#     mainloop()
#
#
# if __name__ == '__main__':
#     main()
