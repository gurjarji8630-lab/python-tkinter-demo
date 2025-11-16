#HOD_Save_Screen
import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
#from tkinter import PhotoImage
def showhodsave():

    import pymysql
    t=tkinter.Tk()
    t.geometry('800x800')
    #img=PhotoImage(file="C:/Users/LENOVO/OneDrive/Pictures/cc.png")
    #pic=Label(t,image=img)
    #pic.place(x=700,y=40)
    
    def savedata():
        if len(e1.get())==0 or len(e2.get())==0 or len(e3.get())==0 or len(e4.get())==0:
            messagebox.showinfo('Hi','Please fill all details')
        else:
            db=pymysql.connect(host='localhost',user='root',password='root',database='eps')
            cur=db.cursor()
            xa=int(e1.get())
            xb=int(e2.get())
            xc=e3.get()
            xd=int(e4.get())
            sql="insert into HOD values(%d,%d,'%s',%d)"%(xa,xb,xc,xd)
            cur.execute(sql)
            db.commit()
            db.close()
            e1.delete(0,100)
            e2.delete(0,100)
            e3.delete(0,100)
            e4.delete(0,100)
            messagebox.showinfo('Hi','Data Saved')
    def filldata():
          
          lt=[]
          db=pymysql.connect(host='localhost',user='root',password='root',database='eps')
          cur=db.cursor()
          sql="select hodid from hod"
          cur.execute(sql)
          data=cur.fetchall()
          for res in data:
              lt.append(res[0])
          e1['values']=lt
               
          db.close()
    def filldatadeptid():
          
          lt=[]
          db=pymysql.connect(host='localhost',user='root',password='root',database='eps')
          cur=db.cursor()
          sql="select deptid from hod"
          cur.execute(sql)
          data=cur.fetchall()
          for res in data:
              lt.append(res[0])
          e2['values']=lt
               
          db.close()
    def filldataempid():
          
          lt=[]
          db=pymysql.connect(host='localhost',user='root',password='root',database='eps')
          cur=db.cursor()
          sql="select empid from hod"
          cur.execute(sql)
          data=cur.fetchall()
          for res in data:
              lt.append(res[0])
          e4['values']=lt
               
          db.close()
            
    def close():
        t.destroy()
    g=Label(t,text='HOD SAVEDATA SHEET',font='ELEPHANT 35 bold',fg='WHITE',bg='#bc5090')
    g.place(x=160,y=10)
    
    a=Label(t,text='HOD ID',font='arial 30 bold',bg='rosybrown3')
    a.place(x=50,y=150)
    e1=ttk.Combobox(t,font='ariel 25 bold')
    filldata()
    e1.place(x=600,y=150)
    
    b=Label(t,text='Department ID',font='ariel 30 bold',bg='rosybrown3')
    b.place(x=50,y=250)
    e2=ttk.Combobox(t,font='ariel 25 bold')
    filldatadeptid()
    e2.place(x=600,y=250)
    
    d=Label(t,text='HOD Name',font='ariel 30 bold',bg='rosybrown3')
    d.place(x=50,y=350)
    e3=Entry(t,width=20,font='ariel 25 bold')
    e3.place(x=600,y=350)
    
    e=Label(t,text='Employee ID',font='ariel 30 bold',bg='rosybrown3')
    e.place(x=50,y=450)
    e4=ttk.Combobox(t,font='ariel 25 bold')
    filldataempid()
    e4.place(x=600,y=450)
    
    k=Button(t,text='Save',command=savedata,font='ariel 25 bold',bg='#88976C',fg='white')
    k.place(x=50,y=550)
    k=Button(t,text='Close',command=close,font='ariel 25 bold',bg='#98A77C',fg='white')
    k.place(x=600,y=550)
    t.config(bg='rosybrown3')
    
    t.mainloop()