from tkinter import Tk
from tkinter import Button
from tkinter import Radiobutton
from tkinter import Label
from tkinter import IntVar

def order():
    value = radio_value.get()
    # 아무것도 선택하지 않은 경우(-1)를 처리
    if value == -1:
        print("메뉴를 선택해주세요!")
    else:
        print(f"주문하신 메뉴: {lunch[value]}")

lunch = {0:"김밥", 1:"김치찌개", 2:"떡볶이"}

# 윈도우 생성
otk = Tk()
otk.title("분식집 주문")
otk.geometry("200x200")

# 라디오 버튼의 선택값을 저장할 변수 생성
radio_value = IntVar()
radio_value.set(-1) # 초기값 -1로 설정하여 아무것도 선택되지 않은 상태로 시작

# --- 위젯 생성 ---
otklabel = Label(otk, text="분식집 메뉴")
orb1 = Radiobutton(otk, text=lunch[0], variable=radio_value, value=0)
orb2 = Radiobutton(otk, text=lunch[1], variable=radio_value, value=1)
# 'radid_value' -> 'radio_value'로 오타 수정
orb3 = Radiobutton(otk, text=lunch[2], variable=radio_value, value=2) 
obtn = Button(otk, text='주문', command=order)

# --- 위젯 배치 (화면에 보일 순서대로 배치하는 것이 좋음) ---
otklabel.pack(side='top', pady=5)
orb1.pack(anchor="w")
orb2.pack(anchor="w")
orb3.pack(anchor="w")
obtn.pack(pady=10)

otk.mainloop()