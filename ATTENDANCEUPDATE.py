#update fill and find data attendence
import tkinter
from tkinter import *
import pymysql
from tkinter import messagebox
from tkinter import ttk
def showattendanceupdate():
    
    t=tkinter.Tk()
    t.geometry('800x800')
    
    def finddata():
        db=pymysql.connect(host='localhost',user='root',password='root',database=
                           'eps')
        cur=db.cursor()
        xa=int(e1.get())
        sql="select month,dateofattendance from attendance where empid=%d"%(xa)
        cur.execute(sql)
        data=cur.fetchone()
        e2.delete(0,100)
        e3.delete(0,100)
        
        e2.insert(0,data[0])
        e3.insert(0,data[1])
       
        db.close()
        
    def updatedata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='eps')
        cur=db.cursor()
        xa=int(e1.get())
        xe=e2.get()
        sql="update attendance set month='%s' where empid=%d"%(xe,xa)
        cur.execute(sql)
        db.commit()
        db.close()
        messagebox.showinfo('hi','updated')
        e4.delete(0,100)
        messagebox.showinfo('hi','data saved')
        
    def filldata():
        lt=[]
        db=pymysql.connect(host='localhost',user='root',password='root',database='eps')
        cur=db.cursor()
        sql="select empid from attendance"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            lt.append(res[0])
        e1['values']=lt
        
    def close():
        t.destroy()
    g=Label(t,text='ATTENDANCE UPDATE SHEET',font='algerian 45 bold',fg='white',bg='rosybrown4')
    g.place(x=200,y=10)
        
    a=Label(t,text='Emp ID',font='tahoma 30 bold',bg='#a59694')
    a.place(x=50,y=150) 
    e1=ttk.Combobox(t,font='tahoma 15 bold')
    filldata()
    e1.place(x=700,y=150)
    
    bt=Button(t,text='Find',command=finddata,font='tahoma 20 bold',bg='KHAKI')
    bt.place(x=300,y=250)
    
    b=Label(t,text='Month',font='tahoma 25 bold',bg='#a59694')
    b.place(x=50,y=300)
    e2=Entry(t,width=20,font='tahoma 15 bold')
    e2.place(x=700,y=300)
    
    d=Label(t,text='Date of Attendance',font='tahoma 25 bold',bg='#a59694')
    d.place(x=50,y=400)
    e3=Entry(t,width=20,font='tahoma 15 bold')
    e3.place(x=700,y=400)
    
    bt2=Button(t,text='Close',command=close,font='tahoma 25 bold',bg='RED')
    bt2.place(x=700,y=600)
    
    bt3=Button(t,text='Update',command=updatedata,font='tahoma 25 bold',bg='LIGHTGREEN')
    bt3.place(x=100,y=600)
    t.config(bg='#a59694')
         
    t.mainloop()