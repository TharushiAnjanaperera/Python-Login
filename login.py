from subprocess import call
from tkinter import Tk, Label, Entry, Frame
from tkinter import *
import mysql.connector
import MySQLdb 
from tkinter import messagebox

root = Tk()
root.title('Login')
root.geometry('825x500+300+200')
root.config(bg="#fff")
root.resizable(False, False)



def OK():
    try:
        mysql = MySQLdb.connect(host="localhost", user="root", password="1234", database="login")
        mycursor = mysql.cursor()
        username = user.get()
        password = code.get()

        sql = "SELECT * FROM users WHERE username = %s AND password = %s"
        mycursor.execute(sql, (username, password))
        results = mycursor.fetchall()

        if results:
            messagebox.showinfo("", "Login Success")
            root.destroy()
            call(["python", "main.py"])
        else:
            messagebox.showinfo("", "Login Unsuccessful")

    except MySQLdb.Error as err:
        messagebox.showerror("Error", f"Database connection error: {err}")


img = PhotoImage(file='login4.png')
Label(root, image=img, bg='white').place(x=100, y=100)

frame = Frame(root, width=350, height=350, bg="white")
frame.place(x=400, y=70)

heading = Label(frame, text="Sign in", fg="#57a1f8", bg="white", font=('arial', 23, 'bold'))
heading.place(x=100, y=5)

def on_enter(e):
    user.delete(0, 'end')

def on_leave(e):
    name = user.get()
    if name == '':
        user.insert(0, 'Username')

user = Entry(frame, width=25, fg="black", border=0, bg="white", font=('arial', 11))
user.place(x=30, y=80)
user.insert(0, 'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

def on_enter(e):
    code.delete(0, 'end')

def on_leave(e):
    name = code.get()
    if name == '':
        code.insert(0, 'Password')

code = Entry(frame, width=25, fg="black", border=0, bg="white", font=('arial', 11))
code.place(x=30, y=150)
code.insert(0, 'Password')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

Button(frame, width=39, pady=7, text="Sign in", bg='#57a1f8', fg="white", border=0, command=OK).place(x=35, y=204)
lable = Label(frame, text="Don't have an account?", fg="black", bg="white", font=('arial', 9))
lable.place(x=75, y=270)

sign_up = Button(frame, width=6, text='Sign up', border=0, bg='white', cursor='hand2', fg='#57a1f8')
sign_up.place(x=215, y=270)

root.mainloop()
