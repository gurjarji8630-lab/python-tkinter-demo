import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from HOLIDAYFIND import*
from HOLIDAYSAVE import*
from HOLIDAYSHOW import*
from HOLIDAYUPDATE import*
from HOLIDAYDELETE import*
from HOLIDAYNAVIGATOR import*

import pymysql

def showHolidaydataDashboard():
    
    t=tkinter.Tk()
    t.geometry('800x800')
    
    g=Label(t,text='HOLIDAYDATA DASHBOARD',font='ELEPHANT 25 bold',fg='black',bg='antiquewhite3')
    g.place(x=60,y=10)
   
    b1=Button(t,text='Insert',command=showholidaydatasave,font='elephant 20 bold',bg='#D6CBBF')
    b1.place(x=50,y=100)
   
    b2=Button(t,text='Delete',command=showholidaydatadelete,font='elephant 20 bold',bg='gray67')
    b2.place(x=50,y=200)
   
    b3=Button(t,text='Update',command=showholidaydataupdate,font='elephant 20 bold',bg='lavender')
    b3.place(x=50,y=300)
   
    b4=Button(t,text='Review',command=showholidaydatashow,font='elephant 20 bold',bg='ivory')
    b4.place(x=400,y=100)
   
    b5=Button(t,text='Find',command=showholidaydatafind,font='elephant 20 bold',bg='thistle3')
    b5.place(x=400,y=200)
   
    b6=Button(t,text='Navigator',command=showholidaydatanavigator,font='elephant 20 bold',bg='BISQUE3')
    b6.place(x=400,y=300)
    t.config(bg='Navajowhite2')
   
    
    t.mainloop()