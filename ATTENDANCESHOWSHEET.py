# Attendance_Show_Screen
import tkinter
from tkinter import *
from tkinter import messagebox
import pymysql

def showattendanceshowsheet():
    t = tkinter.Tk()
    t.geometry('900x600')
    t.title("Attendance Data")
    t.config(bg='#a59694')

    # 🪶 Frame for Text + Scrollbar
    frame = Frame(t, bg='#a59694')
    frame.place(x=20, y=50)

    # 🧾 Text Area (Arial font)
    ta = Text(
        frame, height=25, width=110,
        font=('Courier New', 14, 'bold'),
        fg='black', bg='#a59694'
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
            sql = "SELECT * FROM attendance"
            cur.execute(sql)
            data = cur.fetchall()

            if not data:
                ta.insert(END, "No records found in attendance table.")
                return

            # 🧾 Column Headers
            heading = (
                f"{'EMP ID':<15}"
                f"{'MONTH':<15}"
                f"{'DATE':<20}\n"
            )
            ta.insert(END, heading)
            ta.insert(END, "-" * 50 + "\n")

            # 🧩 Data Rows
            for res in data:
                line = (
                    f"{str(res[0]):<15}"
                    f"{str(res[1]):<15}"
                    f"{str(res[2]):<20}\n"
                )
                ta.insert(END, line)

            db.close()

        except Exception as e:
            messagebox.showerror("Database Error", f"Error: {e}")

    # Fill the data
    filldata()
    t.mainloop()
