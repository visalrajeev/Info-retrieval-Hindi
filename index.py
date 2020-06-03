from tkinter import *
import os

def start():
	os.system("python search_engine.py")

def instruction():
	os.system("instruction.txt")

root = Tk()

root.geometry('310x220')
root.title('Welcome')

l1 = Label(root, text='Welcome to DHOONDO-Lo-ENGINE')
l1.place(x=45, y=20, width=230, height=50)

b1 = Button(root, text='START SEARCH', command=start)
b1.place(x=100, y=80, width=120, height=40)

b2 = Button(root, text='INSTRUCTION', command=instruction)
b2.place(x=100, y=130, width=120, height=40)


root.mainloop()