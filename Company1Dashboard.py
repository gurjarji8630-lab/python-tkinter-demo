import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from COMPANY1SAVE import *
from COMPANY1FIND import *
from COMPANYNAVIGATION import *
from COMPANY1UPDATE import *
from COMPANYDELETE import *
from COMPANY1SHOW import *



import pymysql

def showCompany1Dashboard():
    
    t=tkinter.Tk()
    t.geometry('800x800')
    g=Label(t,text='COMPANY DASHBOARD',font='algerian 40 bold',fg='white',bg='#117C6F')
    g.place(x=130,y=10)
   
    b1=Button(t,text='Insert',command=showcompany1save,font='elephant 25 bold',bg='sienna3')
    b1.place(x=50,y=150) 
    
    b2=Button(t,text='Delete',command=showcompanydelete,font='elephant 25 bold',bg='#8CC152')
    b2.place(x=50,y=250)
   
    b3=Button(t,text='Update',command=showcompany1update,font='elephant 25 bold',bg='rosybrown3')
    b3.place(x=50,y=350)
   
    b4=Button(t,text='Review',command=showcompany1show,font='elephant 25 bold',bg='#37BC9B')
    b4.place(x=450,y=150)
   
    b5=Button(t,text='Find',command=showcompany1find,font='elephant 25 bold',bg='#BA6E8F')
    b5.place(x=450,y=250)
   
    b6=Button(t,text='Navigator',command=showcompanynavigation,font='elephant 25 bold',bg='#ffa600')
    b6.place(x=450,y=350)
    t.config(bg='skyblue2')
    
    t.mainloop()
    