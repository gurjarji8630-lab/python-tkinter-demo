#delete data from salarydata
import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
def showsalarydatadelete():
    import pymysql
    
    t=tkinter.Tk()
    t.geometry('800x800')
    def deletedata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='eps')
        cur=db.cursor()
        xa=int(e1.get())
        sql="delete from salarydata where empid=%d"%(xa)
        cur.execute(sql)
        db.commit()
        db.close()
        messagebox.showinfo('hi','deleted')
        e1.delete(0,100)
    def filldata():
        lt=[]
        db=pymysql.connect(host='localhost',user='root',password='root',database='eps')
        cur=db.cursor()      
        sql="select empid from salarydata"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            lt.append(res[0])
        e1['value']=lt
        db.close()
    def close():
        t.destroy()
        
        
    g=Label(t,text='SALARY DATA DELETE SHEET',font='courier 35 bold',fg='black',bg='lightsteelblue')
    g.place(x=70,y=10)
    a=Label(t,text='Empid',font='ariel 16 bold',bg='lightsteelblue3')
    a.place(x=50,y=100)
    e1=ttk.Combobox(t)
    filldata()
    e1.place(x=400,y=100)
    b1=Button(t,text='Delete',command=deletedata,font='ariel 13 bold',bg='#D6CBBF')
    b1.place(x=50,y=250)
    b1=Button(t,text='Close',command=close,font='ariel 13 bold',bg='#D6CBBF')
    b1.place(x=400,y=250)
    t.config(bg='lightsteelblue3')
    t.mainloop()