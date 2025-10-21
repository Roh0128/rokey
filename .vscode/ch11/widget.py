# from tkinter import * #모든 것을 직접 가져온다
# otk=Tk()  #부모 윈도우
# obtn=Button(otk,text="click") #버튼 위젯
# # 배치
# obtn.pack()

# # 위젯 바인딩
# otk.mainloop()

import tkinter as tk #tkinter를 tk라는 별명으로 쓸래
def hello():
    print("hello")
# 함수 괄호없이 사용되는 경우
# 1. 변수에 저장
# 2.다른 함수에 전달하거나 반환값으로 사용 가능
room=tk.Tk()
room.title("첫 tkinter 창")
room.geometry("200x150+1300+300")
btn=tk.Button(room,text="해해",command=hello)
btn.pack()
room.mainloop()