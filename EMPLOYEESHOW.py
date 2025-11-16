# Employee_Show_Screen
import tkinter
from tkinter import *
from tkinter import messagebox
import pymysql

def showemployeeshow():
    t = tkinter.Tk()
    t.geometry('1000x700')
    t.title("Employee Data")
    t.config(bg='lavender')

    # 🪶 Frame to hold Text widget and scrollbar together
    frame = Frame(t, bg='lavender')
    frame.place(x=20, y=50)

    # 🪶 Text box for data display
    ta = Text(
        frame, height=25, width=130,
        font=('Courier New', 11, 'bold'),   # ✅ Monospaced font for perfect alignment
        fg='black', bg='lavender'
    )
    ta.pack(side=LEFT, fill=BOTH)

    # 🧭 Scrollbar for text area
    scrollbar = Scrollbar(frame, orient=VERTICAL, command=ta.yview)
    scrollbar.pack(side=RIGHT, fill=Y)
    ta.config(yscrollcommand=scrollbar.set)

    def filldata():
        try:
            db = pymysql.connect(host='localhost', user='root', password='root', database='eps')
            cur = db.cursor()
            sql = "SELECT * FROM employee"
            cur.execute(sql)
            data = cur.fetchall()

            if not data:
                ta.insert(END, "No records found in employee table.")
                return

            # 🧾 ---- Heading Row ----
            heading = (
                f"{'EMP ID':<12}"
                f"{'EMP.NAME':<25}"
                f"{'ADDRESS':<25}"
                f"{'PHONE NO.':<20}"
                f"{'EMAIL ID':<35}"
                f"{'DEPT ID':<10}\n"
            )
            ta.insert(END, heading)
            ta.insert(END, "-" * 140 + "\n")

            # 🧩 ---- Data Rows ----
            for res in data:
                line = (
                    f"{str(res[0]):<12}"
                    f"{str(res[1]):<25}"
                    f"{str(res[2]):<25}"
                    f"{str(res[3]):<20}"
                    f"{str(res[4]):<35}"
                    f"{str(res[5]):<10}\n"
                )
                ta.insert(END, line)

            db.close()

        except Exception as e:
            messagebox.showerror("Database Error", f"Error: {e}")

    filldata()
    t.mainloop()
