# COMPANY SAVE TABLE
import tkinter
from tkinter import*
import pymysql
from tkinter import messagebox
from tkinter import ttk
#from tkinter import PhotoImage

from tkinter import ttk
def showcompany1save():
    t=tkinter.Tk() 
    t.geometry('800x800')
    #img=PhotoImage(file="C:/Users/LENOVO/OneDrive/Pictures/picsavecompany.png")
    #pic=Label(t,image=img)
    #pic.place(x=700,y=100)
    
    def savedata():
        if len(e1.get())==0 or len(e2.get())==0 or len(e3.get())==0 or len(e4.get())==0:
            messagebox.showinfo('Hi','Please fill all details')
        else:
            db=pymysql.connect(host='localhost',user='root',password='root',database='eps')
            cur=db.cursor()
            xa=int(e1.get())
            xb=e2.get()
            xc=e3.get()
            xd=e4.get()
            xe=e5.get()
            xf=e6.get()
            xg=e7.get()
            sql="insert into company1 values(%d,'%s','%s','%s','%s','%s','%s')"%(xa,xb,xc,xd,xe,xf,xg)
            cur.execute(sql)
            db.commit()
            db.close()
            e1.delete(0,100)
            e2.delete(0,100)
            e3.delete(0,100)
            e4.delete(0,100)
            e5.delete(0,100)
            e6.delete(0,100)
            e7.delete(0,100)
            messagebox.showinfo('Hi','Data Saved')
    def filldata():
          
          lt=[]
          db=pymysql.connect(host='localhost',user='root',password='root',database='eps')
          cur=db.cursor()
          sql="select comid from company1"
          cur.execute(sql)
          data=cur.fetchall()
          for res in data:
              lt.append(res[0])
          e1['values']=lt
               
          db.close()
            
    def close():
        t.destroy()
    g=Label(t,text='COMPANY SAVEDATA SHEET',font='algerian 30 bold',fg='black',bg='antiquewhite3')
    g.place(x=90,y=10)
            
    a=Label(t,text='Comp ID',font='ariel 13 bold',bg='#D6CBBF')
    a.place(x=50,y=100)
    e1=ttk.Combobox(t)
    filldata()
    e1.place(x=450,y=100)
    b=Label(t,text='Name',font='ariel 13 bold',bg='#D6CBBF')
    b.place(x=50,y=150)
    e2=Entry(t,width=20)
    e2.place(x=450,y=150)
    f=Label(t,text='Address',font='ariel 13 bold',bg='#D6CBBF')
    f.place(x=50,y=200)
    e3=Entry(t,width=20)
    e3.place(x=450,y=200)
    g=Label(t,text='City',font='ariel 13 bold',bg='#D6CBBF')
    g.place(x=50,y=250)
    e4=Entry(t,width=20)
    e4.place(x=450,y=250)
    h=Label(t,text='Phoneno',font='ariel 13 bold',bg='#D6CBBF')
    h.place(x=50,y=300)
    e5=Entry(t,width=20)
    e5.place(x=450,y=300)
    j=Label(t,text='Email',font='ariel 13 bold',bg='#D6CBBF')
    j.place(x=50,y=350)
    e6=Entry(t,width=20)
    e6.place(x=450,y=350)
    l=Label(t,text='Regno',font='ariel 13 bold',bg='#D6CBBF')
    l.place(x=50,y=400)
    e7=Entry(t,width=20)
    e7.place(x=450,y=400)
    bt=Button(t,text='Save',font='ariel 12 bold',command=savedata,bg='GRAY66')
    bt.place(x=70,y=500)
    bt1=Button(t,text='Cancel',font='ariel 12 bold',command=close,bg='gray66')
    bt1.place(x=470,y=500)
    t.config(bg='#D6CBBF')
    t.mainloop()