import tkinter as tk
from tkinter import *
from tkinter import messagebox
import pymysql
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def showleavedatashow():
    t = Tk()
    t.geometry('1200x600')
    t.title("Leave Data")
    t.config(bg='honeydew2')

    # Main frame for table + graph
    main_frame = Frame(t, bg='honeydew2')
    main_frame.pack(fill=BOTH, expand=True, padx=10, pady=10)

    # ---- Left Frame: Table ----
    table_frame = Frame(main_frame, bg='honeydew2')
    table_frame.pack(side=LEFT, fill=BOTH, expand=True)

    ta = Text(table_frame, height=25, width=70, font=('Courier New', 12, 'bold'), fg='black', bg='honeydew2')
    ta.pack(side=LEFT, fill=BOTH, expand=True)

    scrollbar = Scrollbar(table_frame, orient=VERTICAL, command=ta.yview)
    scrollbar.pack(side=RIGHT, fill=Y)
    ta.config(yscrollcommand=scrollbar.set)

    # ---- Right Frame: Graph ----
    graph_frame = Frame(main_frame, bg='honeydew2')
    graph_frame.pack(side=RIGHT, fill=BOTH, expand=True)

    # ---- Fill table data ----
    def filldata():
        try:
            db = pymysql.connect(host='localhost', user='root', password='root', database='eps')
            cur = db.cursor()
            cur.execute("SELECT * FROM leavedata")
            data = cur.fetchall()
            db.close()

            if not data:
                ta.insert(END, "No records found in leavedata table.")
                return

            ta.insert(END, f"{'LEAVE ID':<15}{'LEAVE TYPE':<15}{'LEAVE DAYS':<20}{'PAID':<25}\n")
            ta.insert(END, "-"*75 + "\n")

            for res in data:
                ta.insert(END, f"{str(res[0]):<15}{str(res[1]):<15}{str(res[2]):<20}{str(res[3]):<25}\n")

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
            cur.execute("SELECT leaveid, SUM(noofdays) FROM leavedata GROUP BY leaveid")
            data = cur.fetchall()
            db.close()

            if not data:
                messagebox.showinfo("No Data", "No data to plot!")
                return

            leave_ids = [str(row[0]) for row in data]
            leave_days = [row[1] for row in data]

            fig, ax = plt.subplots(figsize=(6,4))
            ax.bar(leave_ids, leave_days, color='skyblue')
            ax.set_xlabel('Leave ID')
            ax.set_ylabel('Total Leave Days')
            ax.set_title('Total Leave Days per Leave Type')
            plt.xticks(rotation=45)

            canvas = FigureCanvasTkAgg(fig, master=graph_frame)
            canvas.draw()
            canvas.get_tk_widget().pack(fill=BOTH, expand=True)

        except Exception as e:
            messagebox.showerror("Error", f"Error: {e}")

    filldata()
    Button(t, text='Visualization', command=show_graph, font=('Arial',12,'bold'), bg='LIGHTSTEELBLUE3').pack(pady=10)

    t.mainloop()
