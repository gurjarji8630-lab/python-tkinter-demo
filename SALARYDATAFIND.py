#find and fill data salarydata
import tkinter
from tkinter import * 
from tkinter import messagebox
def showsalarydatafind():
    import pymysql
    from tkinter import ttk
    
    t=tkinter.Tk()
    t.geometry('800x800')
    
    def finddata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='eps')
        cur=db.cursor()
        xa=int(e1.get())
        sql="select deptid,CTC,PF,Permonthsalary from salarydata where empid=%d"%(xa)
        cur.execute(sql)
        data=cur.fetchone()
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        e5.delete(0,100)
        e2.insert(0,data[0])
        e3.insert(0,data[1])
        e4.insert(0,data[2])
        e5.insert(0,data[3])
       
        db.close()
    
    def filldata():
        lt=[]
        db=pymysql.connect(host='localhost',user='root',password='root',database='eps')
        cur=db.cursor()
        sql="select empid from salarydata"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            lt.append(res[0])
        e1['values']=lt
             
        db.close()
       
            
    g=Label(t,text='SALARY FIND DATA SHEET',font='courier 35 bold',fg='black',bg='lightsteelblue')
    g.place(x=90,y=10)
        
    a=Label(t,text='Emp ID',font='ariel 13 bold',bg='lightsteelblue3')
    a.place(x=50,y=100)
    e1=ttk.Combobox(t)
    filldata()
    e1.place(x=400,y=100)
    
    bt=Button(t,text='Find',command=finddata,font='ariel 13 bold',bg='#D6CBBF')
    bt.place(x=250,y=150)
    b=Label(t,text='Dept ID',font='ariel 13 bold',bg='lightsteelblue3')
    b.place(x=50,y=200)
    e2=Entry(t,width=20)
    e2.place(x=400,y=200)
    
    d=Label(t,text='CTC',font='ariel 13 bold',bg='lightsteelblue3')
    d.place(x=50,y=250)
    e3=Entry(t,width=20)
    e3.place(x=400,y=250)
    
    e=Label(t,text='PF',font='ariel 13 bold',bg='lightsteelblue3')
    e.place(x=50,y=300)
    e4=Entry(t,width=20)
    e4.place(x=400,y=300)
    
    e=Label(t,text='Permonth salary',font='ariel 13 bold',bg='lightsteelblue3')
    e.place(x=50,y=350)
    e5=Entry(t,width=20)
    e5.place(x=400,y=350)
    t.config(bg='lightsteelblue3')
    t.mainloop()