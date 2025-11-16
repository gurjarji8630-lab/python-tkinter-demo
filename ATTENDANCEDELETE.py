#delete data from attendence table
import tkinter
from tkinter import *
from tkinter import messagebox
import pymysql
def showattendancedelete():
    from tkinter import ttk
    

    t=tkinter.Tk()
    t.geometry('800x800')
    
    def deletedata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='eps')
        cur=db.cursor()
        xa=int(e1.get())
        sql="delete from attendance where empid=%d"%(xa)
        cur.execute(sql)
        db.commit()
        db.close()
        messagebox.showinfo('hi','deleted')
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
        
           
    g=Label(t,text='ATTENDANCE DELETE SHEET',font='elephant 25 bold',fg='black',bg='ivory3')
    g.place(x=80,y=10)
        
    a=Label(t,text='Empid',font='tahoma 15 bold',bg='#a59694')
    a.place(x=50,y=100)
    e1=ttk.Combobox(t)
    filldata()
    e1.place(x=400,y=100)
    
    b1=Button(t,text='Delete',command=deletedata,font='tahoma 13 bold',bg='GRAY67')
    b1.place(x=250,y=250)
    t.config(bg='azure3')
    t.config(bg='#a59694')
    
    t.mainloop()