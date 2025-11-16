#last,first,next,previous attendence
import tkinter
from tkinter import * 
from tkinter import messagebox
import pymysql
xa=[]
xb=[]
xc=[]
 
i=0
 
def showattendancenavigator():

    t=tkinter.Tk()
    t.geometry('800x800')
    
   
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='eps')
        cur=db.cursor()
        sql="select * from attendance"
        cur.execute(sql)
        data=cur.fetchall()
        global xa
        global xb
        global xc
        
        for res in data:
            xa.append(res[0])
            xb.append(res[1])
            xc.append(res[2])
            
        db.close()
        
    def firstdata():
        global i,xa,xb,xc
        i=0
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        
        
        e1.insert(0,xa[i])
        e2.insert(0,xb[i])
        e3.insert(0,xc[i])
        
        
    def nextdata():
            global i,xa,xb,xc
            i=i+1
            e1.delete(0,100)
            e2.delete(0,100)
            e3.delete(0,100)
            
            
            e1.insert(0,xa[i])
            e2.insert(0,xb[i])
            e3.insert(0,xc[i])
            
            
    def prevdata():
            global i,xa,xb,xc
            i=i-1
            e1.delete(0,100)
            e2.delete(0,100)
            e3.delete(0,100)
           
            
            e1.insert(0,xa[i])
            e2.insert(0,xb[i])
            e3.insert(0,xc[i])
            
        
    def lastdata():
            global i,xa,xb,xc
            i=len(xa)-1
            e1.delete(0,100)
            e2.delete(0,100)
            e3.delete(0,100)
           
            
            e1.insert(0,xa[i])
            e2.insert(0,xb[i])
            e3.insert(0,xc[i])
    g=Label(t,text='ATTENDANCE NAVIGATOR SHEET',font='elephant 25 bold',fg='black',bg='rosybrown4')
    g.place(x=50,y=10)
           
    a=Label(t,text='Empid',font='tahoma 15 bold',bg='#a59694')
    a.place(x=50,y=100)
    e1=Entry(t,width=20,font='tahoma 15 bold')
    e1.place(x=400,y=100)
    
    
    b=Label(t,text='Month',font='tahoma 15 bold',bg='#a59694')
    b.place(x=50,y=150)
    e2=Entry(t,width=20,font='tahoma 15 bold')
    e2.place(x=400,y=150)
    
    d=Label(t,text='Date Of Attendance',font='tahoma 15 bold',bg='#a59694')
    d.place(x=50,y=200)
    e3=Entry(t,width=20,font='tahoma 15 bold')
    e3.place(x=400,y=200)
    
    
    
    
    b1=Button(t,text='First',command=firstdata,font='tahoma 15 bold',bg='cornsilk2')
    b1.place(x=100,y=300)
    
    b2=Button(t,text='Next',command=nextdata,font='tahoma 15 bold',bg='skyblue')
    b2.place(x=200,y=300)
    
    b3=Button(t,text='Last',command=lastdata,font='tahoma 15 bold',bg='lightpink')
    b3.place(x=300,y=300)
    
    b4=Button(t,text='Previous',command=prevdata,font='tahoma 15 bold',bg='khaki')
    b4.place(x=400,y=300)
    t.config(bg='#a59694')
    b4=Button(t,text='Close',font='tahoma 15 bold',bg='gray78')
    b4.place(x=250,y=400)
    
    filldata()
    t.mainloop()