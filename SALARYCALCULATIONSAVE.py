#Salarycalculation_Save_Screen
import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
def showsalarycalculationsave():
    import pymysql
    t=tkinter.Tk()
    t.geometry('800x800')
    
    def savedata():
        if len(e1.get())==0 or len(e2.get())==0 or len(e3.get())==0 or len(e4.get())==0:
            messagebox.showinfo('Hi','Please fill all details')
        else:
            db=pymysql.connect(host='localhost',user='root',password='root',database='eps')
            cur=db.cursor()
            xa=int(e1.get())
            xb=int(e2.get())
            xc=int(e3.get())
            xd=e4.get()
            sql="insert into salarycalculation values(%d,%d,%d,'%s')"%(xa,xb,xc,xd)
            cur.execute(sql)
            db.commit()
            db.close()
            e1.delete(0,100)
            e2.delete(0,100)
            e3.delete(0,100)
            e4.delete(0,100)
        
            messagebox.showinfo('Hi','Data Saved')
    def filldata():
        
        lt=[]
        db=pymysql.connect(host='localhost',user='root',password='root',database='eps')
        cur=db.cursor()
        sql="select empid from salarycalculation"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            lt.append(res[0])
        e1['values']=lt
             
        db.close()
    
    def filldata1():
        
        lt=[]
        db=pymysql.connect(host='localhost',user='root',password='root',database='eps')
        cur=db.cursor()
        sql="select deptid from salarycalculation"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            lt.append(res[0])
        e2['values']=lt
             
        db.close()
    g=Label(t,text='SALARYCALCULATION SAVE SHEET',font='elephant 25 bold',fg='black',bg='SNOW4')
    g.place(x=30,y=10)
    
    a=Label(t,text='Employee ID',font='tahoma 15 bold',bg='SNOW3')
    a.place(x=50,y=100)
    e1=ttk.Combobox(t)
    filldata()
    e1.place(x=450,y=100)
    
    b=Label(t,text='Department ID',font='tahoma 15 bold',bg='SNOW3')
    b.place(x=50,y=150)
    e2=ttk.Combobox(t)
    filldata1()
    e2.place(x=450,y=150)
    
    d=Label(t,text='No of Days',font='tahoma 15 bold',bg='SNOW3')
    d.place(x=50,y=200)
    e3=Entry(t,width=30)
    e3.place(x=450,y=200)
    
    e=Label(t,text='Final Salary',font='tahoma 15 bold',bg='SNOW3')
    e.place(x=50,y=250)
    e4=Entry(t,width=30)
    e4.place(x=450,y=250)
    
    
    k=Button(t,text='Save',command=savedata,font='tahoma 13 bold',bg='GRAY55')
    k.place(x=100,y=350)
    k=Button(t,text='Close',command=savedata,font='tahoma 13 bold',bg='GRAY55')
    k.place(x=450,y=350)
    t.config(bg='snow3')
    
    t.mainloop()