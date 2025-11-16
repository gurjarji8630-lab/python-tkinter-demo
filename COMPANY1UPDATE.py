 # COMPANY1 UPDATE ,FIND DATA 
import tkinter
from tkinter import*
import pymysql
from tkinter import messagebox
#from tkinter import PhotoImage
def showcompany1update():
    from tkinter import ttk
    t=tkinter.Tk() 
    t.geometry('800x800')
    #img=PhotoImage(file="C:/Users/LENOVO/OneDrive/Pictures/updatepic.png")
    #pic=Label(t,image=img)
    #pic.place(x=700,y=150)
    def finddata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='eps')
        cur=db.cursor()
        xa=int(e1.get())
        sql="select name,address,city,phoneno,email,regno from company1 where comid=%d"%(xa)
        cur.execute(sql)
        data=cur.fetchone()
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        e5.delete(0,100)
        e6.delete(0,100)
        e7.delete(0,100)
        
        e2.insert(0,data[0])
        e3.insert(0,data[1])
        e4.insert(0,data[2])
        e5.insert(0,data[3])
        e6.insert(0,data[4])
        e7.insert(0,data[5])
        
        db.close()
    
    
    def updatedata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='eps')
        cur=db.cursor()
        xa=int(e1.get())
        xb=e2.get()
        xc=e3.get()
        xd=e4.get()
        xe=e5.get()
        xf=e6.get()
        xg=e7.get()
        
        sql="update company1 set name='%s',address='%s',city='%s',phoneno='%s',email='%s',regno='%s' where comid=%d"%(xb,xc,xd,xe,xf,xg,xa)
        cur.execute(sql)
        db.commit()
        db.close()
        messagebox.showinfo('Hi','Updated')
        
    def filldata():
        lt=[]
        db=pymysql.connect(host='localhost',user='root',password='root',database='eps')
        cur=db.cursor()
        sql="select comid from company1" 
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            lt.append(res[0])
        e1['value']=lt
        db.close()    
             
    def close():
        t.destroy()
    g=Label(t,text='COMPANY UPDATE  SHEET',font='elephant 25 bold',fg='black',bg='antiquewhite3')
    g.place(x=80,y=10)
    
    a=Label(t,text='Comp ID',font='ariel 15 bold',bg='#D6CBBF')
    a.place(x=50,y=100)
    e1=ttk.Combobox(t)
    filldata()
    e1.place(x=450,y=100)
    b=Label(t,text='Name',font='ariel 15 bold',bg='#D6CBBF')
    b.place(x=50,y=150)
    e2=Entry(t,width=20)
    e2.place(x=450,y=150)
    f=Label(t,text='Address',font='ariel 15 bold',bg='#D6CBBF')
    f.place(x=50,y=200)
    e3=Entry(t,width=20)
    e3.place(x=450,y=200)
    g=Label(t,text='City',font='ariel 15 bold',bg='#D6CBBF')
    g.place(x=50,y=250)
    e4=Entry(t,width=20)
    e4.place(x=450,y=250)
    h=Label(t,text='Phoneno',font='ariel 15 bold',bg='#D6CBBF')
    h.place(x=50,y=300)
    e5=Entry(t,width=20)
    e5.place(x=450,y=300)
    j=Label(t,text='Email',font='ariel 15 bold',bg='#D6CBBF')
    j.place(x=50,y=350)
    e6=Entry(t,width=20)
    e6.place(x=450,y=350)
    l=Label(t,text='Reg No',font='ariel 15 bold',bg='#D6CBBF')
    l.place(x=50,y=400)
    e7=Entry(t,width=20)
    e7.place(x=450,y=400)
    bt=Button(t,text='Update',command=updatedata,font='ariel 10 bold',bg='gray63')
    bt.place(x=100,y=500)
    bt1=Button(t,text='Find',command=finddata,font='ariel 10 bold',bg='gray63')
    bt1.place(x=400,y=500)
    t.config(bg='#D6CBBF')
    t.mainloop()