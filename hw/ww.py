import tkinter as tk
oroot=tk.Tk()
oroot.geometry("1200x1400")
oroot.title("조각 피자 주문 프로그램")
tk.Label(oroot,text="피자").pack(pady=20)

pizza_list={0:"치즈피자(3200원)",1:"콤비네이션피자(3500원)",2:"불고기피자(3600원)"}

check_value={}
for i in range(len(pizza_list)):
    check_value[i]=tk.BooleanVar()
    check_=tk.Checkbutton(oroot,text=pizza_list[i],variable=check_value[i])
    check_.pack(anchor='w')

oroot.mainloop()