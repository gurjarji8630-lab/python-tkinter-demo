#Holidaydata_Delete_Screen
import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
def showholidaydatadelete():
    import pymysql
    t=tkinter.Tk()
    t.geometry('800x800')
    
    def deletedata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='eps')
        cur=db.cursor()
        xa=int(e1.get())
        sql="delete from holidaydata where empid=%d"%(xa)
        cur.execute(sql)
        db.commit()
        db.close()
        messagebox.showinfo('Hi','Deleted')
        e1.delete(0,100)
        
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
    g=Label(t,text='HOLIDAY DELETE SHEET',font='elephant 25 bold',fg='black',bg='PINK4')
    g.place(x=120,y=10)
    
        
    a=Label(t,text='Employee ID',font='ALGERIAN 15 bold',bg='bisque3')
    a.place(x=50,y=100)
    e1=ttk.Combobox(t)
    filldata()
    e1.place(x=450,y=100)
    
    d=Button(t,text='Delete',command=deletedata,font='ALGERIAN 13 bold',bg='GRAY55')
    d.place(x=300,y=200)
    t.config(bg='bisque3')
    
    t.mainloop()