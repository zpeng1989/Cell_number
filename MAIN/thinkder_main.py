"""
Created on Mon Apr  9 17:31:52 2018

@author: zhangp
"""

import tkinter 
import tkinter as tk
from tkinter import filedialog
import cellnumber
import os
from PIL import Image,ImageTk

root = tkinter.Tk()
root.title('my window')
root.geometry('1200x800')


var = tk.StringVar()
lp = tk.Label(root, bg='yellow', width=50, text='input')
lp.place(x=3,y=40)

def openfile():
    r = filedialog.askopenfilename(title='打开文件', filetypes=[('*.png', '*.jpeg *.jpg'), ('All Files', '*')])
    var.set(r)

btn1 = tkinter.Button(root, text='File Open', command=openfile)
btn1.place(x=3,y=3)

var1 = tk.IntVar()
l = tk.Label(root, bg='yellow', width=20, text='empty')
l.place(x=3,y=80)

def print_selection(v):
    vb1 = v
    l.config(text='you have selected ' + v)

s = tk.Scale(root, label='colour unmber cut', from_=1, to=255, orient=tk.HORIZONTAL,length=300, showvalue=0, tickinterval=50, resolution=1, command=print_selection)
s.place(x=3,y=110)

var2 = tk.IntVar()

l1 = tk.Label(root, bg='yellow', width=20, text='empty')
l1.place(x=3,y=180)

def print_selection(v1):
    l1.config(text='you have selected ' + v1)

s1 = tk.Scale(root, label='area', from_=1, to=20, orient=tk.HORIZONTAL,length=300, showvalue=0, tickinterval=5, resolution=1, command=print_selection)
s1.place(x=3,y=210)

var3 = tk.StringVar()

l2 = tk.Label(root, bg='yellow', width=20, text='empty')
l2.place(x=3,y=280)

def print_selection(v2):
    l2.config(text='you have selected ' + v2)
s2 = tk.Scale(root, label='area ratio', from_=0, to=1, orient=tk.HORIZONTAL,length=300, showvalue=0, tickinterval=0.1, resolution=0.01, command=print_selection)
s2.place(x=3,y=310)

def hit_me():
    path_var = var.get()
    var1 = s.get()
    var2 = s1.get()
    var3 = s2.get()
    lp = tk.Label(root, bg='yellow', width=50, text=path_var)
    lp.place(x=3,y=40)
    if not os.path.exists(path_var):
        lpp = tk.Label(root, bg='yellow', width=50, text='path is not exit')
        lpp.place(x=3,y=500)
    elif not float(var1):
        lpp = tk.Label(root, bg='yellow', width=50, text='cut off is need numric')
        lpp.place(x=3,y=500)
    elif not float(var2):
        lpp = tk.Label(root, bg='yellow', width=50, text='cut area is need numric')
        lpp.place(x=3,y=500)
    elif not float(var3):
        lpp = tk.Label(root, bg='yellow', width=50, text='screen ratio is need numric')
        lpp.place(x=3,y=500)
    else:
        [one,two,three,four,five,six,seven,eight] = cellnumber.total_number_function(path_var, var1, var2, var3)
        lpp = tk.Label(root, bg='yellow', width=20, text='cell number:')
        lpp.place(x=3,y=500)
        lpp = tk.Label(root, bg='red', width=20, text=one)
        lpp.place(x=3,y=520)
        lpp = tk.Label(root, bg='yellow', width=20, text='Maybe cell number:')
        lpp.place(x=3,y=550)
        lpp = tk.Label(root, bg='red', width=20, text=two)
        lpp.place(x=3,y=570)
        lpp = tk.Label(root, bg='yellow', width=20, text='number ratio:')
        lpp.place(x=3,y=600)
        lpp = tk.Label(root, bg='red', width=20, text=three)
        lpp.place(x=3,y=620)
        lpp = tk.Label(root, bg='yellow', width=20, text='area ratio:')
        lpp.place(x=3,y=650)
        lpp = tk.Label(root, bg='red', width=20, text=four)
        lpp.place(x=3,y=670)
        def pic(pathway,x_w,y_w):
            img_png = tk.PhotoImage(file = pathway)
            lpp = tk.Label(root, image = img_png)
            lpp.img_png = img_png
            lpp.place(x=x_w,y=y_w) 
        pic(five,400,10)
        pic(six,700,10)
        pic(seven,400,410)
        pic(eight,700,410)
        

b = tk.Button(root, 
    text='hit me',     
    width=15, height=2, 
    command=hit_me)   
b.place(x=3,y=400) 
root.mainloop()

