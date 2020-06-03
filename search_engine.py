from tkinter import *
from tkinter.font import Font
import os
from ir_sys import *

import webbrowser

#Stemmer used to stem the queries.........
suffixes = {
        1: [u"ो",u"े",u"ू",u"ु",u"ी",u"ि",u"ा"],
        2: [u"कर",u"ाओ",u"िए",u"ाई",u"ाए",u"ने",u"नी",u"ना",u"ते",u"ीं",u"ती",u"ता",u"ाँ",u"ां",u"ों",u"ें"],
        3: [u"ाकर",u"ाइए",u"ाईं",u"ाया",u"ेगी",u"ेगा",u"ोगी",u"ोगे",u"ाने",u"ाना",u"ाते",u"ाती",u"ाता",u"तीं",u"ाओं",u"ाएं",u"ुओं",u"ुएं",u"ुआं"],
        4: [u"ाएगी",u"ाएगा",u"ाओगी",u"ाओगे",u"एंगी",u"ेंगी",u"एंगे",u"ेंगे",u"ूंगी",u"ूंगा",u"ातीं",u"नाओं",u"नाएं",u"ताओं",u"ताएं",u"ियाँ",u"ियों",u"ियां"],
        5: [u"ाएंगी",u"ाएंगे",u"ाऊंगी",u"ाऊंगा",u"ाइयाँ",u"ाइयों",u"ाइयां"],
        }


def report_msg():
	win = Toplevel(root)
	win.geometry('200x150')
	win.title('Warning!')
	msg = Message(win, width='800',text = "The Field's cannot be empty")
	msg.place(x=10,y=10)

	B = Button(win, text='Ok', width="5", command=win.destroy)
	B.place(x=70, y=80)

def result_display(ans):
	win = Toplevel(root)

	l1 = Label(win, text='Words is/are present in the following document:')
	l1.pack()

	if ans == 'No Document':
		l2 = Label(win, text=ans)
		l2.pack()

	else:
		for i in ans:
			l2 = Label(win, text=i)
			l2.pack()


	b = Button(win, text='Ok', command=win.destroy) 
	b.pack()


def hi_stem(word):
    for L in 5, 4, 3, 2, 1:
        if len(word) > L + 1:
            for suf in suffixes[L]:
                if word.endswith(suf):
                    return word[:-L]
    return word

def callback(url):
    webbrowser.open_new(url)

def search():
	a = e1.get()
	a = hi_stem(a)

	if(a=='Query 1' or a==''):
		report_msg()
	else:
		ans = query(a)
		result_display(ans)


def add():
	a = e1.get()
	a = hi_stem(a)
	b = e2.get()
	b = hi_stem(b)

	if((a=='Query 1' or a=='') or (b=='Query 2 (Optional)'or b=='')):
		report_msg()
		
	else:		
		ans = queryAND(a,b)
		result_display(ans)


def Or():
	a = e1.get()
	a = hi_stem(a)
	b = e2.get()
	b = hi_stem(b)

	if((a=='Query 1' or a=='') or (b=='Query 2 (Optional)'or b=='')):
		report_msg()
	else:	
		ans = queryOR(a,b)
		result_display(ans)

def No():
	a = e1.get()
	
	if(a=='Query 1' or a==''):
		report_msg()

	else:
		a = hi_stem(a)
		ans = Not(a)
		result_display(ans)

def index():
	os.system('python inverted.py')

root = Tk()

root.geometry('520x440')
root.title('Search Engine')

ft = Font(size=12)

l1 = Label(root, text='DHOOND-Lo-ENGINE')
l1.place(x=120, y=30, width=280, height=60)

link = Label(root, text='Click here to type hindi words')
link.place(x=50, y=80, width=280, height=60)
link.bind("<Button-1>", lambda e: callback("http://www.easyhindityping.com/"))

l2 = Label(root, text='Results Are present in Document No.')
l2.place(x=254, y=120, width=196, height=60)

l3 = Label(root, text='Result')
l3.place(x=254, y=200, width=196, height=60)

e1 = Entry(root, font=ft)
e1.insert(0, 'Query 1')
e1.place(x=50, y=120, width=170, height=60)

e2 = Entry(root, font=ft)
e2.insert(0, 'Query 2 (Optional)')
e2.place(x=50, y=190, width=170, height=60)

b1 = Button(root, text='SEARCH', command=search)
b1.place(x=50, y=260, width=80, height=60)

b2 = Button(root, text='AND', bg='yellow', command=add)
b2.place(x=50, y=330, width=80, height=60)

b3 = Button(root, text='OR', bg='yellow', command=Or)
b3.place(x=140, y=260, width=80, height=60)

b4 = Button(root, text='NOT', command=No)
b4.place(x=140, y=330, width=80, height=60)

b5 = Button(root, text='INVERTED INDEX', bg='#FFFFFF', command=index)
b5.place(x=292, y=290, width=120, height=60)

root.mainloop()