#Salarycalculation_Find_Screen
import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pymysql
def showsalarycalculationfind():
    t=tkinter.Tk()
    t.geometry('800x800')
    
    def finddata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='eps')
        cur=db.cursor()
        xa=int(e1.get())
        sql="select deptid,noofdays,finalsalary from salarycalculation where empid=%d"%(xa)
        cur.execute(sql)
        data=cur.fetchone()
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        e2.insert(0,str(data[0]))
        e3.insert(0,str(data[1]))
        e4.insert(0,data[2])
        
        
        db.close()
        
    def filldata():
        lt=[]
        db=pymysql.connect(host='localhost',user='root',password='root',database='eps')
        cur=db.cursor()
        sql="select empid from salarycalculation" 
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            lt.append(res[0])
        e1['value']=lt
        db.close()    
    def filldata1():
         lt=[]
         db=pymysql.connect(host='localhost',user='root',password='root',database='eps')
         cur=db.cursor()
         sql="select empid from salarycalculation" 
         cur.execute(sql)
         data=cur.fetchall()
         for res in data:
             lt.append(res[0])
         e2['value']=lt
         db.close()    
        
    def close():
        t.destroy()
    g=Label(t,text='SALARYCALCULATION FIND SHEET',font='elephant 25 bold',fg='black',bg='SNOW4')
    g.place(x=30,y=10)
      
    a=Label(t,text='Employee ID',font='tahoma 15 bold',bg='SNOW3')
    a.place(x=50,y=100)
    e1=ttk.Combobox(t,font='tahoma 17 bold')
    filldata()
    e1.place(x=450,y=100)
    
    b1=Button(t,text='Find',command=finddata,font='tahoma 15 bold',bg='khaki')
    b1.place(x=300,y=150)
    
    b=Label(t,text='Department ID',font='tahoma 15 bold',bg='SNOW3')
    b.place(x=50,y=200)
    e2=ttk.Combobox(t,font='tahoma 13 bold')
    filldata1()
    e2.place(x=450,y=200)
    
    d=Label(t,text='No of Days',font='tahoma 13 bold',bg='SNOW3')
    d.place(x=50,y=250)
    e3=Entry(t,width=30,font='tahoma 13 bold')
    e3.place(x=450,y=250)
    
    e=Label(t,text='Final Salary',font='tahoma 15 bold',bg='SNOW3')
    e.place(x=50,y=300)
    e4=Entry(t,width=30,font='tahoma 13 bold')
    e4.place(x=450,y=300)
    
    b2=Button(t,text='Close',command=close,font='tahoma 15 bold',bg='red')
    b2.place(x=300,y=350)
    t.config(bg='snow3')
    
    t.mainloop()