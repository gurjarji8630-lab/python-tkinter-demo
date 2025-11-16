import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from HODFIND import*
from HODSAVE import*
from HODUPDATE import*
from HODDELETE import*
from HODSHOW import*
from HODNAVIGATOR import*




import pymysql

def showHODDashboard():
    
    t=tkinter.Tk()
    t.geometry('800x800')
    
    g=Label(t,text='HOD DASHBOARD',font='algerian 40 bold',fg='white',bg='#235347')
    g.place(x=150,y=10)
   
    b1=Button(t,text='Insert',command=showhodsave,font='elephant 25 bold',bg='sienna3')
    b1.place(x=50,y=150) 
    
    b2=Button(t,text='Delete',command=showhoddelete,font='elephant 25 bold',bg='#8CC152')
    b2.place(x=50,y=250)
   
    b3=Button(t,text='Update',command=showhodupdate,font='elephant 25 bold',bg='rosybrown3')
    b3.place(x=50,y=350)
   
    b4=Button(t,text='Review',command=showhodshow,font='elephant 25 bold',bg='#37BC9B')
    b4.place(x=450,y=150)
   
    b5=Button(t,text='Find',command=showhodfind,font='elephant 25 bold',bg='#BA6E8F')
    b5.place(x=450,y=250)
   
    b6=Button(t,text='Navigator',command=showhodnavigator,font='elephant 25 bold',bg='#ffa600')
    b6.place(x=450,y=350)
    t.config(bg='#B5C99A')
    
    t.mainloop()