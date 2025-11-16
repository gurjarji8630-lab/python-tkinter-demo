#find and fill data in attendence table
import tkinter
from tkinter import * 
from tkinter import messagebox
from tkinter import ttk
import pymysql
def showattendancefind():

    t=tkinter.Tk()
    t.geometry('800x800')
    
    def finddata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='eps')
        cur=db.cursor()
        xa=int(e1.get())
        sql="select month,dateofattendance from attendance where empid=%d"%(xa)
        cur.execute(sql)
        data=cur.fetchone()
        e2.delete(0,100)
        e3.delete(0,100)
        
        e2.insert(0,data[0])
        e3.insert(0,data[1])
       
       
        db.close()
    
    def filldata():
        lt=[]
        db=pymysql.connect(host='localhost',user='root',password='root',database='eps')
        cur=db.cursor()
        sql="select empid from attendance"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            lt.append(res[0])
        e1['values']=lt
             
        db.close()
    def close():
        t.destroy()
    g=Label(t,text='ATTENDANCE FIND SHEET',font='elephant 25 bold',fg='black',bg='rosybrown4')
    g.place(x=80,y=10)
    
    a=Label(t,text='Emp Id',font='tahoma 15 bold',bg='#a59694')
    a.place(x=50,y=100)
    e1=ttk.Combobox(t,font='tahoma 13 bold')
    filldata()
    e1.place(x=400,y=100)
    
    bt=Button(t,text='Find',command=finddata,font='tahoma 15 bold',bg='snow2')
    bt.place(x=250,y=160)
    
    
    
    b=Label(t,text='Month',font='tahoma 15 bold',bg='#a59694')
    b.place(x=50,y=250)
    e2=Entry(t,width=20,font='tahoma 15 bold')
    e2.place(x=400,y=250)
    
    d=Label(t,text='Date of Attendance',font='tahoma 15 bold',bg='#a59694')
    d.place(x=50,y=300)
    e3=Entry(t,width=20,font='tahoma 15 bold')
    e3.place(x=400,y=300)
    t.config(bg='#a59694')
    bt=Button(t,text='CLOSE',command=close,font='tahoma 15 bold',bg='snow2')
    bt.place(x=250,y=400)
    
    
    
    t.mainloop()