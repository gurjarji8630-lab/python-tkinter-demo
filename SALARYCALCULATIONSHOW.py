# SalaryCalculation_Show_Screen
import tkinter
from tkinter import *
from tkinter import messagebox
import pymysql

def showsalarycalculationshow():
    t = tkinter.Tk()
    t.geometry('950x600')
    t.title("Salary Calculation Data")
    t.config(bg='snow3')

    # 🪶 Frame for Text + Scrollbar
    frame = Frame(t, bg='snow3')
    frame.place(x=20, y=50)

    # 🧾 Text Area
    ta = Text(
        frame, height=25, width=110,
        font=('Courier New', 13, 'bold'),
        fg='black', bg='snow3'
    )
    ta.pack(side=LEFT, fill=BOTH)

    # 🧭 Scrollbar
    scrollbar = Scrollbar(frame, orient=VERTICAL, command=ta.yview)
    scrollbar.pack(side=RIGHT, fill=Y)
    ta.config(yscrollcommand=scrollbar.set)

    def filldata():
        try:
            db = pymysql.connect(host='localhost', user='root', password='root', database='eps')
            cur = db.cursor()
            sql = "SELECT * FROM salarycalculation"
            cur.execute(sql)
            data = cur.fetchall()

            if not data:
                ta.insert(END, "No records found in salarycalculation table.")
                return

            # 🧾 ---- Heading Row ----
            heading = (
                f"{'EMP ID':<15}"
                f"{'DEPT ID':<15}"
                f"{'NO.OF DAYS':<20}"
                f"{'FINAL SALARY':<20}\n"
            )
            ta.insert(END, heading)
            ta.insert(END, "-" * 70 + "\n")

            # 🧩 ---- Data Rows ----
            for res in data:
                line = (
                    f"{str(res[0]):<15}"
                    f"{str(res[1]):<15}"
                    f"{str(res[2]):<20}"
                    f"{str(res[3]):<20}\n"
                )
                ta.insert(END, line)

            db.close()

        except Exception as e:
            messagebox.showerror("Database Error", f"Error: {e}")

    # Call the function
    filldata()

    t.mainloop()
