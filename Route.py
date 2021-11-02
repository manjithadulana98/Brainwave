
import GUI
import ast

TSP = int( GUI.var1.get())
def points(n):
    b = []
    for i in range(0,int(n)):
        t = chr(65+i)
        b.append(t)
    return b

point = points(int(GUI.data3.get()))

# k =[[0,10,3,'x',5],[10,0,3,8,12],[3,3,0,4,'x'],['x',8,4,0,2],[5,12,'x',2,0]]

k = list(ast.literal_eval(GUI.output.get()))


points =point + []

from itertools import permutations
from itertools import chain, combinations


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
                                         

# defining the starting point      
starting_point = 'E'



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

repeat = non_repeat(starting_point,points,k,TSP)

t = repeat[2]
t1 =  repeat[0]
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
for i in repeated_keys:
    t1 -= t[i]
    t[i] = navi[i]
    t1 += sum(list(navi[i].values()))

# print(t1)
# print(t)

from tkinter import *
window =Tk()
window.title('Distance and Nodes')
window.geometry('500x300')

label1 =Label(window,text="shortest Distance : "+str(t1), fg ='red',font=('Arial',14))
label1.grid(row=0,column=0,padx=5,pady=10)

window.mainloop()


        