#Leavedata_Command_Screen
import tkinter
from tkinter import *
from tkinter import messagebox
import pymysql
xa=[]
xb=[]
xc=[]
xd=[]
i=0
def showleavedatanavigator():
    t=tkinter.Tk()
    t.geometry('800x800')
    
    
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='eps')
        cur=db.cursor()
        sql="select * from leavedata"
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
        
    g=Label(t,text='LEAVE DATA NAVIGATOR SHEET',font='elephant 24 bold',fg='black',bg='HONEYDEW3')
    g.place(x=60,y=10)
    
        
    a=Label(t,text='Leave ID',font='ariel 15 bold',bg='honeydew2')
    a.place(x=50,y=100)
    e1=Entry(t,width=30)
    e1.place(x=400,y=100)
    
    d=Label(t,text='Leave Type',font='ariel 15 bold',bg='honeydew2')
    d.place(x=50,y=150)
    e2=Entry(t,width=30)
    e2.place(x=400,y=150)
    
    f=Label(t,text='No of days',font='ariel 15 bold',bg='honeydew2')
    f.place(x=50,y=200)
    e3=Entry(t,width=30)
    e3.place(x=400,y=200)
    
    h=Label(t,text='Paid',font='ariel 15 bold',bg='honeydew2')
    h.place(x=50,y=250)
    e4=Entry(t,width=30)
    e4.place(x=400,y=250)
    
    
    bt1=Button(t,text='First',command=firstdata,font='ariel 13 bold',bg='gray75')
    bt1.place(x=100,y=350)
    
    bt1=Button(t,text='Next',command=nextdata,font='ariel 13 bold',bg='gray78')
    bt1.place(x=200,y=350)
    
    bt1=Button(t,text='Last',command=lastdata,font='ariel 13 bold',bg='gray75')
    bt1.place(x=300,y=350)
    
    bt1=Button(t,text='Previous',command=predata,font='ariel 13 bold',bg='gray78')
    bt1.place(x=400,y=350)
    
    filldata()
    t.config(bg='honeydew2')
    t.mainloop()