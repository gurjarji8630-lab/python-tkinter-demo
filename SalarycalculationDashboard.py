import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from SALARYCALCULATIONSAVE import*
from SALARYCALCULATIONFIND import*
from SALARYCALCULATIONUPDATE import*
from SALARYCALCULATIONDELETE import*
from SALARYCALCULATIONNAVIGATOR import*
from SALARYCALCULATIONSHOW import*



import pymysql

def showSalarycalculationDashboard():
    t=tkinter.Tk()
    t.geometry('800x800')
    
    g=Label(t,text='SALARYDEDUCTION DASHBOARD',font='ELEPHANT 25 bold',fg='black',bg='antiquewhite3')
    g.place(x=60,y=10)
  
    b1=Button(t,text='Insert',command=showsalarycalculationsave,font='elephant 20 bold',bg='#D6CBBF')
    b1.place(x=50,y=100)
  
    b2=Button(t,text='Delete',command=showsalarycalculationdelete,font='elephant 20 bold',bg='gray67')
    b2.place(x=50,y=200)
  
    b3=Button(t,text='Update',command=showsalarycalculationupdate,font='elephant 20 bold',bg='lavender')
    b3.place(x=50,y=300)
  
    b4=Button(t,text='Review',command=showsalarycalculationshow,font='elephant 20 bold',bg='ivory')
    b4.place(x=400,y=100)
  
    b5=Button(t,text='Find',command=showsalarycalculationfind,font='elephant 20 bold',bg='thistle3')
    b5.place(x=400,y=200)
  
    b6=Button(t,text='Navigator',command=showsalarycalculationnavigator,font='elephant 20 bold',bg='BISQUE3')
    b6.place(x=400,y=300)
    t.config(bg='PLUM3')
  
    t.mainloop()
  