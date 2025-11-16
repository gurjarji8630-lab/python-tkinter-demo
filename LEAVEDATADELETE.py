#Leavedata_Delete_Screen
import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
def showleavedatadelete():
    import pymysql
    t=tkinter.Tk()
    t.geometry('800x800')
    
    def deletedata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='eps')
        cur=db.cursor()
        xa=int(e1.get())
        sql="delete from leavedata where leaveid=%d"%(xa)
        cur.execute(sql)
        db.commit()
        db.close()
        messagebox.showinfo('Hi','Deleted')
        e1.delete(0,100)
        
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
    g=Label(t,text='LEAVE DATA DELETE SHEET',font='elephant 30 bold',fg='black',bg='HONEYDEW3')
    g.place(x=40,y=10)
        
    a=Label(t,text='Leave ID',font='ariel 15 bold',bg='honeydew2')
    a.place(x=50,y=100)
    e1=ttk.Combobox(t)
    filldata()
    e1.place(x=400,y=100)
    
    d=Button(t,text='Delete',command=deletedata,font='ariel 13 bold',bg='GRAY78')
    d.place(x=300,y=150)
    t.config(bg='honeydew2')
    
    t.mainloop()