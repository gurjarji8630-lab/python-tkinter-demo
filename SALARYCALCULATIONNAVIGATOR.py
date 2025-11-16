#Salarycalculation_Command_Screen
import tkinter
from tkinter import *
from tkinter import messagebox
xa=[]
xb=[]
xc=[]
xd=[]
i=0
import pymysql
def showsalarycalculationnavigator():
    t=tkinter.Tk()
    t.geometry('800x800')
    
    
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='eps')
        cur=db.cursor()
        sql="select * from salarycalculation"
        cur.execute(sql)
        data=cur.fetchall()
        global xa
        global xb
        global xc
        global xd
    
        for res in data:
            xa.append(res[0])
            xb.append(res[1])
            xc.append(res[2])
            xd.append(res[3])
           
        db.close()
        
    def firstdata():
        global i,xa,xb,xc,xd
        i=0
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        
        
        e1.insert(0,xa[i])
        e2.insert(0,xb[i])
        e3.insert(0,xc[i])
        e4.insert(0,xd[i])
        
    def nextdata():
        global i,xa,xb,xc,xd
        i=i+1
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        
        
        e1.insert(0,xa[i])
        e2.insert(0,xb[i])
        e3.insert(0,xc[i])
        e4.insert(0,xd[i])
        
        
    def lastdata():
        global i,xa,xb,xc,xd
        i=len(xa)-1
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        
        e1.insert(0,xa[i])
        e2.insert(0,xb[i])
        e3.insert(0,xc[i])
        e4.insert(0,xd[i]) 
    
        
    def predata():
        global i,xa,xb,xc,xd
        i=i-1
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
    
        
        e1.insert(0,xa[i])
        e2.insert(0,xb[i])
        e3.insert(0,xc[i])
        e4.insert(0,xd[i])
    g=Label(t,text='SALARYCALCULATION NAVIGATOR SHEET',font='elephant 22 bold',fg='black',bg='SNOW4')
    g.place(x=20,y=10)
    
    
        
    
    a=Label(t,text='Employee ID',font='tahoma 15 bold',bg='SNOW3')
    a.place(x=50,y=100)
    e1=Entry(t,width=30)
    e1.place(x=450,y=100)
    
    d=Label(t,text='Department ID',font='tahoma 15 bold',bg='SNOW3')
    d.place(x=50,y=150)
    e2=Entry(t,width=30)
    e2.place(x=450,y=150)
    
    f=Label(t,text='No of Days',font='tahoma 15 bold',bg='SNOW3')
    f.place(x=50,y=200)
    e3=Entry(t,width=30)
    e3.place(x=450,y=200)
    
    h=Label(t,text='Final Salary',font='tahoma 15 bold',bg='SNOW3')
    h.place(x=50,y=250)
    e4=Entry(t,width=30)
    e4.place(x=450,y=250)
    
    
    bt1=Button(t,text='First',command=firstdata,font='tahoma 13 bold',bg='khaki')
    bt1.place(x=100,y=350)
    
    bt1=Button(t,text='Next',command=nextdata,font='tahoma 13 bold',bg='thistle2')
    bt1.place(x=180,y=350)
    
    bt1=Button(t,text='Last',command=lastdata,font='tahoma 13 bold',bg='rosybrown')
    bt1.place(x=260,y=350)
    
    bt1=Button(t,text='Previous',command=predata,font='tahoma 13 bold',bg='skyblue')
    bt1.place(x=340,y=350)
    t.config(bg='snow3')
    bt1=Button(t,text='Close',font='tahoma 15 bold',bg='red')
    bt1.place(x=260,y=450)
    t.config(bg='snow3')
    
    filldata()
    t.mainloop()