import tkinter as tk
from tkinter import *
from tkinter import messagebox
import pymysql
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def showsalarydeductionshow():
    t = Tk()
    t.geometry('1200x800')
    t.title("Salary Deduction Data")
    t.config(bg='PALETURQUOISE3')

    # Main frame to hold table and graph side by side
    main_frame = Frame(t, bg='PALETURQUOISE3')
    main_frame.pack(fill=BOTH, expand=True, padx=10, pady=10)

    # ---- Left Frame: Table ----
    table_frame = Frame(main_frame, bg='PALETURQUOISE3')
    table_frame.pack(side=LEFT, fill=BOTH, expand=True)

    ta = Text(table_frame, height=25, width=70, font=('Arial', 12, 'bold'), fg='black', bg='PALETURQUOISE3')
    ta.pack(side=LEFT, fill=BOTH, expand=True)

    scrollbar = Scrollbar(table_frame, orient=VERTICAL, command=ta.yview)
    scrollbar.pack(side=RIGHT, fill=Y)
    ta.config(yscrollcommand=scrollbar.set)

    # ---- Right Frame: Graph ----
    graph_frame = Frame(main_frame, bg='PALETURQUOISE3')
    graph_frame.pack(side=RIGHT, fill=BOTH, expand=True)

    # ---- Fill table data ----
    def filldata():
        try:
            db = pymysql.connect(host='localhost', user='root', password='root', database='eps')
            cur = db.cursor()
            cur.execute("SELECT * FROM salarydeduction")
            data = cur.fetchall()
            db.close()

            if not data:
                ta.insert(END, "No records found in salarydeduction table.")
                return

            ta.insert(END, f"{'EMP ID':<15}{'DEPT ID':<15}{'MONTH':<20}{'DEDUCTION':<20}\n")
            ta.insert(END, "-"*75 + "\n")

            for res in data:
                ta.insert(END, f"{str(res[0]):<15}{str(res[1]):<15}{str(res[2]):<20}{str(res[3]):<20}\n")

        except Exception as e:
            messagebox.showerror("Database Error", f"Error: {e}")

    # ---- Show graph ----
    def show_graph():
        # Clear previous graph if exists
        for widget in graph_frame.winfo_children():
            widget.destroy()

        try:
            db = pymysql.connect(host='localhost', user='root', password='root', database='eps')
            cur = db.cursor()
            cur.execute("SELECT empid, SUM(deduction) FROM salarydeduction GROUP BY empid")
            data = cur.fetchall()
            db.close()

            if not data:
                messagebox.showinfo("No Data", "No data to plot!")
                return

            emp_ids = [str(row[0]) for row in data]
            deductions = [row[1] for row in data]

            fig, ax = plt.subplots(figsize=(6,4))
            ax.bar(emp_ids, deductions, color='skyblue')
            ax.set_xlabel('Employee ID')
            ax.set_ylabel('Total Deduction')
            ax.set_title('Total Salary Deduction per Employee')
            plt.xticks(rotation=45)

            canvas = FigureCanvasTkAgg(fig, master=graph_frame)
            canvas.draw()
            canvas.get_tk_widget().pack(fill=BOTH, expand=True)

        except Exception as e:
            messagebox.showerror("Error", f"Error: {e}")

    filldata()
    Button(t, text='Show Graph', command=show_graph, font=('Arial',12,'bold'), bg='LIGHTSTEELBLUE3').pack(pady=10)

    t.mainloop()
