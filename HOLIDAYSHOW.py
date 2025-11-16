#Holidaydata_Show_Screen
import tkinter
from tkinter import *
import pymysql

def showholidaydatashow():
    t = tkinter.Tk()
    t.title("Holiday Data Viewer")
    t.geometry('750x400')
    t.config(bg='bisque3')

    def filldata():
        db = pymysql.connect(host='localhost', user='root', password='root', database='eps')
        cur = db.cursor()
        sql = "select * from holidaydata"
        cur.execute(sql)
        data = cur.fetchall()

        # --- Heading row ---
        heading = f"{'Emp ID':<8}{'Dept ID':<25}{'Leave ID':<15}{'Leave Type':<15}{'No.of Leaves':<20}\n"
        ta.insert(END, heading)
        ta.insert(END, "-" * 85 + "\n")

        # --- Data rows ---
        for res in data:
            line = f"{str(res[0]):<8}{res[1]:<25}{str(res[2]):<15}{res[3]:<15}{str(res[4]):<20}\n"
            ta.insert(END, line)

        db.close()

    # --- Text area for data display ---
    ta = Text(t, height=20, width=90, font=('Consolas', 11), bg='bisque2')
    ta.place(x=20, y=50)

    # --- Call function to fill data ---
    filldata()

    t.mainloop()