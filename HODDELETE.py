#HOD_Delete_Screen
import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
def showhoddelete():
    import pymysql
    t=tkinter.Tk()
    t.geometry('800x800')
    
    def deletedata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='eps')
        cur=db.cursor()
        xa=int(e1.get())
        sql="delete from hod where hodid=%d"%(xa)
        cur.execute(sql)
        db.commit()
        db.close()
        messagebox.showinfo('Hi','Deleted')
        e1.delete(0,100)
        
    def filldata():
        lt=[]
        db=pymysql.connect(host='localhost',user='root',password='root',database='eps')
        cur=db.cursor()      
        sql="select hodid from hod"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            lt.append(res[0])
        e1['value']=lt
        db.close()  
        
    g=Label(t,text='HOD DELETE DATA SHEET',font='ELEPHANT 35 bold',fg='WHITE',bg='#BA6E8F')
    g.place(x=160,y=10)
     
    a=Label(t,text='HOD ID',font='arial 30 bold',bg='rosybrown3')
    a.place(x=50,y=150)
    e1=ttk.Combobox(t,font='ariel 25 bold')
    filldata()
    e1.place(x=600,y=150)
     
    
    d=Button(t,text='Delete',command=deletedata,font='ariel 25 bold',bg='#88976C',fg='white')
    d.place(x=300,y=200)
    t.config(bg='rosybrown3')
    
    t.mainloop()