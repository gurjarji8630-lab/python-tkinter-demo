import tkinter as tk
from tkinter import messagebox

import pymysql
from dashboard import *
from NEWLOGIN import *
# Login function
def login():
    user = username_entry.get()
    pwd = password_entry.get()

    if user == "chhaya" and pwd == "123":
        messagebox.showinfo("Success", "Login Successful!")
        showdashboard()
    else:
        messagebox.showerror("Error", "Invalid Username or Password")
def NEWlogin():
    user = username_entry.get()
    pwd = password_entry.get()

    if user == "chhaya" and pwd == "1234":
        messagebox.showinfo("Success", "Login Successful!")
        showNEWLOGIN()
    else:
        messagebox.showerror("Error", "Invalid Username or Password")
        
        

# Create Gradient Background
def create_gradient(canvas, width, height, color1, color2):
    r1, g1, b1 = root.winfo_rgb(color1)
    r2, g2, b2 = root.winfo_rgb(color2)
    r_ratio = (r2 - r1) / height
    g_ratio = (g2 - g1) / height
    b_ratio = (b2 - b1) / height

    for i in range(height):
        nr = int(r1 + (r_ratio * i))
        ng = int(g1 + (g_ratio * i))
        nb = int(b1 + (b_ratio * i))
        color = f"#{nr>>8:02x}{ng>>8:02x}{nb>>8:02x}"
        canvas.create_line(0, i, width, i, fill=color)

# Main window
root = tk.Tk()
root.title("Login Page")
root.geometry("800x800")
root.resizable(False, False)

# Left gradient background
canvas = tk.Canvas(root, width=400, height=700, highlightthickness=0)
canvas.pack(side="left", fill="both")
create_gradient(canvas, 400, 700, "#6C4AB6", "#9F73C5")

# Left text
canvas.create_text(200, 200, text="Welcome back!", font=("Arial", 30, "bold"), fill="white")
canvas.create_text(200, 280, text="You can sign in to access\nwith your existing account.", 
                   font=("Arial", 12), fill="white")

# Right Frame
right_frame = tk.Frame(root, bg="white", width=400, height=700)
right_frame.pack(side="right", fill="both")

signin_label = tk.Label(right_frame, text="LOG IN PAGE", font=("Arial", 25, "bold"), bg="white")
signin_label.place(x=80, y=50)

# --- Load icons ---
try:
    user_img = Image.open("C:/Users/LENOVO/OneDrive/Pictures/Screenshots/Screenshot (5405).png").resize((25, 25))
    user_icon = ImageTk.PhotoImage(user_img)

    lock_img = Image.open("C:/Users/LENOVO/OneDrive/Pictures/Screenshots/Screenshot (5405).png").resize((25, 25))
    lock_icon = ImageTk.PhotoImage(lock_img)
except Exception as e:
    print("⚠ Icon not found:", e)
    user_icon = None
    lock_icon = None

# Username field
if user_icon:
    tk.Label(right_frame, image=user_icon, bg="white").place(x=40, y=150)
tk.Label(right_frame, text="Username", font=("Arial", 15, "bold"), bg="white").place(x=70, y=150)
username_entry = tk.Entry(right_frame, font=("Arial", 12), bd=2, relief="groove")
username_entry.place(x=70, y=180, width=260, height=30)

# Password field
if lock_icon:
    tk.Label(right_frame, image=lock_icon, bg="white").place(x=40, y=230)
tk.Label(right_frame, text="Password", font=("Arial", 15,"bold"), bg="white").place(x=70, y=230)
password_entry = tk.Entry(right_frame, font=("Arial", 12), bd=2, relief="groove", show="*")
password_entry.place(x=70, y=260, width=260, height=30)

# Remember me
remember_var = tk.IntVar()
remember_check = tk.Checkbutton(right_frame, text="Remember me", variable=remember_var, bg="white")
remember_check.place(x=70, y=310)

# Forgot password
forgot_btn = tk.Button(right_frame, text="Forgot password?", bg="white", fg="blue", bd=0, cursor="hand2")
forgot_btn.place(x=200, y=310)

# Sign in button
signin_btn = tk.Button(right_frame, text="Log In", font=("Arial", 12, "bold"), bg="#6C4AB6", fg="white",
                       command=login)
signin_btn.place(x=140, y=360, width=120, height=35)

# Create account
create_label = tk.Label(right_frame, text="New here?", bg="white", font=("Arial", 10))
create_label.place(x=110, y=420)

create_btn = tk.Button(right_frame, text="Create an Account", fg="#6C4AB6", bg="white", bd=0, cursor="hand2")
create_btn.place(x=170, y=418)

signin_btn = tk.Button(right_frame, text="NEW Log In", font=("Arial", 12, "bold"), bg="#6C4AB6", fg="white",
                       command=NEWlogin)
signin_btn.place(x=140, y=460, width=120, height=35)


root.mainloop()