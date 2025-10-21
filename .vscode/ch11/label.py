from tkinter import Tk
from tkinter import Label
from tkinter import Entry
from tkinter import StringVar

otk=Tk()
otk.geometry("400x300")

olabel1=Label(otk,text='적',bg='red',width=20).pack()
olabel2=Label(otk,text='녹',bg='green',width=20).pack()
olabel3=Label(otk,text='파',bg='blue',width=20).pack()

ostring=StringVar()
oentry=Entry(otk, textvariable=ostring).pack()

otk.mainloop()

