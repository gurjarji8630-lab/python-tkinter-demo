#HOD_Find_Screen
import tkinter
from tkinter import *
from tkinter import messagebox 
from tkinter import ttk
def showhodfind():
    
    import pymysql
    t=tkinter.Tk()
    t.geometry('800x800')
    
    
    def finddata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='eps')
        cur=db.cursor()
        xa=int(e1.get())
        sql="select deptid,hname,empid from hod where hodid=%d"%(xa)
        cur.execute(sql)
        data=cur.fetchone()
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        e2.insert(0,data[0])
        e3.insert(0,str(data[1]))
        e4.insert(0,data[2])
        
        db.close()
        
    def filldata():
        lt=[]
        db=pymysql.connect(host='localhost',user='root',password='root',database='eps')
        cur=db.cursor()
        sql="select hodid from hod" 
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            lt.append(res[0])
        e1['value']=lt
        db.close()  
        
    def filldataempid():
         lt=[]
         db=pymysql.connect(host='localhost',user='root',password='root',database='eps')
         cur=db.cursor()
         sql="select empid from hod" 
         cur.execute(sql)
         data=cur.fetchall()
         for res in data:
             lt.append(res[0])
         e4['value']=lt
         db.close()  
     
            
    def close():
        t.destroy()
  
    g=Label(t,text='HOD FINDDATA SHEET',font='ELEPHANT 35 bold',fg='WHITE',bg='#BA6E8F')
    g.place(x=160,y=10)
    
    a=Label(t,text='HOD ID',font='arial 30 bold',bg='rosybrown3')
    a.place(x=50,y=150)
    e1=ttk.Combobox(t,font='ariel 25 bold')
    filldata()
    e1.place(x=600,y=150)
    b1=Button(t,text='Find',command=finddata,font='ariel 20 bold',bg='#98A77C',fg='white')
    b1.place(x=400,y=200)
    
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
    e4=ttk.Combobox(t,font='ariel 25 bold')
    filldataempid()
    e4.place(x=600,y=450)
    
    
    k=Button(t,text='Close',command=close,font='ariel 25 bold',bg='#98A77C',fg='white')
    k.place(x=400,y=550)
    t.config(bg='rosybrown3')
    
    t.mainloop()