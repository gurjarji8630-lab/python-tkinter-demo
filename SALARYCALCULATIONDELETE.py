#Salarycalculation_Delete_Screen
import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
def showsalarycalculationdelete():
    import pymysql
    t=tkinter.Tk()
    t.geometry('800x800')
    
    def deletedata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='eps')
        cur=db.cursor()
        xa=int(e1.get())
        sql="delete from salarycalculation where empid=%d"%(xa)
        cur.execute(sql)
        db.commit()
        db.close()
        messagebox.showinfo('Hi','Deleted')
        e1.delete(0,100)
        
    def filldata():
        lt=[]
        db=pymysql.connect(host='localhost',user='root',password='root',database='eps')
        cur=db.cursor()      
        sql="select empid from salarycalculation"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            lt.append(res[0])
        e1['value']=lt
        db.close()  
    g=Label(t,text='SALARYCALCULATION DELETE SHEET',font='elephant 23 bold',fg='black',bg='SNOW4')
    g.place(x=20,y=10)
        
    a=Label(t,text='Employee ID',font='tahoma 16 bold',bg='SNOW3')
    a.place(x=50,y=100)
    e1=ttk.Combobox(t,font='tahoma 13 bold')
    filldata()
    e1.place(x=400,y=100)
    
    d=Button(t,text='Delete',command=deletedata,font='tahoma 13 bold',bg='thistle')
    d.place(x=100,y=200)
    t.config(bg='snow3')
    d=Button(t,text='Close',command=deletedata,font='tahoma 13 bold',bg='skyblue')
    d.place(x=400,y=200)
    t.config(bg='snow3')
    
    t.mainloop()