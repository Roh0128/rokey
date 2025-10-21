from tkinter import *

otk=Tk() # 부모 윈도우(위젯)
otk.geometry("100x150+1300+400")
obtn1=Button(otk, text="PUSH1").pack()
obtn2=Button(otk,text="PUSH2").pack()
obtn3=Button(otk, text="PUSH3").pack()

Label(otk, text="빨강", bg="red", width=20).pack() #텍스트를 화면에 출력하기 위해 사용
Label(otk, text="초록", bg="green", width=20).pack()
Label(otk, text="파랑", bg="blue", width=20).pack()

otk.mainloop()