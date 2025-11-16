# salarydeduction find data
import tkinter
from tkinter import*
from tkinter import messagebox
from tkinter import ttk
def showsalarydeductionfind():
    import pymysql
    
    t=tkinter.Tk()
    t.geometry('800x800')
    
    # 02/09/2025
    def finddata():
        db=pymysql.connect(host='localhost',user='root',password='root',database=
                           'eps')
        cur=db.cursor()
        xa=int(e1.get())
        
        sql="select deptid,month,deduction from salarydeduction where empid=%d"%(xa)
    
        cur.execute(sql)
        data=cur.fetchone()
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        
        e2.insert(0,data[0])
        e3.insert(0,data[1])
        e4.insert(0,str(data[2]))
        db.close() 
        
    def close():
        t.destroy()
        
    #03/09/2025    
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
    def filldata1():
        lt=[]
        db=pymysql.connect(host='localhost',user='root',password='root',database='eps')
        cur=db.cursor()
        sql="select deptid from salarydeduction" 
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            lt.append(res[0])
        e2['value']=lt
        db.close()  
    g=Label(t,text='SALARYDEDUCTION FIND SHEET',font='elephant 23 bold',fg='black',bg='PALETURQUOISE4')
    g.place(x=70,y=10)
        
    a=Label(t,text='Emp ID',font='algerian 15 bold',bg='PALETURQUOISE3') 
    a.place(x=50,y=100)
    e1=ttk.Combobox(t)
    filldata() 
    e1.place(x=450,y=100)
        
    bt=Button(t,text='Find',command=finddata,font='algerian 13 bold',bg='gray56')
    bt.place(x=250,y=150)
    b=Label(t,text='Dept ID',font='algerian 15 bold',bg='PALETURQUOISE3')
    b.place(x=50,y=200)
    e2=ttk.Combobox(t)
    filldata1()
    e2.place(x=450,y=200)
    c=Label(t,text='Month',font='algerian 15 bold',bg='PALETURQUOISE3')
    c.place(x=50,y=250)
    e3=Entry(t,width=20)
    e3.place(x=450,y=250)
    d=Label(t,text='Deduction',font='algerian 15 bold',bg='PALETURQUOISE3')
    d.place(x=50,y=300)
    e4=Entry(t,width=20) 
    e4.place(x=450,y=300)
    bt2=Button(t,text='Close',command=close,font='algerian 13 bold',bg='gray56')
    bt2.place(x=250,y=350)
    t.config(bg='PALETURQUOISE3')
    t.mainloop()