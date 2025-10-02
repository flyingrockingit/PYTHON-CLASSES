from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

root = Tk()
root.title("Denominator Calculator")
root.configure(bg="#ADD8E6")
root.geometry("650x480")

upload = Image.open("1000 AED.jpg")
image = ImageTk.PhotoImage(upload)
label = Label(root, image=image, bg="#00308F")
label.place(x=100, y=180)

label1 = Label(root, text="Welcome to the future of technology!", bg="#4682B4")
label1.place(relx=0.5, y=340, anchor=CENTER)

def msg():
    Msgbox = messagebox.askyesno("Alert", "Do you want to proceed?")
    if Msgbox:  
        topwin()

button1 = Button(root, text="Let's get started", bg="#008080", fg="#2E5894", command=msg)
button1.place(x=260, y=360)

def topwin():
    top = Toplevel()
    top.title("Denomination Calculator")
    top.configure(bg="#4B6194")
    top.geometry("400x400")

    Label(top, text="Enter your total amount", bg="#082567", fg="white", font=("Arial", 12)).pack(pady=10)

    entry = Entry(top, font=("Arial", 12))
    entry.pack(pady=5)

    Label(top, text="Here are the number of notes you can use for each denomination", 
          bg="#005A92", fg="white", font=("Arial", 10), wraplength=350).pack(pady=10)

    l1 = Label(top, text="AED 1000", bg="#4B6194", fg="white", font=("Arial", 12))
    l2 = Label(top, text="AED 500", bg="#4B6194", fg="white", font=("Arial", 12))
    l3 = Label(top, text="AED 100", bg="#4B6194", fg="white", font=("Arial", 12))
    l4 = Label(top, text="AED 50", bg="#4B6194", fg="white", font=("Arial", 12))
    l5 = Label(top, text="AED 20", bg="#4B6194", fg="white", font=("Arial", 12))
    l6 = Label(top, text="AED 10", bg="#4B6194", fg="white", font=("Arial", 12))
    l7 = Label(top, text="AED 5", bg="#4B6194", fg="white", font=("Arial", 12))

    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)
    t4 = Entry(top)
    t5 = Entry(top)
    t6 = Entry(top)
    t7 = Entry(top)

    def calculator():
        try:
            global amount 
            amount = int(entry.get())

            note1000 = amount // 1000
            amount %= 1000

            note500 = amount // 500
            amount %= 500

            note100 = amount // 100
            amount %= 100

            note50 = amount // 50
            amount %= 50

            note20 = amount // 20
            amount %= 20

            note10 = amount // 10
            amount %= 10 

            note5 = amount // 5

            t1.delete(0, END)
            t2.delete(0, END)
            t3.delete(0, END)
            t4.delete(0, END)
            t5.delete(0, END)
            t6.delete(0, END)
            t7.delete(0, END)

            t1.insert(0, note1000)
            t2.insert(0, note500)
            t3.insert(0, note100)
            t4.insert(0, note50)
            t5.insert(0, note20)
            t6.insert(0, note10)
            t7.insert(0, note5)

        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number")

    btn = Button(top, text="Calculate", command=calculator, bg="dark grey", fg="white")
    btn.place(x=240, y=120)

    l1.place(x=140, y=170)
    entry.place(x=200, y=80)

    l1.place(x=140, y=170)
    l2.place(x=140, y=200) 
    l3.place(x=140, y=230)
    l4.place(x=140, y=260)
    l5.place(x=140, y=290) 
    
    t1.place(x=240, y=170)
    t2.place(x=240, y=200)
    t3.place(x=240, y=230)
    t4.place(x=240, y=260)
    t5.place(x=240, y=290)
    l6.place(x=140, y=320)
    l7.place(x=140, y=350)
    t6.place(x=240, y=320)
    t7.place(x=240, y=350)

    top.mainloop ()
root.mainloop()
