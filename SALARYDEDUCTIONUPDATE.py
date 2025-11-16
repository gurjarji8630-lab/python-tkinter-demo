#update fill and find salarydeduction data
import tkinter
from tkinter import*
import pymysql
from tkinter import messagebox 
from tkinter import ttk
def showsalarydeductionupdate():

    t=tkinter.Tk()
    t.geometry('800x800')
    
    # 02/09/2025
    def finddata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='eps')
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
        e4.insert(0,data[2])
        db.close()
        
    #03/09/2025    
    def updatedata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='eps')
        cur=db.cursor()
        xa=int(e1.get())
        xb=e2.get()
        xc=e3.get()
        xd=int(e4.get())
        sql="update salarydeduction set deptid ='%s',month='%s',deduction=%d where empid=%d"%(xb,xc,xd,xa)
        cur.execute(sql)
        db.commit()
        db.close()
        messagebox.showinfo('hi','updated')
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        messagebox.showinfo('Hi','Datasaved')
    def close():
        t.destroy()
        
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
    
    
    g=Label(t,text='SALARYDEDUCTION UPDATE SHEET',font='elephant 23 bold',fg='black',bg='PALETURQUOISE4')
    g.place(x=60,y=10)
        
    a=Label(t,text='Empid',font='algerian 15 bold',bg='PALETURQUOISE3') 
    a.place(x=50,y=100)
    e1=ttk.Combobox(t)
    filldata() 
    e1.place(x=450,y=100)
        
    bt=Button(t,text='Find',command=finddata,font='algerian 13 bold',bg='gray56')
    bt.place(x=250,y=150)
    b=Label(t,text='deptid',font='algerian 15 bold',bg='PALETURQUOISE3')
    b.place(x=50,y=200)
    e2=Entry(t,width=20)
    e2.place(x=450,y=200)
    c=Label(t,text='No Of Days',font='algerian 15 bold',bg='PALETURQUOISE3')
    c.place(x=50,y=250)
    e3=Entry(t,width=20)
    e3.place(x=450,y=250)
    d=Label(t,text='Final Salary',font='algerian 15 bold',bg='PALETURQUOISE3')
    d.place(x=50,y=300)
    e4=Entry(t,width=20) 
    e4.place(x=450,y=300)
    bt2=Button(t,text='close',command=close,font='algerian 13 bold',bg='gray56')
    bt2.place(x=500,y=400)
    t.config(bg='PALETURQUOISE3')
    
    b3=Button(t,text='Update',command=updatedata,font='algerian 13 bold',bg='gray56')
    b3.place(x=100,y=400)
    t.mainloop()