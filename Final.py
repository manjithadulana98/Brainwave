from tkinter import *
from itertools import permutations
from itertools import chain, combinations
from  tkinter import ttk
from PIL import Image, ImageTk

import csv
from os import read
import tkinter as tk
from tkinter.filedialog import askopenfilename
import pandas as pd


def matrix(n):
    
    a= []
    for j in range(n):
        b=[]
        for i in range(n):
            if i == j:
                b.append(0)
            else:
                b.append('x')
        a.append(b)
    return a

def import_csv_data():
    global v
    csv_file_path = askopenfilename()
    t = read_csv(csv_file_path)
    v.set(t)


def read_csv(word):

  with open(word, mode ='r')as file:
    global k
    # reading the CSV file
    csvFile = csv.reader(file)
    next(csvFile)
    # displaying the contents of the CSV file
    nodes = []
    distance = []
    destination =[]
    for lines in csvFile:
        destination.append(lines[0])
        destination.append(lines[1])
        nodes.append(lines[0]+lines[1])
        distance.append(lines[2])
        
        
    number = len(set(destination))
    data3.set(number)
    node_matrix = matrix(number)

    for i in range(len(nodes)):
        element1= ord(nodes[i][0])-65
        element2= ord(nodes[i][1])-65
        node_matrix[element1][element2]=int(distance[i])
        node_matrix[element2][element1]=int(distance[i])
        
    k = node_matrix
    output.set(node_matrix)




window =Tk()
window.title('Optimize Path')
window.resizable(width=0, height=0)
window.geometry("+650+300")
# window.geometry('450x200')


def on_resize(event):
    # resize the background image to the size of label
    image = bgimg.resize((event.width, event.height), Image.ANTIALIAS)
    # update the image of the label
    l.image = ImageTk.PhotoImage(image)
    l.config(image=l.image)


def close2():
    window.destroy()


bgimg = Image.open('b.png') # load the background image
l = Label(window)
l.place(x=0, y=0, relwidth=1, relheight=1) # make label l to fit the parent window always
l.bind('<Configure>', on_resize) # on_resize will be executed whenever label l is resized

label4 =Label(window,text='Enter the Starting loaction:', fg ='white',font=('Arial',14),bg= '#022866')
label4.grid(row=4,column=0,padx=5,pady=10)

label4 =Label(window,text='', fg ='white',font=('Arial',14),bg= '#022866')
label4.grid(row=1,column=0,padx=0,pady=0)

start =StringVar()

textbox4 = Entry (window,textvariable=start,fg='blue',font=('Arial',14))
textbox4.grid(row =4,column =1)


data3 = IntVar()
output = StringVar()
TSP = IntVar()
var1 = IntVar()

c1 = Checkbutton(window, text='TSP mechanism',variable=var1, onvalue=1, offvalue=0,bg= '#022866',fg='red',font=('Arial',16))
c1.grid(row =5,column =0,sticky=W)

var2= IntVar()

c1 = Checkbutton(window, text='With repeat nodes',variable=var2, onvalue=1, offvalue=0,bg= '#022866',fg='red',font=('Arial',16))
c1.grid(row =6,column =0,sticky=W)


v = StringVar()
Button(window, text='Browse Data Set',command=import_csv_data,bg= '#014c90',fg='white',font= 16).grid(row=2, column=1)
button2=Button(window,command=close2,text='Enter',fg='white',font=('Arial',16),bg= '#014c90')
button2.grid(row =9,column =1,sticky=W)
window.mainloop()

