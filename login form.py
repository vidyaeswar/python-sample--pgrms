from tkinter import *
root=Tk()
root.geometry()
root.configure(bg='#003e53')
title=Label(root,text="Login Form",fg="white",bg="#003e53",font=("bold",15))
title.place(x=200,y=30)
uname=(root,text="User Name",fg="white",bg="#003e53",font=("bold",15))
uname.place(x=100,y=60)
password=Label(root,text="Password",fg="white",bg="#003e53",font=("bold",15))
password.place(x=100,y=60)
root.mainloop() 

