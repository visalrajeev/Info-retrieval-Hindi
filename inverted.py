from tkinter import *
from tkinter.font import Font
from ir_sys import *

root = Tk()
root.geometry('290x340')
root.title('Inverted Indexes')

ft = Font(size=12)

l = Label(root, text='Inverted index are:', font=ft)
l.place(x=72.5, y=20, width=145, height=40)

ans = get_invert()

scrollbar = Scrollbar(root)
scrollbar.pack( side = RIGHT, fill = Y )

mylist = Listbox(root, yscrollcommand = scrollbar.set )

for x,y in ans.items():
	a = x,y
	mylist.insert(END, a)
	

mylist.place(x=55, y=70, width=180, height=180)
scrollbar.config( command = mylist.yview )

b = Button(root, text='Okay', command=root.destroy, font=ft)
b.place(x=100, y=276, width=90, height=40)

root.mainloop()

