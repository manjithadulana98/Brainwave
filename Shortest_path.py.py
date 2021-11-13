from tkinter import *
from  tkinter import ttk
import Final
import ast
from itertools import permutations
from itertools import chain, combinations


TSP = int( Final.var1.get())
return_point = int( Final.var2.get())
# defining the starting point      
starting_point =str(Final.start.get())
k = list(ast.literal_eval(Final.output.get()))
num_points= int(Final.data3.get())


def points(n):
    b = []
    for i in range(0,int(n)):
        t = chr(65+i)
        b.append(t)
    return b

def powerset(s):
    powerset_list = list(chain.from_iterable(combinations(s, r) for r in range(len(s) + 1)))
    powerset_list.remove(())
    return powerset_list

def out(list1,list2):
    cost = 0
    path ={}
    for i in range(0,len(list1)-1):
        element  = list2[ord(list1[i])-65][ord(list1[i+1])-65]
        if  type(element) is int:
            node = list1[i] + list1[i+1]
            path[node] =  element
            cost += element
            pass
        else:
            cost = 10000
            path =[]
            break
    return list1,cost,path


def non_repeat(starting_point,points,k,TSP):
    # removing the starting point 
    points.remove(starting_point)

    # taking all the permutations   
    perm = permutations(points)

    min_cost = 1000000

    for i in list(perm):
        if TSP ==1:
            new_list = list(starting_point)+ list(i) + list(starting_point)
        else:
            new_list = list(starting_point)+ list(i)
        new,cost_i,path1 = out(new_list,k)
        if (cost_i <= min_cost):
            min_cost = cost_i
            output = new
            path = path1
    return min_cost,output,path

point = points(num_points)

# k =[[0,10,3,'x',5],[10,0,3,8,12],[3,3,0,4,'x'],['x',8,4,0,2],[5,12,'x',2,0]]

points =point + []

repeat = non_repeat(starting_point,points,k,TSP)

t = repeat[2]

final_distance =  repeat[0]
# point_static = point +[]
points.append(starting_point)

def repeat(list3,k,points):
    Dict ={}
    point_static = points +[]
    dictionarty = list3
    route = dictionarty.keys()
    for j in route:
        a = points + []
        a.remove(j[0])
        a.remove(j[1])
        set_1 =  powerset(a)
        for all_set  in set_1 :
             list_all =  list(str(j[0])) + list(all_set) + list(str(j[1]))
             new,cost_i,path1 = out(list_all,k)
             if list3[j] >  cost_i :
                 Dict[j] = path1
    return Dict

       
navi = repeat(t,k,points)
repeated_keys = list(navi.keys())
if return_point==1 :
    for i in repeated_keys:
        final_distance -= t[i]
        t[i] = navi[i]
        final_distance += sum(list(navi[i].values()))


def final_path(t): 
    k={}
    for i in t:
        if type(t[i]) is dict:
            for j in t[i]:
                k[j] = t[i][j]
        else:
            k[i]=t[i]
    return k

t1 = list(final_path(t).keys())
t2 = list(final_path(t).values())

map_out = ''
for i in range(len(t1)):
    map_out += t1[i][0]+ '__['+str(t2[i])+']__'

map_out+=t1[-1][1]








########################################## GUI output #############################################

window =Tk()
window.title('Distance and Nodes')
window.resizable(width=0, height=0)
window.geometry("+650+300")


from PIL import Image, ImageTk

def on_resize(event):
    # resize the background image to the size of label
    image = bgimg.resize((event.width, event.height), Image.ANTIALIAS)
    # update the image of the label
    l.image = ImageTk.PhotoImage(image)
    l.config(image=l.image)

bgimg = Image.open('b.png') # load the background image
l = Label(window,bg ='#022866')
l.place(x=0, y=0, relwidth=1, relheight=1) # make label l to fit the parent window always
l.bind('<Configure>', on_resize) # on_resize will be executed whenever label l is resized

label2 =Label(window,text=map_out, bg ='#022866',font=('Arial',16),fg ='white')
label2.grid(row=0,column=0,padx=5,pady=10)

label1 =Label(window,text="shortest distance : "+str(final_distance), bg ='#022866',font=('Arial',20),fg ='white')
label1.grid(row=2,column=0,padx=5,pady=10)


button1=Button(window,command=window.destroy,text='Close',fg='white',font=('Arial',14),bg= '#014c90')
button1.grid(row =3,column = 0,padx=5,pady=10)

window.mainloop()

###################################### GUI Output ############################### 

        