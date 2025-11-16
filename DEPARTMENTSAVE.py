#dept save data
import tkinter
from tkinter import*
import pymysql 
from tkinter import messagebox
from tkinter import ttk
#from tkinter import PhotoImage
def showdepartmentsave():
    t=tkinter.Tk() 
    t.geometry('800x800')
    t.geometry('800x800')
    #img=PhotoImage(file="C:/Users/LENOVO/OneDrive/Pictures/Screenshots/Screenshot (5401).png")
    #pic=Label(t,image=img)
    #pic.place(x=650,y=100)
    
    def savedata():
            if len(e1.get())==0 or len(e2.get())==0 or len(e3.get())==0 or len(e4.get())==0:
                messagebox.showinfo('hi','pls fill all data')
            else:
            
                    db=pymysql.connect(host='localhost',user='root',password='root',database='eps')
                    cur=db.cursor()
                    xa=int(e1.get())
                    xb=e2.get()
                    xc=e3.get()
                    xd=e4.get()
                    sql="insert into department values(%d,'%s','%s','%s')"%(xa,xb,xc,xd)
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
        sql="select deptid from department"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            lt.append(res[0])
        e1['values']=lt
             
        db.close()
    
        
    def close():
        t.destroy()
    g=Label(t,text='DEPARTMENT SAVEDATA SHEET',font='ALGERIAN 30 bold',fg='black',bg='GRAY65')
    g.place(x=60,y=10)
    a=Label(t,text='Deptid',font='arial 15 bold',bg='GRAY73')
    a.place(x=50,y=100)
    b=Label(t,text='DName',font='arial 15 bold',bg='GRAY73')
    b.place(x=50,y=150)
    c=Label(t,text='HOD',font='arial 15 bold',bg='GRAY73')
    c.place(x=50,y=200)
    d=Label(t,text='Daysinweek',font='arial 15 bold',bg='GRAY73')
    d.place(x=50,y=250)
    e1=ttk.Combobox(t,font='arial 15 bold')
    filldata()
    e1.place(x=400,y=100)
    e2=Entry(t,width=20,font='arial 15 bold')
    e2.place(x=400,y=150)
    e3=Entry(t,width=20,font='arial 15 bold')
    e3.place(x=400,y=200)
    e4=Entry(t,width=20,font='arial 15 bold')
    e4.place(x=400,y=250)
    bt=Button(t,text='Save',command=savedata,font='algerian 20 bold',bg='lightcyan2')
    bt.place(x=100,y=350)
    bt=Button(t,text='cancel',command=close,font='algerian 20 bold',bg='thistle1')
    bt.place(x=400,y=350)
    t.config(bg='gray73')
    t.mainloop()