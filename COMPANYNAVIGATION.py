# COMPANY1 COMMAND DATA 
import tkinter
from tkinter import *
from tkinter import messagebox
import pymysql
xa=[]
xb=[]
xc=[]
xd=[]
xe=[]
xf=[]
xg=[]
i=0
def showcompanynavigation():
    t=tkinter.Tk()
    t.geometry('800x800')
    
    
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='eps')
        cur=db.cursor()
        sql="select * from company1"
        cur.execute(sql)
        data=cur.fetchall()
        global xa
        global xb
        global xc
        global xd
        global xe
        global xf
        global xg
        for res in data:
            xa.append(res[0])
            xb.append(res[1])
            xc.append(res[2])
            xd.append(res[3])
            xe.append(res[4])
            xf.append(res[5])
            xg.append(res[6])
        db.close()
        
    def firstdata():
        
        global i,xa,xb,xc,xd,xe,xf,xg
        i=0
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        e5.delete(0,100)
        e6.delete(0,100)
        e7.delete(0,100)
        
        e1.insert(0,xa[i])
        e2.insert(0,xb[i])
        e3.insert(0,xc[i])
        e4.insert(0,xd[i])
        e5.insert(0,xe[i])
        e6.insert(0,xf[i])
        e7.insert(0,xg[i])
        
    def nextdata():
        global i,xa,xb,xc,xd,xe,xf,xg
        i=i+1
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        e5.delete(0,100)
        e6.delete(0,100)
        e7.delete(0,100)
        
        
        e1.insert(0,xa[i])
        e2.insert(0,xb[i])
        e3.insert(0,xc[i])
        e4.insert(0,xd[i])
        e5.insert(0,xe[i])
        e6.insert(0,xf[i])
        e7.insert(0,xg[i])
        
        
    def lastdata():
        global i,xa,xb,xc,xd,xe,xf,xg
        i=len(xa)-1
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        e5.delete(0,100)
        e6.delete(0,100)
        e7.delete(0,100)
        
        e1.insert(0,xa[i])
        e2.insert(0,xb[i])
        e3.insert(0,xc[i])
        e4.insert(0,xd[i]) 
        e5.insert(0,xe[i])
        e6.insert(0,xf[i])
        e7.insert(0,xg[i])
        
    def predata():
        global i,xa,xb,xc,xd,xe,xf,xg
        i=i-1
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        e5.delete(0,100)
        e6.delete(0,100)
        e7.delete(0,100)
        
        e1.insert(0,xa[i])
        e2.insert(0,xb[i])
        e3.insert(0,xc[i])
        e4.insert(0,xd[i])
        e5.insert(0,xe[i])
        e6.insert(0,xf[i])
        e7.insert(0,xg[i])
        
    g=Label(t,text='COMPANY NAVIGATION SHEET',font='ELEPHANT 25 bold',fg='black',bg='antiquewhite3')
    g.place(x=60,y=10)
        
    a=Label(t,text='Company ID',font='ariel 15 bold',fg='black',bg='#D6CBBF')
    a.place(x=50,y=100)
    e1=Entry(t,width=30)
    e1.place(x=450,y=100)
    
    d=Label(t,text='Name',font='ariel 15 bold',fg='black',bg='#D6CBBF')
    d.place(x=50,y=150)
    e2=Entry(t,width=30)
    e2.place(x=450,y=150)
    
    f=Label(t,text='Address',font='ariel 15 bold',fg='black',bg='#D6CBBF')
    f.place(x=50,y=200)
    e3=Entry(t,width=30)
    e3.place(x=450,y=200)
    
    h=Label(t,text='City',font='ariel 15 bold',fg='black',bg='#D6CBBF')
    h.place(x=50,y=250)
    e4=Entry(t,width=30)
    e4.place(x=450,y=250)
    
    h=Label(t,text='Phone No',font='ariel 15 bold',fg='black',bg='#D6CBBF')
    h.place(x=50,y=300)
    e5=Entry(t,width=30)
    e5.place(x=450,y=300)
    
    j=Label(t,text='Email ID',font='ariel 15 bold',fg='black',bg='#D6CBBF')
    j.place(x=50,y=350)
    e6=Entry(t,width=30)
    e6.place(x=450,y=350)
    
    k=Label(t,text='Email ID',font='ariel 15 bold',fg='black',bg='#D6CBBF')
    k.place(x=50,y=400)
    e7=Entry(t,width=30)
    e7.place(x=450,y=400)
    
    bt1=Button(t,text='First',command=firstdata,font='ariel 10 bold',fg='black',bg='gray77')
    bt1.place(x=200,y=500)
    
    bt2=Button(t,text='Next',command=nextdata,font='ariel 10 bold',fg='black',bg='gray65')
    bt2.place(x=270,y=500)
     
    bt3=Button(t,text='Previous',command=predata,font='ariel 10 bold',fg='black',bg='gray77')
    bt3.place(x=350,y=500)
    
    bt4=Button(t,text='Last',command=lastdata,font='ariel 10 bold',fg='black',bg='gray65')
    bt4.place(x=440,y=500)
    t.config(bg='#D6CBBF')
    
    filldata()
    t.mainloop()
   