#Leavedata_Find_Screen
import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
def showleavedatafind():
    import pymysql
    t=tkinter.Tk()
    t.geometry('800x800')
    
    def finddata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='eps')
        cur=db.cursor()
        xa=int(e1.get())
        sql="select leaveid,leavetype,noofdays,paid from leavedata where leaveid=%d"%(xa)
        cur.execute(sql)
        data=cur.fetchone()
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        e2.insert(0,str(data[0]))
        e3.insert(0,data[1])
        e4.insert(0,str(data[2]))
        
        db.close()
        
    def filldata():
        lt=[]
        db=pymysql.connect(host='localhost',user='root',password='root',database='eps')
        cur=db.cursor()
        sql="select leaveid from leavedata" 
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            lt.append(res[0])
        e1['value']=lt
        db.close()    
        
    def close():
        t.destroy()
    g=Label(t,text='LEAVE DATA FIND SHEET',font='elephant 30 bold',fg='black',bg='HONEYDEW3')
    g.place(x=70,y=10)
        
    a=Label(t,text='Leave ID',font='ariel 15 bold',bg='honeydew2')
    a.place(x=50,y=100)
    e1=ttk.Combobox(t)
    filldata()
    e1.place(x=400,y=100)
    
    b1=Button(t,text='Find',command=finddata,font='ariel 13 bold',bg='GRAY78')
    b1.place(x=250,y=150)
    
    b=Label(t,text='Leave Type',font='ariel 15 bold',bg='honeydew2')
    b.place(x=50,y=200)
    e2=Entry(t,width=30)
    e2.place(x=400,y=200)
    
    d=Label(t,text='No. of Days',font='ariel 15 bold',bg='honeydew2')
    d.place(x=50,y=250)
    e3=Entry(t,width=30)
    e3.place(x=400,y=250)
    
    e=Label(t,text='Paid',font='ariel 15 bold',bg='honeydew2')
    e.place(x=50,y=300)
    e4=Entry(t,width=30)
    e4.place(x=400,y=300)
    
    
    b2=Button(t,text='Close',command=close,font='ariel 13 bold',bg='GRAY78')
    b2.place(x=250,y=370)
    t.config(bg='honeydew2')
    
    t.mainloop()