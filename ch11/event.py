import tkinter as tk
def order():
    print("주문하세여")

root=tk.Tk()
btn=tk.Button(root,text='주문',command=order)
btn.pack()
root.mainloop()