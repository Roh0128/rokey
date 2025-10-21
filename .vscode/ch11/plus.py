import tkinter as tk
oroot=tk.Tk()
oroot.geometry("200x200")
coffee={0:'아메리카노',1:'라떼',2:'카프치노',3:'에스프레소'}

check_value={}
for i in range(len(coffee)):
    check_value[i]=tk.BooleanVar()
    ocheckbutton= tk.Checkbutton(oroot,text=coffee[i],variable=check_value[i])#onvalue, offvalue
    ocheckbutton.pack(anchor='s')

def buy():
    for i in check_value:
        print(i)
        if check_value[i].get()==True:
            print(coffee[i])

tk.Button(oroot,text='주문',command=buy).pack()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
oroot.mainloop()


