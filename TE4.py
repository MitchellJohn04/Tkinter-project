from Tkinter import *

import tkFileDialog

import tkMessageBox

from tkColorChooser import askcolor

import datetime

import webbrowser

from tkFileDialog import askopenfilename, asksaveasfilename


def funA():
    def funA1():
        def funA12():
            # stuff

    def funA2():
        # stuff

def funB():
    def funB1():
        # stuff

    def funB2():
        # stuff

def funC():
    def funC1():
        # stuff

    def funC2():
        # stuff


root = tk.Tk()

button1 = tk.Button(root, command=funA)
button1.pack()


button2 = tk.Button(root, command=funB)
button2.pack()


button3 = tk.Button(root, command=funC)
button3.pack()