from tkinter import *
from itertools import permutations
from itertools import chain, combinations





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


window =Tk()
window.title('Distance and Nodes')
window.geometry('600x300')

  

# define  the enter the path

label1 =Label(window,text='Enter the path(with commas):', fg ='black',font=('Arial',14))
label1.grid(row=0,column=0,padx=5,pady=10)

data1 =StringVar()

textbox1 = Entry (window,textvariable=data1,fg='blue',font=('Arial',14))
textbox1.grid(row =0,column =1)

# define  the enter the distance

label2 =Label(window,text='Enter the distance(with commas):', fg ='black',font=('Arial',14))
label2.grid(row=1,column=0,padx=5,pady=10)

data2 =StringVar()

textbox2 = Entry (window,textvariable=data2,fg='blue',font=('Arial',14))
textbox2.grid(row =1,column =1)

# define  the enter the number of nodes

label3 =Label(window,text='Enter the number of Destination:', fg ='black',font=('Arial',14))
label3.grid(row=2,column=0,padx=5,pady=10)

data3 =StringVar()

textbox3 = Entry (window,textvariable=data3,fg='blue',font=('Arial',14))
textbox3.grid(row =2,column =1)


output = StringVar()
TSP = IntVar()

def func():
    global k
    t11 = str(data1.get())
    m11 = t11.split(',')
    t22 = str(data2.get())
    m22 = t22.split(',')
    t33 = int(data3.get())


    node_matrix = matrix(t33)

    for i in range(len(m11)):
        element1= ord(m11[i][0])-65
        element2= ord(m11[i][1])-65
        node_matrix[element1][element2]=int(m22[i])
        node_matrix[element2][element1]=int(m22[i])
    k = node_matrix
    output.set(node_matrix)


def close():
    func()
    window.destroy()

var1 = IntVar()
c1 = Checkbutton(window, text='TSP mechanism',variable=var1, onvalue=1, offvalue=0)
c1.grid(row =3,column =0,sticky=W)
# c1.pack()


button1=Button(window,command=close,text='Enter',fg='black',font=('Arial',14))
button1.grid(row =4,column =1,sticky=W)



window.mainloop()


