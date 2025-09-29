import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Login Page")
root.geometry("500x500")
root.configure (bg="blue")


tk.Label(root, text="Enter your username here:", bg = "Yellow").pack(pady=5)
username_entry = tk.Entry(root)
username_entry.pack()

tk.Label(root, text="Enter your password here:", bg = "Orange").pack(pady=5)
password_entry = tk.Entry(root, show='*')  
password_entry.pack()

def login():
    username = username_entry.get()
    password = password_entry.get()
    if username == "Admin" and password == "1234":
        messagebox.showinfo("Login", "Login successful! Welcome :)")
    else:
        messagebox.showwarning("Login Failed", "Invalid credentials. Please try again.")

tk.Button(root, text="Login", command=login).pack(pady=10)

root.mainloop()
