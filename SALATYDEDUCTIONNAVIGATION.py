#1st,2nd,previos,last salarydeduction data 
import tkinter
import pymysql
from tkinter import*
import pymysql 
xa=[]
xb=[]
xc=[]
xd=[]
i=0
def showsalarydeductionnavigation():
    from tkinter import messagebox
    
    t=tkinter.Tk() 
    t.geometry('800x800')
    
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='eps')
        cur=db.cursor()
        sql="select * from salarydeduction"
        cur.execute(sql)
        data=cur.fetchall()
        global xa
        global xb
        global xc
        global xd
        for res in data:
            xa.append(res[0])
            xb.append(res[1])
            xc.append(res[2])
            xd.append(res[3])
        db.close()
        
    def firstdata():
        global i,xa,xb,xc,xd
        i=0 
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        e1.insert(0,xa[i])
        e2.insert(0,xb[i])
        e3.insert(0,xc[i])
        e4.insert(0,xd[i])
        
    def seconddata():
        global i,xa,xb,xc,xd
        i=i+1       
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        e1.insert(0,xa[i])
        e2.insert(0,xb[i])
        e3.insert(0,xc[i])
        e4.insert(0,xd[i])
        
    def predata():
        global i,xa,xb,xc,xd
        i=i-1
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        e1.insert(0,xa[i])
        e2.insert(0,xb[i])
        e3.insert(0,xc[i])
        e4.insert(0,xd[i])
    
    def lastdata():
        global i,xa,xb,xc,xd
        i=len(xa)-1
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        e1.insert(0,xa[i])
        e2.insert(0,xb[i])
        e3.insert(0,xc[i])
        e4.insert(0,xd[i])
    g=Label(t,text='SALARYDEDUCTION NAVIGATOR SHEET',font='elephant 21 bold',fg='black',bg='PALETURQUOISE4')
    g.place(x=50,y=10)
        
    a=Label(t,text='empid',font='algerian 15 bold',bg='PALETURQUOISE3')
    a.place(x=50,y=100)
    b=Label(t,text='deptid',font='algerian 15 bold',bg='PALETURQUOISE3')
    b.place(x=50,y=150)
    c=Label(t,text='month',font='algerian 15 bold',bg='PALETURQUOISE3')
    c.place(x=50,y=200)
    d=Label(t,text='deduction',font='algerian 15 bold',bg='PALETURQUOISE3')
    d.place(x=50,y=250)
    e1=Entry(t,width=20)
    e1.place(x=450,y=100)
    e2=Entry(t,width=20) 
    e2.place(x=450,y=150)
    e3=Entry(t,width=20)
    e3.place(x=450,y=200)
    e4=Entry(t,width=20)
    e4.place(x=450,y=250)
    bt1=Button(t,text='first',command=firstdata,font='algerian 13 bold',bg='gray56')
    bt1.place(x=50,y=350)
    bt2=Button(t,text='next',command=seconddata,font='algerian 13 bold',bg='gray54')
    bt2.place(x=150,y=350)
    bt3=Button(t,text='last',command=lastdata,font='algerian 13 bold',bg='gray56')
    bt3.place(x=250,y=350)
    bt4=Button(t,text='previos',command=predata,font='algerian 13 bold',bg='gray54')
    bt4.place(x=350,y=350)
    filldata()
    t.config(bg='PALETURQUOISE3')
    bt=Button(t,text='Close',font='algerian 11 bold',bg='gray54')
    bt.place(x=600,y=400)
    t.mainloop()