import tkinter
from tkinter import*
from tkinter import messagebox
from tkinter import ttk
import pymysql
from AttendanceDashboard import*
from Company1Dashboard import*
from DepartmentDashboard import*
from EmployeeDashboard import*
from HODDashboard import*
from SalarydataDashboard import*
from LeavedataDashboard import*
from HolidaydataDashboard import*
from SalarydeductionDashboard import*
from SalarycalculationDashboard import*


def showdashboard():
    
    
    t=tkinter.Tk() 
    t.geometry('1000x1000')
    g=Label(t,text='DASHBOARD',font='ELEPHANT 40 bold',fg='white',bg='#235347')
    g.place(x=400,y=10)
    
    bt1=Button(t,text='HOD',command=showHODDashboard,font='elephant 25 bold',bg='palegreen3')
    bt1.place(x=70,y=150)
    
           
    bt2=Button(t,text='COMPANY1',command=showCompany1Dashboard,font='elephant 25 bold',bg='#D4F3B7')
    bt2.place(x=60,y=250)
           
    bt3=Button(t,text='EMPLOYEE',command=showEmployeeDashboard,font='elephant 25 bold',bg='cornsilk3')
    bt3.place(x=50,y=350)
           
    bt4=Button(t,text='SALARYDATA',command=showSalarydataDashboard,font='elephant 25 bold',bg='#93A87E')
    bt4.place(x=50,y=450)
           
    bt5=Button(t,text='DEPARTMENT',command=showDepartmentDashboard,font='elephant 25 bold',bg="gold")
    bt5.place(x=50,y=550)
           
    bt6=Button(t,text='LEAVEDATA',command=showLeavedataDashboard,font='elephant 25 bold',bg='lightcoral')
    bt6.place(x=850,y=150)
           
    bt7=Button(t,text='ATTENDANCE',command=showAttendanceDashboard,font='elephant 25 bold',bg='khaki')
    bt7.place(x=850,y=250)
           
    bt8=Button(t,text='HOLIDAYDAYA',command=showHolidaydataDashboard,font='elephant 25 bold',bg='BISQUE3')
    bt8.place(x=850,y=350)
           
    bt9=Button(t,text='SALARYDEDUCTION',command=showSalarydeductionDashboard,font='elephant 25 bold',bg='sienna3')
    bt9.place(x=800,y=450) 

    bt10=Button(t,text='SALARYCALCULATION',command=showSalarycalculationDashboard,font='elephant 25 bold',bg='rosybrown3')
    bt10.place(x=800,y=550)
    t.config(bg="#289CBE")
    t.mainloop()