import sys
from tkinter import*
from tkinter import messagebox

import numpy as np
from scipy.optimize import linear_sum_assignment
v=0
def vp_start_gui():
    global main_window
    main_window = Tk()
    main_window.title("BrainWave")
    main_window['bg']='#2e4583'
    main_window.resizable(width=0, height=0)
    main_window.geometry("+650+300")
    
    frame1 = LabelFrame(main_window,bg='#2e4583',padx=5,pady=5)
    frame1.grid(row=1,column=0,padx=5,pady=5)
    frame2 = LabelFrame(main_window,text = "Enter the costs from first location\n to the last, seperated by commas",bg='#2e4583', fg='White',padx=12,pady=12,font=14)
    frame2.grid(row=2,column=0,padx=5,pady=5)
    frame3 = LabelFrame(main_window,bg='#2e4583',padx=11,pady=11)
    frame3.grid(row=3,column=0,padx=5,pady=5)
    
    
    
    #Labels
    Label(main_window,anchor=W,text ="Optimal Assignment", font = 20,bg='#2e4583',fg='White').grid(row = 0,column = 0)
    Label(frame1,anchor=W,text ="Enter the number of tasks         : ",bg='#2e4583',fg='White',font =16).grid(row = 1,column = 0)
    Label(frame1,text ="Enter the number of location      : ",bg='#2e4583',fg='White',font=16).grid(row = 2,column = 0)
    
    
    #Text Input
    tasks_entry = Entry(frame1, width = 10,font=14)
    tasks_entry.grid(row = 1,column = 1,padx=5,pady=5)
    Loc_entry = Entry(frame1, width = 10,font=14)
    Loc_entry.grid(row = 2,column = 1,padx=5,pady=5)
    
    
    
    def ok_click():
        
        entries = []
        
        global x
        try :
            num_tasks = int(tasks_entry.get())
            num_locations = int(Loc_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Invalid Input")
            return
        
    
            
        #print(num_locations,num_tasks)
        
    
        for i in range(num_tasks):
            
            Label(frame2,anchor=W,text = "Costs for the Task  "+str(i+1)+" :",bg='#2e4583',fg='White',font=16).grid(row = i+8,column = 0)
            
            en = Entry(frame2,width = 17,font=14)
            en.grid(row=i+8, column=1,padx = 5,pady = 5)
            entries.append(en)
              
  
        def submit():
            
            
            matrix=[]
            
            for entry in entries:
                a= entry.get().split(",")

                if '-' in a:
                    l = a.index('-')
                    a[l]=100000
                elif "" in a:
                    messagebox.showerror("Error", "Blank Input")
                    matrix=[]
                    return
                elif num_tasks>num_locations:
                    if len(a)>num_locations:
                        messagebox.showerror("Error", "Maximum inputs exceeded")
                        matrix=[]
                        return 
                    elif len(a)<num_locations:
                        messagebox.showerror("Error", "Minimum inputs not reached")
                        matrix=[]
                        return                 
                else:
                    if len(a)<num_locations:
                        messagebox.showerror("Error", "Maximum inputs exceeded")
                        matrix=[]
                        return 
                    elif len(a)>num_locations:
                        messagebox.showerror("Error", "Minimum inputs not reached")
                        matrix=[]
                        return                         
                if num_tasks>num_locations:
                    for q in range(num_tasks-num_locations):
                        a.append("1000000")
                  
                        
                    
                    
                    
                #print(a)
                try :
                    a= [int(t) for t in a]
                except ValueError:
                    messagebox.showerror("Error", "Invalid Input")
                    return                    
                matrix.append(a)
                #print(matrix)
                
            if num_tasks<=num_locations:
            
                cost_matrix = np.array(matrix)
                
                '''drow = np.zeros((num_locations,),dtype=int)
                cost_matrix = np.vstack((cost_matrix,drow))'''
                
                row_ind, col_ind = linear_sum_assignment(cost_matrix)
                opt_ass = col_ind
                tc = cost_matrix[row_ind, col_ind].sum()
                #print(cost_matrix)
                
                for n in range (num_tasks):
                    l1=Label(frame3,text = "Optimum Location for Task " + str(n+1) + " is Location : "+ str(chr(opt_ass[n]+65)),bg='#2e4583',fg='White',font=16).grid(row = n,column = 0)
                        
                l2=Label(frame3,text = "Total Cost (in hundred rupees) = "+str(tc), font =22,bg='#2e4583',fg='White').grid(row = n+i+12,pady=5)
                #print (opt_ass)
                

            else:    
                
                cost_matrix = np.array(matrix)
                ncost_matrix= cost_matrix.transpose 
                
                #print(cost_matrix)
                
                
                
                row_ind, col_ind = linear_sum_assignment(cost_matrix)
                opt_ass = col_ind
                tc = cost_matrix[row_ind, col_ind].sum()
                #print(cost_matrix)
                
                '''k=[]
                for t in range(num_tasks-1,-1,-1):
                        k.append(opt_ass[t])
                print(k)'''

                for n in range (num_tasks):
                    if opt_ass[n]<num_locations:
                        Label(frame3,text = "Optimum location for task " + str(n+1) + " is location: "+ str(chr(opt_ass[n]+65)),bg='#2e4583',fg='White',font=16).grid(row = n,column = 0)
                        
                Label(frame3,text = "Total Cost (in hundred rupees) = "+str(tc-(num_tasks-num_locations)*1000000), font =22,bg='#2e4583',fg='White').grid(row = n+i+12,pady=5)                
                #print (opt_ass)
                
                
                
            
            Refresh =Button(frame3, text= "Reset",bg='#2e4583',fg='White', command = refresh , width = 12)
            Refresh.grid(row = n+i+13,column = 0)   
            
            #submit["state"] = DISABLED
            
        
        submit =Button(frame2, text= "Submit", bg='#2e4583',fg='White',command = submit , width = 12,font=16)
        submit.grid(row = i+10,column = 1)              
        
        
        ok["state"] = DISABLED
        
    #Buttons
    ok = Button(frame1, text= "OK",bg='#2e4583',fg='White', command = ok_click , width = 7,font =16)
    ok.grid(row = 3,column = 1)

    main_window.mainloop()

if __name__ == '__main__':
    def refresh():
        main_window.destroy()
        vp_start_gui()

    vp_start_gui() 