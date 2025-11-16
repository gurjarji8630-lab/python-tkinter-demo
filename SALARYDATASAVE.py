#save data salarydata
import tkinter
from tkinter import * 
from tkinter import messagebox 
from tkinter import ttk
#from tkinter import PhotoImage
import pymysql
def showsalarydatasave():

    t=tkinter.Tk()
    t.geometry('800x800')
   # img=PhotoImage(file="C:/Users/LENOVO/OneDrive/Pictures/Screenshots/Screenshot (5403).png")
    #pic=Label(t,image=img)
    #pic.place(x=550,y=100)
    
    def savedata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='eps')
        cur=db.cursor()
        xa=int(e1.get())
        xb=int(e2.get())
        xc=int(e3.get())
        xd=float(e4.get()) 
        xe=float(e5.get())
        

        sql="insert into salarydata values(%d,%d,'%s','%s',%d)"%(xa,xb,xc,xd,xe)
        cur.execute(sql)
        db.commit()
        db.close()
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        e5.delete(0,100)
        messagebox.showinfo('hi','Data Saved')
    
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
    def filldata1():
           
           lt=[]
           db=pymysql.connect(host='localhost',user='root',password='root',database='eps')
           cur=db.cursor()
           sql="select deptid from salarydata"
           cur.execute(sql)
           data=cur.fetchall()
           for res in data:
               lt.append(res[0])
           e2['values']=lt
                
           db.close()
             
    def close():
        t.destroy()
        
    def calculate():
        ctc=int(e3.get())
        pf=0.12*ctc
        per=ctc/12
    
        e4.insert(0,pf)
        e5.insert(0,per)
        savedata()
    
    g=Label(t,text='SALARY DATA SAVE SHEET',font='courier 35 bold',fg='black',bg='lightsteelblue')
    g.place(x=90,y=10)
        
    a=Label(t,text='Empid',font='arial 15 bold',bg='lightsteelblue3')
    a.place(x=50,y=100)
    e1=ttk.Combobox(t)
    filldata()
    e1.place(x=400,y=100)
    
    
    b=Label(t,text='Deptid',font='ariel 15 bold',bg='lightsteelblue3')
    b.place(x=50,y=150)
    e2=ttk.Combobox(t)
    filldata1()
    e2.place(x=400,y=150)
    
    d=Label(t,text='CTC',font='ariel 15 bold',bg='lightsteelblue3')
    d.place(x=50,y=200)
    e3=Entry(t,width=20)
    e3.place(x=400,y=200)
    
    e=Label(t,text='PF',font='ariel 15 bold',bg='lightsteelblue3')
    e.place(x=50,y=250)
    e4=Entry(t,width=20)
    e4.place(x=400,y=250)
    
    e=Label(t,text='Permonth salary',font='ariel 15 bold',bg='lightsteelblue3')
    e.place(x=50,y=300)
    e5=Entry(t,width=20)
    e5.place(x=400,y=300)
    
    b1=Button(t,text='Save',command=savedata,font='elephant 15 bold',bg='skyblue')
    b1.place(x=50,y=400)
    b2=Button(t,text='Close',command=close,font='elephant 15 bold',bg='rosybrown')
    b2.place(x=400,y=400)
    b3=Button(t,text='Calculate',command=calculate,font='elephant 13 bold',bg='khaki')
    b3.place(x=600,y=250)
    t.config(bg='lightsteelblue3')
    t.mainloop()