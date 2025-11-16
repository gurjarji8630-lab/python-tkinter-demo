#Holidaydata_Update_Screen
import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
def showholidaydataupdate():
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
        
    def updatedata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='eps')
        cur=db.cursor()
        xa=int(e1.get())
        xd=e5.get()
        sql="update holidaydata set leavetype='%s' where empid=%d"%(xd,xa)
        cur.execute(sql)
        db.commit()
        db.close()
        e6.delete(0,100)
        messagebox.showinfo('Hi','Updated')
        
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
    g=Label(t,text='HOLIDAY UPDATE SHEET',font='elephant 25 bold',fg='black',bg='PINK4')
    g.place(x=120,y=10)
    
    
    a=Label(t,text='Leave ID',font='ALGERIAN 15 bold',bg='bisque3')
    a.place(x=50,y=100)
    e1=ttk.Combobox(t)
    filldata()
    e1.place(x=450,y=100)
    
    b1=Button(t,text='Find',command=finddata,font='ALGERIAN 13 bold',bg='GRAY56')
    b1.place(x=300,y=150)
    
    b=Label(t,text='Leave Type',font='ALGERIAN 15 bold',bg='bisque3')
    b.place(x=50,y=200)
    e2=Entry(t,width=30)
    e2.place(x=450,y=200)
    
    d=Label(t,text='No of days',font='ALGERIAN 15 bold',bg='bisque3')
    d.place(x=50,y=250)
    e3=Entry(t,width=30)
    e3.place(x=450,y=250)
    
    e=Label(t,text='Paid',font='ALGERIAN 15 bold',bg='bisque3')
    e.place(x=50,y=300)
    e4=Entry(t,width=30)
    e4.place(x=450,y=300)
    
    h=Label(t,text='New Leave Type',font='ALGERIAN 15 bold',bg='bisque3')
    h.place(x=50,y=350)
    e5=Entry(t,width=30)
    e5.place(x=450,y=350)
    
    b2=Button(t,text='Close',command=close,font='ALGERIAN 13 bold',bg='GRAY55')
    b2.place(x=500,y=450)
    
    b3=Button(t,text='Update',command=updatedata,font='ALGERIAN 13 bold',bg='GRAY45')
    b3.place(x=100,y=450)
    t.config(bg='bisque3')
    
    t.mainloop()