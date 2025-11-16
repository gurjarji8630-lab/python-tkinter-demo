import tkinter 
from tkinter import* 
import pymysql


def showhodshow():
    t = tkinter.Tk()
    t.title("HOD Data Viewer")
    t.geometry('800x800')
    t.config(bg='#F0DDD6')

 
    def filldata():
        db = pymysql.connect(host='localhost', user='root', password='root', database='eps')
        cur = db.cursor()
        sql="SELECT * FROM hod"
        cur.execute(sql)
        data = cur.fetchall()
        
    #-----Heading row------
        heading=f"{'HOD ID':<8}{'Dept.ID':<25}{'H.Name':<29}{'Emp ID':<20}\n"
        ta.insert(END,heading)
        ta.insert(END,"-"*85+"\n")
        
    #----Data rows---
        for res in data:
            line = f"{str(res[0]):<8}{res[1]:<25}{res[2]:<29}{str(res[3]):<20}\n"
            ta.insert(END,line)
        db.close()
        
       

    
    #----TEXT AREA FOR DATA DISPLAY----
    ta=Text(t,height=20,width=90,font=('Consolas',15),bg='white')
    ta.place(x=20,y=50)
    filldata()
    t.mainloop()
     