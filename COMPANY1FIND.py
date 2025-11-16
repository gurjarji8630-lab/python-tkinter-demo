# COMPANY1 FIND TABLE
import tkinter
from tkinter import *
from tkinter import messagebox
#from tkinter import PhotoImage

from tkinter import ttk
import pymysql
def showcompany1find():
    t=tkinter.Tk()
    t.geometry('800x800')
   # img=PhotoImage(file="C:/Users/LENOVO/OneDrive/Pictures/Screenshots/Screenshot (5397).png")
   # pic=Label(t,image=img)
   # pic.place(x=650,y=150)
    def finddata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='eps')
        cur=db.cursor()
        xa=int(e1.get())
        sql="select name,address,city,phoneno,email,regno from company1 where comid=%d"%(xa)
        cur.execute(sql)
        data=cur.fetchone()
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        e5.delete(0,100)
        e6.delete(0,100)
        e7.delete(0,100)
        
        e2.insert(0,data[0])
        e3.insert(0,data[1])
        e4.insert(0,data[2])
        e5.insert(0,data[3])
        e6.insert(0,data[4])
        e7.insert(0,str(data[5]))
        
        db.close()
    
        
    def filldata():
        lt=[]
        db=pymysql.connect(host='localhost',user='root',password='root',database='eps')
        cur=db.cursor()
        sql="select Comid from company1" 
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            lt.append(res[0])
        e1['value']=lt
        db.close()    
        
    def close():
        t.destroy()
    g=Label(t,text='COMPANY FINDDATA SHEET',font='elephant 25 bold',fg='black',bg='antiquewhite3')
    g.place(x=110,y=10)
        
    a=Label(t,text='Comp ID',font='ariel 15 bold',bg='#D6CBBF')
    a.place(x=50,y=100)
    e1=ttk.Combobox(t)
    filldata()
    e1.place(x=450,y=100)
    
    b1=Button(t,text='Find',font='ariel 11 bold',command=finddata,bg='gray78')
    b1.place(x=250,y=150)
    
    b=Label(t,text='Name',font='ariel 13 bold',bg='#D6CBBF')
    b.place(x=50,y=200)
    e2=Entry(t,width=30)
    e2.place(x=450,y=200)
    
    d=Label(t,text='Address',font='ariel 13 bold',bg='#D6CBBF')
    d.place(x=50,y=250)
    e3=Entry(t,width=30)
    e3.place(x=450,y=250)
    
    e=Label(t,text='City',font='ariel 13 bold',bg='#D6CBBF')
    e.place(x=50,y=300)
    e4=Entry(t,width=30)
    e4.place(x=450,y=300)
    
    f=Label(t,text='Phone No',font='ariel 13 bold',bg='#D6CBBF')
    f.place(x=50,y=350)
    e5=Entry(t,width=30)
    e5.place(x=450,y=350)
    
    g=Label(t,text='Email ID',font='ariel 13 bold',bg='#D6CBBF')
    g.place(x=50,y=400)
    e6=Entry(t,width=30)
    e6.place(x=450,y=400)
    
    h=Label(t,text='Regno',font='ariel 13 bold',bg='#D6CBBF')
    h.place(x=50,y=450)
    e7=Entry(t,width=30)
    e7.place(x=450,y=450)
    
    b2=Button(t,text='Close', font='ariel 11 bold',command=close,bg='gray67')
    b2.place(x=250,y=500)
    t.config(bg='#D6CBBF')
    
    t.mainloop()