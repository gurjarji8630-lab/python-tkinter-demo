#Leavedata_Save_Screen
import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
#from tkinter import PhotoImage
def showleavedatasave():
    import pymysql
    t=tkinter.Tk()
    t.geometry('800x800')
    #img=PhotoImage(file="C:/Users/LENOVO/OneDrive/Pictures/Screenshots/Screenshot (5404).png")
    #pic=Label(t,image=img)
    #pic.place(x=600,y=150)
    
    def savedata():
        if len(e1.get())==0 or len(e2.get())==0 or len(e3.get())==0 or len(e4.get())==0:
            messagebox.showinfo('Hi','Please fill all details')
        else:
            db=pymysql.connect(host='localhost',user='root',password='root',database='eps')
            cur=db.cursor()
            xa=int(e1.get())
            xb=e2.get()
            xc=int(e3.get())
            xd=e4.get()
            sql="insert into leavedata values(%d,'%s',%d,'%s')"%(xa,xb,xc,xd)
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
        sql="select leaveid from leavedata" 
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            lt.append(res[0])
        e1['value']=lt
        db.close()  
    g=Label(t,text='LEAVE DATA SAVE SHEET',font='elephant 30 bold',fg='black',bg='honeydew3')
    g.place(x=70,y=10)
    
    a=Label(t,text='Leave ID',font='ariel 15 bold',bg='honeydew2')
    a.place(x=50,y=100)
    e1=ttk.Combobox(t)
    filldata()
    e1.place(x=400,y=100)
    
    b=Label(t,text='Leavetype',font='ariel 15 bold',bg='honeydew2')
    b.place(x=50,y=150)
    e2=Entry(t,width=30)
    e2.place(x=400,y=150)
    
    d=Label(t,text='No of days',font='ariel 15 bold',bg='honeydew2')
    d.place(x=50,y=200)
    e3=Spinbox(t,from_=0,to=30)
    e3.place(x=400,y=200)
    
    e=Label(t,text='Paid',font='ariel 15 bold',bg='honeydew2')
    e.place(x=50,y=250)
    e4=Entry(t,width=30)
    e4.place(x=400,y=250)
    
    k=Button(t,text='Save',command=savedata,font='ariel 13 bold',bg='gray80')
    k.place(x=300,y=300)
    t.config(bg='honeydew2')
    
    t.mainloop()