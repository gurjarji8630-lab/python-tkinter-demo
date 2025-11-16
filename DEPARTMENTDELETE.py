# dept delete data
import tkinter
from tkinter import*
import pymysql
from tkinter import messagebox
from tkinter import ttk
def showdepartmentdelete():

    t=tkinter.Tk()
    t.geometry('800x800') 
    def deletedata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='eps')
        cur=db.cursor()
        xa=int(e1.get())
        
        sql="delete from department where deptid=%d"%(xa)
    
        cur.execute(sql)
        db.commit()
        db.close()
        messagebox.showinfo('Hi','deleted')
        e1.delete(0,100)
    def filldata():
        lt=[]
        db=pymysql.connect(host='localhost',user='root',password='root',database='eps')
        cur=db.cursor()      
        sql="select empid from attendance"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            
            lt.append(res[0])
        e1['value']=lt
        db.close()  
    def close():
        t.destroy()
        
    g=Label(t,text='DEPARTMENT DELETEDATA SHEET',font='elephant 25 bold',fg='black',bg='GRAY65')
    g.place(x=30,y=10)
    a=Label(t,text='Deptid',font='arial 15 bold',bg='GRAY73')
    a.place(x=50,y=100)
    e1=ttk.Combobox(t,font='arial 15 bold')
    filldata()
    e1.place(x=400,y=100)
    bt=Button(t,text='Delete',command=deletedata,font='arial 13 bold',bg='skyblue')
    bt.place(x=100,y=200)
    bt=Button(t,text='CLOSE',command=close,font='arial 13 bold',bg='red')
    bt.place(x=500,y=200)
    t.config(bg='gray73')
    t.mainloop()