import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from DEPARTMENTSAVE import*
from DEPARTMENTNAVIGATOR import*
from DEPARTMENTUPDATE import*
from DEPARTMENTFIND import*
from DEPARTMENTDELETE import*
from DEPARTMENTSHOW import*


import pymysql

def showDepartmentDashboard():
    
    t=tkinter.Tk()
    t.geometry('800x800')
    g=Label(t,text='DEPARTMENT DASHBOARD',font='algerian 40 bold',fg='white',bg='#7B466A')
    g.place(x=110,y=10)
   
    b1=Button(t,text='Insert',command=showdepartmentsave,font='elephant 25 bold',bg='sienna3')
    b1.place(x=50,y=150) 
    
    b2=Button(t,text='Delete',command=showdepartmentdelete,font='elephant 25 bold',bg='#8CC152')
    b2.place(x=50,y=250)
   
    b3=Button(t,text='Update',command=showdepartmentupdate,font='elephant 25 bold',bg='rosybrown3')
    b3.place(x=50,y=350)
   
    b4=Button(t,text='Review',command=showdepartmentshow,font='elephant 25 bold',bg='#37BC9B')
    b4.place(x=450,y=150)
   
    b5=Button(t,text='Find',command=showdepartmentfind,font='elephant 25 bold',bg='#BA6E8F')
    b5.place(x=450,y=250)
   
    b6=Button(t,text='Navigator',command=showdepartmentnavigator,font='elephant 25 bold',bg='#ffa600')
    b6.place(x=450,y=350)
    t.config(bg='gray73')
    
    t.mainloop()