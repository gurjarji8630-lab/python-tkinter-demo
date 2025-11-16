#Employee_Update_Screen
import tkinter
from tkinter import *
from tkinter import messagebox
#from tkinter import PhotoImage
from tkinter import ttk
import pymysql
def showemployeeupdate():
    
    t=tkinter.Tk()
    t.geometry('800x800')
    #img=PhotoImage(file="C:/Users/LENOVO/OneDrive/Pictures/Screenshots/Screenshot (5400).png")
    #pic=Label(t,image=img)
    #pic.place(x=650,y=100)
    
    def finddata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='eps')
        cur=db.cursor()
        xa=int(e1.get())
        sql="select ename,address,phoneno,email,deptid from employee where empid=%d"%(xa)
        cur.execute(sql)
        data=cur.fetchone()
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        e5.delete(0,100)
        e6.delete(0,100)
        e2.insert(0,data[0])
        e3.insert(0,data[1])
        e4.insert(0,data[2])
        e5.insert(0,data[3])
        e6.insert(0,str(data[4]))
        
        
        db.close()
        
    def updatedata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='eps')
        cur=db.cursor()
        xa=int(e1.get())
        xd=e7.get()
        sql="update employee set ename='%s' where empid=%d"%(xd,xa)
        cur.execute(sql)
        db.commit()
        db.close()
        e6.delete(0,100)
        messagebox.showinfo('Hi','Updated')
        
    def filldata():
        lt=[]
        db=pymysql.connect(host='localhost',user='root',password='root',database='eps')
        cur=db.cursor()
        sql="select empid from employee" 
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            lt.append(res[0])
        e1['value']=lt
        db.close()   
        
    def close():
        t.destroy()
    g=Label(t,text='EMPLOYEE UPDATEDATA SHEET',font='ELEPHANT 25 bold',fg='black',bg='alice blue')
    g.place(x=60,y=10)
        
    
    
    a=Label(t,text='Employee ID',font='ariel 12 bold',bg='lavender')
    a.place(x=50,y=100)
    e1=ttk.Combobox(t)
    filldata()
    e1.place(x=450,y=100)
    
    b1=Button(t,text='Find',command=finddata,font='ariel 15 bold',bg='khaki')
    b1.place(x=300,y=150)
    
    b=Label(t,text='Employee Name',font='ariel 12 bold',bg='lavender')
    b.place(x=50,y=200)
    e2=Entry(t,width=30)
    e2.place(x=450,y=200)
    
    d=Label(t,text='Address',font='ariel 12 bold',bg='lavender')
    d.place(x=50,y=250)
    e3=Entry(t,width=30)
    e3.place(x=450,y=250)
    
    e=Label(t,text='Phone No',font='ariel 12 bold',bg='lavender')
    e.place(x=50,y=250)
    e4=Entry(t,width=30)
    e4.place(x=450,y=250)
    
    f=Label(t,text='Email ID',font='ariel 12 bold',bg='lavender')
    f.place(x=50,y=300)
    e5=Entry(t,width=30)
    e5.place(x=450,y=300)
    
    g=Label(t,text='Department ID',font='ariel 12 bold',bg='lavender')
    g.place(x=50,y=350)
    e6=Entry(t,width=30)
    e6.place(x=450,y=350)
    
    b2=Button(t,text='Close',command=close,font='ariel 17 bold',bg='red')
    b2.place(x=450,y=450)
    
    b3=Button(t,text='Update',command=updatedata,font='ariel 17 bold',bg='skyblue')
    b3.place(x=50,y=450)
    t.config(bg='lavender')
    
    t.mainloop()