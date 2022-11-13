from tkinter import *
from tkinter import ttk

win = Tk()
win.geometry("700x250")
win.title('Email Slicer')

def get_username():
   email = entry.get()
   username = email[:email.index("@")]
   return username

def get_domain():
    email = entry.get()
    domain = email[email.index("@")+1:]
    return domain
    
def get_data():
   label.config(text= "The user name is: " + get_username() + ", and the domain is: " + get_domain(), font= ('Helvetica 13'))

entry = Entry(win, width= 42)
entry.place(relx= .5, rely= .5, anchor= CENTER)


label= Label(win, text="", font=('Helvetica 13'))
label.pack()

ttk.Button(win, text= "Split Email", command= get_data).place(relx= .7, rely= .5, anchor= CENTER)

win.mainloop()
