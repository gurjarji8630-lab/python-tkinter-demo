import tkinter as tk
from tkinter import messagebox, PhotoImage
from captcha.image import ImageCaptcha
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random
import pymysql
from dashboard import *
from NEWLOGIN import *

# ---------------- Global variables ----------------
st = ''
otp_global = None

# ---------------- CAPTCHA ----------------
def capgen():
    img = ImageCaptcha(width=150, height=150)
    r = random.randint(1000, 9999)
    global st
    st = str(r)
    img.write(st, 'capone.png')
    messagebox.showinfo('Info', 'Captcha generated ✅')

    xa = PhotoImage(file='capone.png')
    d.config(image=xa)
    d.image = xa

# ---------------- OTP SEND ----------------
def gmail():
    from_address = "gurjarji8630@gmail.com"
    to_address = username_entry1.get()
    pwd = password_entry2.get()

    if not to_address or not pwd:
        messagebox.showerror("Error", "Please enter email and password first!")
        return

    # Generate OTP
    global otp_global
    otp_global = str(random.randint(100000, 999999))

    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Your OTP Code"
    msg['From'] = from_address
    msg['To'] = to_address
    msg.attach(MIMEText(f"Your OTP is: {otp_global}", 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_address, "otprhdpbvabjqlrx")  # Your app password
        server.sendmail(from_address, to_address, msg.as_string())
        server.quit()
        messagebox.showinfo("Success", "OTP sent to your email ✅")

        db = pymysql.connect(host='localhost', user='root', password='root', database='eps')
        cur = db.cursor()
        cur.execute("SELECT * FROM logintable WHERE loginid=%s", (to_address,))
        if cur.fetchone():
            cur.execute("UPDATE logintable SET password=%s, otp=%s WHERE loginid=%s", (pwd, otp_global, to_address))
        else:
            cur.execute("INSERT INTO logintable (loginid, password, otp) VALUES (%s, %s, %s)",
                        (to_address, pwd, otp_global))
        db.commit()
        db.close()

    except Exception as e:
        messagebox.showerror("Error", f"Failed to send OTP\n{e}")

# ---------------- VERIFY OTP ----------------
def verify():
    uid = username_entry1.get()
    pwd = password_entry2.get()
    otp = OTP_entry3.get()

    if not uid or not pwd or not otp:
        messagebox.showwarning("Warning", "Please fill all fields!")
        return

    db = pymysql.connect(host='localhost', user='root', password='root', database='eps')
    cur = db.cursor()
    cur.execute("SELECT * FROM logintable WHERE loginid=%s", (uid,))
    result = cur.fetchone()
    db.close()

    if result:
        db_pwd, db_otp = result[1], result[2]
        if pwd == db_pwd and otp == db_otp:
            messagebox.showinfo("Success", "OTP Verified ✅")
            login_btn.config(state="normal")
            newlogin_btn.config(state="normal")
        else:
            messagebox.showerror("Error", "Invalid Password or OTP ❌")
    else:
        messagebox.showerror("Error", "User not found ❌")

# ---------------- LOGIN ----------------
def login():
    user = username_entry1.get()
    pwd = password_entry2.get()
    captcha = captcha_entry3.get()

    if not user or not pwd or not captcha:
        messagebox.showwarning("Warning", "Please fill all fields!")
        return

    if captcha == st:
        messagebox.showinfo("Success", "Login Successful ✅")
        showdashboard()
    else:
        messagebox.showwarning("Warning", "Invalid Captcha ❌")

def NEWlogin():
    user = username_entry1.get()
    pwd = password_entry2.get()
    if user == "Chhaya" and pwd == "1234":
        messagebox.showinfo("Success", "Login Successful ✅")
        showNEWLOGIN()
    else:
        messagebox.showerror("Error", "Invalid Username or Password ❌")

# ---------------- UI DESIGN ----------------
t = tk.Tk()
t.title("Employee Payroll Portal - Login")
t.geometry("900x800")

# ====== HEADING BAR ======
header = tk.Frame(t, bg="#6D68AF", height=70)
header.pack(fill="x")
tk.Label(header, text="🏢 EMPLOYEE PAYROLL PORTAL 🏢",
         font=("Segoe UI", 27, "bold"), bg="white", fg="purple").pack(pady=10)

# ====== LEFT SIDE (Gradient Look) ======
canvas = tk.Canvas(t, width=700, height=800, highlightthickness=0)
canvas.pack(side="left", fill="both")

for i in range(800):
    r = 108 + i//30
    g = 74 + i//20
    b = 182 + i//15
    color = f"#{r:02x}{g:02x}{b:02x}"
    canvas.create_line(0, i, 700, i, fill=color)

canvas.create_text(350, 150, text="Welcome Back!", font=("Arial", 48, "bold"), fill="white")
canvas.create_text(350, 300, text="Manage your payroll securely.\nPlease log in below.",
                   font=("Arial", 16), fill="white")

# ====== RIGHT SIDE (Form Section) ======
right_frame = tk.Frame(t, bg="white", width=800, height=800)
right_frame.pack(side="right", fill="both")

signin_label = tk.Label(right_frame, text="LOG IN PAGE", font=("Arial", 32, "bold"), bg="white", fg="#3F51B5")
signin_label.place(x=200, y=20)

# Username
tk.Label(right_frame, text="Username/Email", font=("Arial", 17, "bold"), bg="white").place(x=90, y=120)
tk.Label(right_frame, text="👤", font=("Arial", 18), bg="white").place(x=60, y=120)
username_entry1 = tk.Entry(right_frame, font=("Arial", 12), bd=2, relief="groove")
username_entry1.place(x=300, y=120, width=250, height=40)

# Password
tk.Label(right_frame, text="Password", font=("Arial", 17, "bold"), bg="white").place(x=90, y=200)
tk.Label(right_frame, text="🗝", font=("Arial", 18), bg="white").place(x=60, y=200)
password_entry2 = tk.Entry(right_frame, font=("Arial", 12), bd=2, relief="groove", show="*")
password_entry2.place(x=300, y=200, width=260, height=40)

# OTP
tk.Label(right_frame, text="OTP", font=("Arial", 17, "bold"), bg="white").place(x=90, y=280)
tk.Label(right_frame, text="📧", font=("Arial", 18), bg="white").place(x=60, y=280)
OTP_entry3 = tk.Entry(right_frame, font=("Arial", 12), bd=2, relief="groove")
OTP_entry3.place(x=300, y=280, width=260, height=40)

# Buttons
send_otp_btn = tk.Button(right_frame, text="Send OTP", font=("Arial", 12, "bold"), bg="#B5C99A",
                         fg="black", command=gmail)
send_otp_btn.place(x=60, y=350, width=140, height=35)

verify_otp_btn = tk.Button(right_frame, text="Verify OTP", font=("Arial", 12, "bold"), bg="#B5C99A",
                           fg="black", command=verify)
verify_otp_btn.place(x=450, y=350, width=140, height=35)

# Captcha
d = tk.Label(right_frame, bg="black")
d.place(x=400, y=400)
tk.Label(right_frame, text="Captcha", font=("Arial", 17, "bold"), bg="white").place(x=80, y=450)
captcha_entry3 = tk.Entry(right_frame, font=("Arial", 12), bd=2, relief="groove")
captcha_entry3.place(x=70, y=500, width=200, height=40)
captcha_btn = tk.Button(right_frame, text="Generate Captcha", font=("Arial", 12, "bold"),
                        bg="skyblue", fg="black", command=capgen)
captcha_btn.place(x=230, y=350, width=180, height=40)

# Login Buttons
login_btn = tk.Button(right_frame, text="Log In", font=("Arial", 12, "bold"), bg="#3F51B5", fg="white",
                      command=login)
login_btn.place(x=100, y=580, width=120, height=35)

newlogin_btn = tk.Button(right_frame, text="NEW Log In", font=("Arial", 12, "bold"),
                         bg="#3F51B5", fg="white", command=NEWlogin)
newlogin_btn.place(x=350, y=580, width=120, height=35)

t.mainloop()
