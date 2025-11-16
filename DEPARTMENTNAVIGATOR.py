#DEPARTMENT Command_Screen
import tkinter
from tkinter import *
from tkinter import messagebox
import pymysql
xa=[]
xb=[]
xc=[]
xd=[]
i=0
def showdepartmentnavigator():
    t=tkinter.Tk()
    t.geometry('800x800')
    
    
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='eps')
        cur=db.cursor()
        sql="select * from department"
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
    def cancel():
        t.destroy()
        
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
        global i,xa,xb,xc,xd,xe,xf
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
        global i,xa,xb,xc,xd,xe,xf
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
        global i,xa,xb,xc,xd,xe,xf
        i=i-1
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
      
        
        e1.insert(0,xa[i])
        e2.insert(0,xb[i])
        e3.insert(0,xc[i])
        e4.insert(0,xd[i])
        
    g=Label(t,text='DEPARTMENT NAVIGATOR SHEET',font='ELEPHANT 25 bold',fg='black',bg='gray65')
    g.place(x=40,y=10)
        
    
    a=Label(t,text='Dept ID',font='ariel 15 bold',bg='gray73')
    a.place(x=50,y=100)
    e1=Entry(t,width=30,font='ariel 13 bold')
    e1.place(x=450,y=100)
    
    d=Label(t,text='Dname',font='ariel 15 bold',bg='gray73')
    d.place(x=50,y=150)
    e2=Entry(t,width=30,font='ariel 13 bold')
    e2.place(x=450,y=150)
    
    f=Label(t,text='HOD',font='ariel 15 bold',bg='gray73')
    f.place(x=50,y=200)
    e3=Entry(t,width=30,font='ariel 13 bold')
    e3.place(x=450,y=200)
    
    h=Label(t,text='Daysofweek',font='ariel 15 bold',bg='gray73')
    h.place(x=50,y=250)
    e4=Entry(t,width=30,font='ariel 13 bold')
    e4.place(x=450,y=250)
    
    
    bt1=Button(t,text='First',command=firstdata,font='ariel 13 bold',bg='gray85')
    bt1.place(x=200,y=400)
    
    bt1=Button(t,text='Next',command=nextdata,font='ariel 13 bold',bg='gray85')
    bt1.place(x=280,y=400)
    
    bt1=Button(t,text='Previous',command=lastdata,font='ariel 13 bold',bg='gray85')
    bt1.place(x=360,y=400)
    
    bt1=Button(t,text='Last',command=predata,font='ariel 13 bold',bg='gray85')
    bt1.place(x=480,y=400)
    bt1=Button(t,text='Close',command=cancel,font='ariel 15 bold',bg='red')
    bt1.place(x=320,y=500)
    
    
    filldata()
    t.config(bg='gray73')
    t.mainloop()