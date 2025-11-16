# COMPANY1 SHOW DATA
import tkinter
from tkinter import *
from tkinter import messagebox
import pymysql

def showcompany1show():
    
    t = tkinter.Tk()
    t.geometry('1000x600')
    t.title("Company1 Data")
    t.config(bg='#D6CBBF')
    
    def filldata():
        try:
            db = pymysql.connect(host='localhost', user='root', password='root', database='eps')
            cur = db.cursor()
            sql = "SELECT * FROM company1"
            cur.execute(sql)
            data = cur.fetchall()
            
            if not data:
                ta.insert(END, "No records found in company1 table.")
                return

            # 🧾 ---- Heading Row ----
            heading = (
                f"{'COMP ID':<10}"
                f"{'NAME':<25}"
                f"{'ADDRESS':<30}"
                f"{'CITY':<20}"
                f"{'PHONE NO.':<18}"
                f"{'EMAIL':<30}"
                f"{'REG NO.':<15}\n"
            )
            ta.insert(END, heading)
            ta.insert(END, "-" * 140 + "\n")

            # 🧩 ---- Data Rows ----
            for res in data:
                # Ensure all values are converted to string safely
                line = (
                    f"{str(res[0]):<10}"
                    f"{str(res[1]):<25}"
                    f"{str(res[2]):<30}"
                    f"{str(res[3]):<20}"
                    f"{str(res[4]):<18}"
                    f"{str(res[5]):<30}"
                    f"{str(res[6]):<15}\n"
                )
                ta.insert(END, line)

            db.close()

        except Exception as e:
            messagebox.showerror("Database Error", f"Error: {e}")

    # 🪶 Text box for data display
    ta = Text(t, height=25, width=140, font=('Courier New', 11, 'bold'), fg='black', bg='gray66')
    ta.place(x=20, y=50)
    
    filldata()
    t.mainloop()
