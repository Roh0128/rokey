import tkinter as tk

root = tk.Tk()
root.title("Radiobutton")
root.geometry("260x180")

# 1. tk.label -> tk.Label, pady(8,0) -> pady=(8,0) 수정
tk.Label(root, text='세트 선택').pack(anchor='w', padx=8, pady=(8,0))

radio_val = tk.IntVar()
radio_val.set(1) 
lunch = {0:"김밥", 1:"떡볶이", 2:"김치볶음밥"}

for i in lunch:
    tk.Radiobutton(root, text=lunch[i], variable=radio_val, value=i).pack(anchor='w', padx=15)

def buy():
    print(lunch[radio_val.get()])

tk.Button(root, text='주문', command=buy).pack(pady=5)
root.mainloop()