from tkinter import *
oroot=Tk()
oroot.geometry("200x100")

obtn1=Button(oroot,text='push1')
obtn2=Button(oroot,text='push2')
obtn3=Button(oroot,text='push3')

obtn1.grid(row=1,column=0)
obtn2.grid(row=2,column=1)
obtn3.grid(row=0,column=4)
# pack(side='left') ,(side='right') , top, bottom
# place(x=10,y=60)
oroot.mainloop()

