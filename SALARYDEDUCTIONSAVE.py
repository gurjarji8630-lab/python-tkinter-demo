#salarydeductions save data
import tkinter
from tkinter import*
import pymysql 
from tkinter import messagebox
from tkinter import ttk
def showsalarydeductionsave():
    t=tkinter.Tk() 
    t.geometry('800x800')
    
    def savedata():
        if len(e1.get())==0 or len(e2.get())==0 or len(e3.get())==0 or len(e4.get())==0:
            messagebox.showinfo('hi','pls fill all data')
        else:
            
            db=pymysql.connect(host='localhost',user='root',password='root',database='eps')
            cur=db.cursor()
            xa=int(e1.get())
            xb=int(e2.get())
            xc=e3.get()
            xd=int(e4.get())
            sql="insert into salarydeduction values(%d,%d,'%s',%d)"%(xa,xb,xc,xd)
            cur.execute(sql)
            db.commit()
            db.close()
            e1.delete(0,100)
            e2.delete(0,100)
            e3.delete(0,100)
            e4.delete(0,100)
            messagebox.showinfo('Hi','Datasaved') 
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
    # 08/09/2025     

    def deductions():
        db=pymysql.connect(host='localhost',user='root',password='root',database='eps')
        cur=db.cursor()
        xa=int(e1.get())
        sql="select salarydata.permonthsalary-(salarydata.permonthsalary/30*holidaydata.noofleaves) from holidaydata join salarydata where holidaydata.empid=salarydata.empid and salarydata.empid=%d;"%(xa);
        cur.execute(sql)
        data=cur.fetchone()
        e4.delete(0,100)
        e4.insert(0,int(data[0]))
        
    def close():
        
        t.destroy()
    g=Label(t,text='SALARYDEDUCTION SAVE SHEET',font='elephant 23 bold',fg='black',bg='PALETURQUOISE4')
    g.place(x=70,y=10)
    a=Label(t,text='Emp ID',font='algerian 15 bold',bg='PALETURQUOISE3')
    a.place(x=50,y=100)
    b=Label(t,text='Dept ID',font='algerian 15 bold',bg='PALETURQUOISE3')
    b.place(x=50,y=150)
    c=Label(t,text='Month',font='algerian 15 bold',bg='PALETURQUOISE3')
    c.place(x=50,y=200)
    d=Label(t,text='Deductions',font='algerian 15 bold',bg='PALETURQUOISE3')
    d.place(x=50,y=250)
    e1=ttk.Combobox(t)
    filldata()
    e1.place(x=450,y=100)
    e2=ttk.Combobox(t)
    filldata1()
    e2.place(x=450,y=150)
    e3=Entry(t,width=20,font='algerian 15 bold')
    e3.place(x=450,y=200)
    e4=Entry(t,width=20,font='algerian 15 bold')
    e4.place(x=450,y=250)
    bt=Button(t,text='Save',command=savedata,font='algerian 13 bold',bg='#D6CBBF')
    bt.place(x=100,y=300)
    bt=Button(t,text='cancel',command=close,font='algerian 13 bold',bg='#D6CBBF')
    bt.place(x=450,y=300)
    dt = Button(t, text='CALCULATE', font=('Arial', 15), fg='white', bg='limegreen', command=deductions)
    dt.place(x=550, y=400)
    
    t.config(bg='PALETURQUOISE3')
    t.mainloop()