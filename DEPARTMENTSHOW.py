# Show all data of department
import tkinter
from tkinter import *
from tkinter import messagebox
import pymysql

def showdepartmentshow():
    t = tkinter.Tk()
    t.geometry('950x600')
    t.title("Department Data")
    t.config(bg='gray73')

    # 🪶 Frame for Text + Scrollbar
    frame = Frame(t, bg='gray73')
    frame.place(x=20, y=50)

    # 🧾 Text Area
    ta = Text(
        frame, height=25, width=110,
        font=('Courier New', 11, 'bold'),
        fg='black', bg='lavender'
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
            sql = "SELECT * FROM department"
            cur.execute(sql)
            data = cur.fetchall()

            if not data:
                ta.insert(END, "No records found in department table.")
                return

            # 🧾 ---- Heading Row ----
            heading = (
                f"{'DEPT ID':<15}"
                f"{'DEPT NAME':<25}"
                f"{'HOD':<25}"
                f"{'DAYS IN WEEK':<15}\n"
            )
            ta.insert(END, heading)
            ta.insert(END, "-" * 85 + "\n")

            # 🧩 ---- Data Rows ----
            for res in data:
                line = (
                    f"{str(res[0]):<15}"
                    f"{str(res[1]):<25}"
                    f"{str(res[2]):<25}"
                    f"{str(res[3]):<15}\n"
                )
                ta.insert(END, line)

            db.close()

        except Exception as e:
            messagebox.showerror("Database Error", f"Error: {e}")

    filldata()
    t.mainloop()
