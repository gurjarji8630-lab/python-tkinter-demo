#dept find data
import tkinter
from tkinter import*
from tkinter import messagebox
from tkinter import ttk
import pymysql
def showdepartmentfind():

    t=tkinter.Tk()
    t.geometry('800x800')
    
    # 02/09/2025
    def finddata():
        db=pymysql.connect(host='localhost',user='root',password='root',database=
                           'eps')
        cur=db.cursor()
        xa=int(e1.get())
        
        sql="select dname,hod,daysinweek from department where deptid=%d"%(xa)
    
        cur.execute(sql)
        data=cur.fetchone()
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        
        e2.insert(0,data[0])
        e3.insert(0,data[1])
        e4.insert(0,str(data[2]))
        db.close() 
        
    def close():
        t.destroy()
        
    #03/09/2025    
    def filldata():
        lt=[]
        db=pymysql.connect(host='localhost',user='root',password='root',database='eps')
        cur=db.cursor()
        sql="select deptid from department" 
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            lt.append(res[0])
        e1['value']=lt
        db.close()  
    g=Label(t,text='DEPARTMENT FINDDATA SHEET',font='elephant 25 bold',fg='black',bg='GRAY65')
    g.place(x=60,y=10)
        
    a=Label(t,text='Deptid',font='arial 15 bold',bg='GRAY73')
    a.place(x=50,y=100)
    e1=ttk.Combobox(t)
    filldata() 
    e1.place(x=400,y=100)
        
    bt=Button(t,text='Find',command=finddata,font='arial 15 bold',bg='khaki')
    bt.place(x=250,y=150)
    b=Label(t,text='Dname',font='arial 15 bold',bg='GRAY73')
    b.place(x=50,y=200)
    e2=Entry(t,width=20,font='arial 13 bold')
    e2.place(x=400,y=200)
    c=Label(t,text='HOD',font='arial 15 bold',bg='GRAY73')
    c.place(x=50,y=250)
    e3=Entry(t,width=20,font='arial 13 bold')
    e3.place(x=400,y=250)
    d=Label(t,text='Days in Week',font='arial 15 bold',bg='GRAY73')
    d.place(x=50,y=300)
    e4=Entry(t,width=20,font='arial 13 bold') 
    e4.place(x=400,y=300)
    bt2=Button(t,text='Close',command=close,font='arial 15 bold',bg='red')
    bt2.place(x=250,y=400)
    t.config(bg='gray73')
    t.mainloop()