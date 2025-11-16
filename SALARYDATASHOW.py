# Show the complete table of salarydata
import tkinter
from tkinter import *
from tkinter import messagebox
import pymysql

def showsalarydatashow():
    t = tkinter.Tk()
    t.geometry('950x600')
    t.title("Salary Data")
    t.config(bg='lightsteelblue3')

    # 🪶 Frame for text + scrollbar
    frame = Frame(t, bg='lightsteelblue3')
    frame.place(x=20, y=50)

    # 🧾 Text box
    ta = Text(
        frame, height=25, width=120,
        font=('Courier New', 11, 'bold'),
        fg='black', bg='lightsteelblue3'
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
            sql = "SELECT * FROM salarydata"
            cur.execute(sql)
            data = cur.fetchall()

            if not data:
                ta.insert(END, "No records found in salarydata table.")
                return

            # 🧾 ---- Heading Row ----
            heading = (
                f"{'EMP ID':<15}"
                f"{'DEPT ID':<15}"
                f"{'CTC':<20}"
                f"{'PF':<20}"
                f"{'PER MONTH SALARY':<20}\n"
            )
            ta.insert(END, heading)
            ta.insert(END, "-" * 100 + "\n")

            # 🧩 ---- Data Rows ----
            for res in data:
                line = (
                    f"{str(res[0]):<15}"
                    f"{str(res[1]):<15}"
                    f"{str(res[2]):<20}"
                    f"{str(res[3]):<20}"
                    f"{str(res[4]):<20}\n"
                )
                ta.insert(END, line)

            db.close()

        except Exception as e:
            messagebox.showerror("Database Error", f"Error: {e}")

    filldata()
    t.mainloop()
