from tkinter import *
from tkinter import messagebox

def register():
    username = username_entry.get()
    password = password_entry.get()

    if username and password:
        with open("user_data.txt", "a") as f:
            f.write(f"Username: {username}, Password: {password}\n")
        messagebox.showinfo("Registration", "Registration successful!")
        uservalue.set("")
        passvalue.set("")
    else:
        messagebox.showerror("Registration", "Please enter a username and password.")

# Create the main window
root = Tk()
root.title("Registration Page")
root.geometry("535x350")
root.minsize(535,350)
root.maxsize(535,350)
Label(root, text="Registration form ",fg="red",font="sunken 13 bold").grid(row=0,column=1)
frame =Frame(root, bg="pink",relief=RIDGE, borderwidth=3)
frame.grid(row=1,column=1,padx=40,pady=33,ipadx=55,ipady=55)#pack(pady=156,padx=240,ipadx=100)
# Create labels and entry fields

username_label = Label(frame, text="Username:",fg="red",font="sunken 10 bold")
username_label.grid(row=0,column=1,padx=5,pady=5)
passvalue = StringVar()
uservalue = StringVar()

username_entry =Entry(frame,textvariable=uservalue,width=40)
username_entry.grid(row=0,column=2,padx=5,pady=5)

password_label = Label(frame, text="Password:",fg="red",font="sunken 10 bold")
password_label.grid(row=4,column=1,padx=15,pady=15)
password_entry =Entry(frame,textvariable=passvalue,width=40)
password_entry.grid(row=4,column=2,padx=5,pady=5)

register_button = Button(frame, text="Register",fg="red",font="sunken 13 bold", command=register)
register_button.grid(row=6,column=2,padx=5,pady=20)

# Start the main event loop
root.mainloop()

# Example (Hello, World):
# import tkinter
# from tkinter.constants import *
# tk = tkinter.Tk()
# tk.minsize(400,400)
# frame = tkinter.Frame(tk, relief=RIDGE, borderwidth=8)
# frame.pack(fill=BOTH,expand=1)
# label = tkinter.Label(frame, text="Hello, World")
# label.pack(fill=X, expand=1)
# button = tkinter.Button(frame,text="Exit",command=tk.destroy)
# button.pack(side=BOTTOM)
# tk.mainloop()
