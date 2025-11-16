#Holidaydata_Save_Screen
import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pymysql
def showholidaydatasave():
    t=tkinter.Tk()
    t.geometry('800x800')
    
    def savedata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='eps')
        cur=db.cursor()
        xa=int(e1.get())
        xb=int(e2.get())
        xc=int(e3.get())
        xd=e4.get()
        xe=int(e5.get())
        sql="insert into holidaydata values(%d,%d,%d,'%s',%d)"%(xa,xb,xc,xd,xe)
        cur.execute(sql)
        db.commit()
        db.close()
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        e5.delete(0,100)
        messagebox.showinfo('Hi','Data Saved')
    def filldata():
           
           lt=[]
           db=pymysql.connect(host='localhost',user='root',password='root',database='eps')
           cur=db.cursor()
           sql="select empid from holidaydata"
           cur.execute(sql)
           data=cur.fetchall()
           for res in data:
               lt.append(res[0])
           e1['values']=lt
                
           db.close()
    g=Label(t,text='HOLIDAY SAVE SHEET',font='elephant 25 bold',fg='black',bg='PINK4')
    g.place(x=150,y=10)
    
    a=Label(t,text='Employee ID',font='ALGERIAN 15 bold',bg='bisque3')
    a.place(x=50,y=100)
    e1=ttk.Combobox(t)
    filldata()
    e1.place(x=400,y=100)
    
    b=Label(t,text='Department ID',font='ALGERIAN 15 bold',bg='bisque3')
    b.place(x=50,y=150)
    e2=Entry(t,width=30)
    e2.place(x=400,y=150)
    
    d=Label(t,text='Leave ID',font='ALGERIAN 15 bold',bg='bisque3')
    d.place(x=50,y=200)
    e3=Entry(t,width=30)
    e3.place(x=400,y=200)
    
    e=Label(t,text='Leave Type',font='ALGERIAN 15 bold',bg='bisque3')
    e.place(x=50,y=250)
    e4=Entry(t,width=30)
    e4.place(x=400,y=250)
    
    e=Label(t,text='No of Leaves',font='ALGERIAN 15 bold',bg='bisque3')
    e.place(x=50,y=300)
    e5=Entry(t,width=30)
    e5.place(x=400,y=300)
    
    k=Button(t,text='Save',command=savedata,font='ALGERIAN 13 bold',bg='PINK4')
    k.place(x=100,y=400)
    t.config(bg='bisque3')
    k=Button(t,text='Close',command=savedata,font='ALGERIAN 13 bold',bg='PINK4')
    k.place(x=400,y=400)
    
    t.mainloop()