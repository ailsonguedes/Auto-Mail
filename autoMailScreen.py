import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import Widget

color1 = '#AABD8C' #Olivine
color2 = '#E9E3B4' #Vanilla

mainScreen = Tk()
mainScreen.title("Auto Mail")
mainScreen.geometry("800x500")
mainScreen.config(bg=color1)
mainScreen.resizable(width=False, height=False)

label_userEmail = Label(mainScreen, width=20, text= "User Email", font='Times 12', bg=color2)
label_userEmail.place(x=100, y=40)
label_userPassword = Label(mainScreen, width=20, text= "User Password", font='Times 12', bg=color2)
label_userPassword.place(x=350, y=40)
label_content = Label(mainScreen, width=20, text= "Content", font='Times 12', bg=color2)
label_content.place(x=100, y=180)
label_subject = Label(mainScreen, width=20, text= "Subject", font='Times 12', bg=color2)
label_subject.place(x=100, y=120)

entry_userEmail = Entry(mainScreen, width=35, relief='sunken', font='Times 10')
entry_userEmail.place(x=100, y=70)
entry_userPassword = Entry(mainScreen, width=35, relief='sunken', font='Times 10')
entry_userPassword.place(x=350, y=70)
entry_userSubject = Entry(mainScreen, width=35, relief='sunken', font='Times 10')
entry_userSubject.place(x=100, y=150)

field=tk.Text(mainScreen,height=15,width=100,font='Times 10', relief='sunken')
field.tag_configure('tag-right', justify='right')
field.place(x=100, y=210)
mainScreen.mainloop()