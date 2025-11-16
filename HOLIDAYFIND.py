#Holidaydata_Find_Screen
import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
def showholidaydatafind():
    import pymysql
    t=tkinter.Tk()
    t.geometry('800x800')
    
    def finddata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='eps')
        cur=db.cursor()
        xa=int(e1.get())
        sql="select deptid,leaveid,leavetype,noofleaves from holidaydata where empid=%d"%(xa)
        cur.execute(sql)
        data=cur.fetchone()
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        e5.delete(0,100)
        e2.insert(0,str(data[0]))
        e3.insert(0,str(data[1]))
        e4.insert(0,data[2])
        e5.insert(0,str(data[3]))
        
        
        db.close()
        
    def filldata():
        lt=[]
        db=pymysql.connect(host='localhost',user='root',password='root',database='eps')
        cur=db.cursor()
        sql="select empid from holidaydata" 
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            lt.append(res[0])
        e1['value']=lt
        db.close()    
        
        
        
    def close():
        t.destroy()
    g=Label(t,text='HOLIDAY FIND SHEET',font='elephant 25 bold',fg='black',bg='PINK4')
    g.place(x=150,y=10)
        
    a=Label(t,text='Employee ID',font='ALGERIAN 15 bold',bg='bisque3')
    a.place(x=50,y=100)
    e1=ttk.Combobox(t)
    filldata()
    e1.place(x=450,y=100)
    
    b1=Button(t,text='Find',command=finddata,font='ALGERIAN 15 bold',bg='gray55')
    b1.place(x=300,y=150)
    
    b=Label(t,text='Department ID',font='ALGERIAN 15 bold',bg='bisque3')
    b.place(x=50,y=200)
    e2=Entry(t,width=30)
    e2.place(x=450,y=200)
    
    d=Label(t,text='Leave ID',font='ALGERIAN 15 bold',bg='bisque3')
    d.place(x=50,y=250)
    e3=Entry(t,width=30)
    e3.place(x=450,y=250)
    
    e=Label(t,text='Leave Type',font='ALGERIAN 15 bold',bg='bisque3')
    e.place(x=50,y=300)
    e4=Entry(t,width=30)
    e4.place(x=450,y=300)
    
    e=Label(t,text='No of Leaves',font='ALGERIAN 15 bold',bg='bisque3')
    e.place(x=50,y=350)
    e5=Entry(t,width=30)
    e5.place(x=450,y=350)
    
    
    b2=Button(t,text='Close',command=close,font='ALGERIAN 15 bold',bg='gray67')
    b2.place(x=300,y=400)
    t.config(bg='bisque3')
    
    t.mainloop()