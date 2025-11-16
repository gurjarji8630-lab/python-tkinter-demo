# salary deduction delete data
import tkinter
from tkinter import*
import pymysql
from tkinter import messagebox
from tkinter import ttk
def showsalarydeductiondelete():

    t=tkinter.Tk()
    t.geometry('800x800') 
    def deletedata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='eps')
        cur=db.cursor()
        xa=int(e1.get())
        
        sql="delete from salarydeduction where empid=%d"%(xa)
    
        cur.execute(sql)
        db.commit()
        db.close()
        messagebox.showinfo('Hi','deleted')
        e1.delete(0,100)
    def filldata():
        lt=[]
        db=pymysql.connect(host='localhost',user='root',password='root',database='eps')
        cur=db.cursor()
        sql="select empid from salarydeduction" 
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            lt.append(res[0])
        e1['value']=lt
        db.close()  
    g=Label(t,text='SALARYDEDUCTION DELETE SHEET',font='elephant 23 bold',fg='black',bg='PALETURQUOISE4')
    g.place(x=60,y=10)
    a=Label(t,text='empid',font='algerian 15 bold',bg='PALETURQUOISE3')
    a.place(x=50,y=100)
    e1=ttk.Combobox(t)
    filldata()
    e1.place(x=400,y=100)
    bt=Button(t,text='Delete',command=deletedata,font='algerian 12 bold',bg='gray56')
    bt.place(x=250,y=150)
    t.config(bg='PALETURQUOISE3')
    
    t.mainloop()