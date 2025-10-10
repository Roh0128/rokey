import tkinter as tk

# 1. 옵션이 변경될 때마다 실행될 함수를 정의합니다.
#    선택된 값(selection)이 자동으로 이 함수의 인자로 들어옵니다.
def on_option_change(selection):
    print(f"선택된 항목: {selection}")

root = tk.Tk()
root.geometry("600x400")
root.title("OptionMenu 이벤트 처리")

options_list = ['옵션 1', '옵션 2', '옵션 3']
selected_option = tk.StringVar()

# 초기값 설정
selected_option.set(options_list[0])

# 2. OptionMenu를 만들 때 command 옵션에 함수를 연결합니다.
option_menu = tk.OptionMenu(root, 
                            selected_option, 
                            *options_list, 
                            command=on_option_change)
option_menu.pack(pady=20)

# 프로그램 시작 시 초기값을 한 번 출력
print(f"초기값: {selected_option.get()}")

root.mainloop()