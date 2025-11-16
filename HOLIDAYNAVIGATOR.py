#Holidaydata_Command_Screen
import tkinter
from tkinter import *
from tkinter import messagebox
import pymysql
xa=[]
xb=[]
xc=[]
xd=[]
i=0
def showholidaydatanavigator():
    t=tkinter.Tk()
    t.geometry('800x800')
    
  
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='eps')
        cur=db.cursor()
        sql="select * from holidaydata"
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
    g=Label(t,text='HOLIDAY NAVIGATOR SHEET',font='elephant 25 bold',fg='black',bg='rosybrown4')
    g.place(x=120,y=10)
    
        
    
    a=Label(t,text='Employee ID',font='ALGERIAN 15 bold',bg='bisque3')
    a.place(x=50,y=100)
    e1=Entry(t,width=30)
    e1.place(x=450,y=100)
    
    d=Label(t,text='Department ID',font='ALGERIAN 15 bold',bg='bisque3')
    d.place(x=50,y=150)
    e2=Entry(t,width=30)
    e2.place(x=450,y=150)
    
    f=Label(t,text='Leave Type',font='ALGERIAN 15 bold',bg='bisque3')
    f.place(x=50,y=200)
    e3=Entry(t,width=30)
    e3.place(x=450,y=200)
    
    h=Label(t,text='No of leaves',font='ALGERIAN 15 bold',bg='bisque3')
    h.place(x=50,y=250)
    e4=Entry(t,width=30)
    e4.place(x=450,y=250)
    
    
    bt1=Button(t,text='First',command=firstdata,font='ALGERIAN 13 bold',bg='GRAY55')
    bt1.place(x=100,y=350)
    
    bt1=Button(t,text='Next',command=nextdata,font='ALGERIAN 13 bold',bg='GRAY55')
    bt1.place(x=190,y=350)
    
    bt1=Button(t,text='Previous',command=predata,font='ALGERIAN 13 bold',bg='GRAY55')
    bt1.place(x=290,y=350)
    
    bt1=Button(t,text='last',command=lastdata,font='ALGERIAN 13 bold',bg='GRAY55')
    bt1.place(x=430,y=350)
    bt1=Button(t,text='Close',font='ALGERIAN 13 bold',bg='rosybrown4')
    bt1.place(x=250,y=450)
    
    filldata()
    t.config(bg='bisque3')
    t.mainloop()