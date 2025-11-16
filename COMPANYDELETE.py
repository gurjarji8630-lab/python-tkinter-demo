 #company DELETE TABLE
import tkinter
from tkinter import*
import pymysql
from tkinter import messagebox

def showcompanydelete():
    from tkinter import ttk
    t=tkinter.Tk() 
    t.geometry('800x800')
    
    def deletedata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='eps')
        cur=db.cursor()
        xa=int(e1.get())
        sql="delete from company1 where comid=%d"%(xa)
        cur.execute(sql)
        db.commit()
        db.close()
        messagebox.showinfo('Hi','Deleted')
        e1.delete(0,100)
        
    def filldata():
        lt=[]
        db=pymysql.connect(host='localhost',user='root',password='root',database='eps')
        cur=db.cursor()      
        sql="select comid from company1"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            lt.append(res[0])
        e1['value']=lt
        db.close()  
    g=Label(t,text='COMPANY DELETE SHEET',font='ELEPHANT 25 bold',fg='black',bg='antiquewhite3')
    g.place(x=140,y=10)
        
    
    a=Label(t,text='Company ID',font='ariel 15 bold',bg='#D6CBBF')
    a.place(x=50,y=100)
    e1=ttk.Combobox(t)
    filldata()
    e1.place(x=450,y=100)
    bt=Button(t,text='Delete',font='ariel 15 bold',command=deletedata,bg='gray89')
    bt.place(x=300,y=200)
    t.config(bg='#D6CBBF')
    t.mainloop()