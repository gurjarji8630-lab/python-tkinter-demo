#HOD_Command_Screen
import tkinter
from tkinter import *
from tkinter import messagebox
import pymysql
xa=[]
xb=[]
xc=[]
xd=[]
i=0 
def showhodnavigator():
    t=tkinter.Tk()
    t.geometry('800x800')
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='eps')
        cur=db.cursor()
        sql="select * from hod"
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
    g=Label(t,text='HOD NAVIGATOR DATA SHEET',font='ELEPHANT 35 bold',fg='WHITE',bg='#BA6E8F')
    g.place(x=160,y=10)
    
    a=Label(t,text='HOD ID',font='arial 30 bold',bg='rosybrown3')
    a.place(x=50,y=150)
    e1=Entry(t,width=20,font='ariel 25 bold')
    e1.place(x=600,y=150)
    
    b=Label(t,text='Department ID',font='ariel 30 bold',bg='rosybrown3')
    b.place(x=50,y=250)
    e2=Entry(t,width=20,font='ariel 25 bold')
    e2.place(x=600,y=250)
    
    d=Label(t,text='HOD Name',font='ariel 30 bold',bg='rosybrown3')
    d.place(x=50,y=350)
    e3=Entry(t,width=20,font='ariel 25 bold')
    e3.place(x=600,y=350)
    
    e=Label(t,text='Employee ID',font='ariel 30 bold',bg='rosybrown3')
    e.place(x=50,y=450)
    e4=Entry(t,width=20,font='ariel 25 bold')
    e4.place(x=600,y=450)
    
    bt1=Button(t,text='First',command=firstdata,font='ariel 25 bold',bg='#98A77C',fg='white')
    bt1.place(x=100,y=550)
    
    bt2=Button(t,text='Next',command=nextdata,font='ariel 25 bold',bg='#98A77C',fg='white')
    bt2.place(x=240,y=550)
    
    bt3=Button(t,text='Last',command=lastdata,font='ariel 25 bold',bg='#98A77C',fg='white')
    bt3.place(x=380,y=550)
    
    bt4=Button(t,text='Previous',command=predata,font='ariel 25 bold',bg='#98A77C',fg='white')
    bt4.place(x=540,y=550)
    t.config(bg='rosybrown3')
    
    filldata()
    t.mainloop()