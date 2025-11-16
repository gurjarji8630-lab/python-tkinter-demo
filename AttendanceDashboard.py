import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from ATTENDANCESAVE import*
from ATTENDANCEDELETE import*
from ATTENDANCEUPDATE import*
from ATTENDANCEFIND import*
from ATTENDANCENAVIGATOR import*
from ATTENDANCESHOWSHEET import*

import pymysql

def showAttendanceDashboard():
    
    
    t=tkinter.Tk()
    t.geometry('800x800')
    
    
    g=Label(t,text='ATTENDANCE DASHBOARD',font='algerian 40 bold',fg='white',bg='#235347')
    g.place(x=120,y=10)
    
    # Buttons
    b1 = Button(t, text='Insert', command=showattendancesave,
                   font=('Elephant', 30, 'bold'), bg='palegreen')
    b1.place(x=80, y=150, width=200, height=60)

    b2 = Button(t, text='Delete', command=showattendancedelete,
                   font=('Elephant', 30, 'bold'), bg='lightcoral')
    b2.place(x=80, y=250, width=200, height=60)

    b3 = Button(t, text='Update', command=showattendanceupdate,
                   font=('Elephant', 30, 'bold'), bg='khaki')
    b3.place(x=80, y=350, width=200, height=60)

    b4 = Button(t, text='Review', command=showattendanceshowsheet,
                   font=('Elephant', 30, 'bold'), bg='lightblue')
    b4.place(x=600, y=150, width=200, height=60)

    b5 = Button(t, text='Find', command=showattendancefind,
                   font=('Elephant', 30, 'bold'), bg='plum')
    b5.place(x=600, y=250, width=200, height=60)

    b6 = Button(t, text='Navigator', command=showattendancenavigator,
                   font=('Elephant', 30, 'bold'), bg='burlywood')
    b6.place(x=600, y=350, width=200, height=60)
    t.config(bg='#2FC4B2')
   
    
   
    t.mainloop()
   