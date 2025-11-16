#last,next,previous ,first salarydata
import tkinter
from tkinter import * 
from tkinter import messagebox
xa=[]
xb=[]
xc=[]
xd=[]
xe=[]
i=0
def showsalarydatanavigator():
    import pymysql
    
    t=tkinter.Tk()
    t.geometry('800x800')
    
   
    
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='eps')
        cur=db.cursor()
        sql="select * from salarydata"
        cur.execute(sql)
        data=cur.fetchall()
        global xa
        global xb
        global xc
        global xd
        global xe
        for res in data:
            xa.append(res[0])
            xb.append(res[1])
            xc.append(res[2])
            xd.append(res[3])
            xd.append(res[4])
        db.close()
        
    def firstdata():
        global i,xa,xb,xc,xd,xe
        i=0
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        e5.delete(0,100)
        
        e1.insert(0,xa[i])
        e2.insert(0,xb[i])
        e3.insert(0,xc[i])
        e4.insert(0,xd[i])
        e5.insert(0,xd[i])
        
    def nextdata():
            global i,xa,xb,xc,xd,xe
            i=i+1
            e1.delete(0,100)
            e2.delete(0,100)
            e3.delete(0,100)
            e4.delete(0,100)
            e5.delete(0,100)
            
            e1.insert(0,xa[i])
            e2.insert(0,xb[i])
            e3.insert(0,xc[i])
            e4.insert(0,xd[i])
            e5.insert(0,xd[i])
            
    def prevdata():
            global i,xa,xb,xc,xd,xe
            i=i-1
            e1.delete(0,100)
            e2.delete(0,100)
            e3.delete(0,100)
            e4.delete(0,100)
            e5.delete(0,100)
            
            e1.insert(0,xa[i])
            e2.insert(0,xb[i])
            e3.insert(0,xc[i])
            e4.insert(0,xd[i])
            e5.insert(0,xd[i])
        
    def lastdata():
            global i,xa,xb,xc,xd,xe
            i=len(xa)-1
            e1.delete(0,100)
            e2.delete(0,100)
            e3.delete(0,100)
            e4.delete(0,100)
            e5.delete(0,100)
            
            e1.insert(0,xa[i])
            e2.insert(0,xb[i])
            e3.insert(0,xc[i])
            e4.insert(0,xd[i])
            e5.insert(0,xd[i])
    def close():
        t.destroy
    g=Label(t,text='SALARYDATA NAVIGATOR SHEET',font='courier 25 bold',fg='black',bg='lightsteelblue')
    g.place(x=70,y=10)
        
    a=Label(t,text='Empid',font='ariel 16 bold',bg='lightsteelblue3')
    a.place(x=50,y=100)
    e1=Entry(t,width=20)
    e1.place(x=400,y=100)
    
    b=Label(t,text='Deptid',font='ariel 16 bold',bg='lightsteelblue3')
    b.place(x=50,y=150)
    e2=Entry(t,width=20)
    e2.place(x=400,y=150)
    
    d=Label(t,text='CTC',font='ariel 16 bold',bg='lightsteelblue3')
    d.place(x=50,y=200)
    e3=Entry(t,width=20)
    e3.place(x=400,y=200)
    
    e=Label(t,text='PF',font='ariel 16 bold',bg='lightsteelblue3')
    e.place(x=50,y=250)
    e4=Entry(t,width=20)
    e4.place(x=400,y=250)
    
    e=Label(t,text='Permonthsalary',font='ariel 16 bold',bg='lightsteelblue3')
    e.place(x=50,y=300)
    e5=Entry(t,width=20)
    e5.place(x=400,y=300)
    
    b1=Button(t,text='First',command=firstdata,font='ariel 13 bold',bg='#D6CBBF')
    b1.place(x=100,y=400)
    
    b2=Button(t,text='Next',command=nextdata,font='ariel 13 bold',bg='#D6CBBF')
    b2.place(x=180,y=400)
    
    b3=Button(t,text='Last',command=lastdata,font='ariel 13 bold',bg='#D6CBBF')
    b3.place(x=260,y=400)
    
    b4=Button(t,text='Previous',command=prevdata,font='ariel 13 bold',bg='#D6CBBF')
    b4.place(x=340,y=400)
    b5=Button(t,text='Close',command=close,font='ariel 13 bold',bg='#D6CBBF')
    b5.place(x=340,y=500)
    
    filldata()
    t.config(bg='lightsteelblue3')
    t.mainloop()