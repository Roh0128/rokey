import tkinter as tk
oroot=tk.Tk()
oroot.geometry("1200x1100")
img1=tk.PhotoImage(file=r"C:\Users\jhroh\Downloads\freepik__the-style-is-candid-image-photography-with-natural__60420.png")

img_label=tk.Label(oroot,image=img1)
img_label.place(x=-20,y=-20)
obtn1= tk.Button(oroot,text='push1')
obtn2= tk.Button(oroot,text='push2')
obtn3= tk.Button(oroot,text='push3')
obtn1.pack()
obtn2.pack()
obtn3.pack()
oroot.mainloop()
