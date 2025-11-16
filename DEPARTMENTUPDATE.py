#update department data
import tkinter
from tkinter import*
import pymysql
from tkinter import messagebox 
from tkinter import ttk
def showdepartmentupdate():
    

    t=tkinter.Tk()
    t.geometry('800x800')
    
    # 02/09/2025
    def finddata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='eps')
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
        e4.insert(0,data[2])
        db.close()
        
    #03/09/2025    
    def updatedata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='eps')
        cur=db.cursor()
        xa=int(e1.get())
        xb=e2.get()
        xc=e3.get()
        xd=e4.get()
        sql="update department set dname='%s',hod='%s',daysinweek='%s' where deptid=%d"%(xb,xc,xd,xa)
        cur.execute(sql)
        db.commit()
        db.close()
        messagebox.showinfo('hi','updated')
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        messagebox.showinfo('Hi','Datasaved')
    def close():
        t.destroy()
        
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
    g=Label(t,text='DEPARTMENT UPDATEDATA SHEET',font='elephant 25 bold',fg='black',bg='GRAY65')
    g.place(x=30,y=10)
    
    
    
    
    a=Label(t,text='Dept ID',font='arial 15 bold',bg='GRAY73')
    a.place(x=50,y=100)
    e1=ttk.Combobox(t,font='arial 15 bold')
    filldata()
    e1.place(x=400,y=100)
    
    bt=Button(t,text='Find',command=finddata,font='arial 14 bold',bg='khaki')
    bt.place(x=250,y=150)
    
    b=Label(t,text='DName',font='arial 15 bold',bg='GRAY73')
    b.place(x=50,y=200)
    e2=Entry(t,width=20,font='arial 15 bold')
    e2.place(x=400,y=200)
    c=Label(t,text='HOD',font='arial 15 bold',bg='GRAY73')
    c.place(x=50,y=250)
    e3=Entry(t,width=20,font='arial 15 bold')
    e3.place(x=400,y=250)
    d=Label(t,text='Days in Week',font='arial 15 bold',bg='GRAY73')
    d.place(x=50,y=300)
    e4=Entry(t,width=20,font='arial 15 bold')
    e4.place(x=400,y=300)
    
    bt2=Button(t,text='Close',command=close,font='arial 16 bold',bg='red')
    bt2.place(x=500,y=400)
    b3=Button(t,text='Update',command=updatedata,font='arial 16 bold',bg='skyblue')
    b3.place(x=50,y=400)
    t.config(bg='gray73')
    t.mainloop()