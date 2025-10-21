import tkinter as tk

# 1. 계산을 위해 피자 이름과 가격을 분리해서 저장 (데이터 구조 개선)
pizza_data = [
    {"name": "치즈피자", "price": 3200},
    {"name": "콤비네이션피자", "price": 3500},
    {"name": "불고기피자", "price": 3600}
]

# --- 10번 문제의 핵심: 주문 버튼을 눌렀을 때 실행될 함수 ---
def process_order():
    """
    체크된 피자들을 확인하고, 주문 내역과 총 가격을 계산하여
    결과 레이블(result_label)에 텍스트를 업데이트하는 함수.
    """
    selected_pizzas = []  # 선택된 피자 이름과 가격을 담을 리스트
    total_price = 0       # 총가격을 계산할 변수

    # 모든 체크박스를 하나씩 확인
    for i in range(len(pizza_data)):
        # check_vars[i]의 .get() 값이 True이면 (체크되었으면)
        if check_vars[i].get():
            pizza = pizza_data[i]
            selected_pizzas.append(f"- {pizza['name']} ({pizza['price']}원)")
            total_price += pizza['price']
    
    # 화면에 표시할 최종 결과 문자열 생성
    if not selected_pizzas:
        # 아무것도 선택하지 않았을 경우
        result_text = "피자를 선택해주세요."
    else:
        # 선택한 내역을 줄바꿈으로 합쳐서 보기 좋게 만듦
        order_details = "\n".join(selected_pizzas)
        result_text = f"주문내역:\n{order_details}\n\n총 가격: {total_price}원"
    
    # 결과 레이블의 텍스트를 위에서 만든 결과 문자열로 변경
    result_label.config(text=result_text)


# --- GUI 윈도우 설정 ---
oroot = tk.Tk()
oroot.geometry("400x400")
oroot.title("조각 피자 주문 프로그램")
tk.Label(oroot, text="피자").pack(pady=10)


# --- 체크박스 생성 ---
# 각 체크박스의 상태(True/False)를 저장할 딕셔너리
check_vars = {}
for i, pizza in enumerate(pizza_data):
    check_vars[i] = tk.BooleanVar()
    # 화면에 표시될 텍스트 (예: "치즈피자 (3200원)")
    display_text = f"{pizza['name