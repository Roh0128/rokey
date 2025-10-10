# # singer.py
# class 클래스명:
#     멤버변수명= 데이터
#     def 메서드명(self, 매개변수):
#         self.멤버변수명= 매개변수
#         return
# # 객체 생성   
# 객체명=클래스명()
# # 객체 활용
# 객체명.멤버변수명
# 객체명.메서드명()

class Singer:  
    name="아이유"
    def sing(self):
        self.name="유재석"
        return self.name+"가 노래합니다."
iu=Singer()
print(iu.name)
print(iu.sing())

# 클래스 변수: 클래스 내부에서 선언된 변수
# 인스턴스 변수: 메서드 내부에서 self.변수명으로 선언된 변수
# 클래스 메서드: 클래스 내부에서 선언된 함수
# 인스턴스 메서드: 메서드 내부에서 self를 매개변수로 선언한 함수


# 객체--Car 설계도를 바탕으로 실제 자동차 2대를 만듭니다.
my_sonata = Car()
your_avante = Car()
class Car:
    # 객체가 생성될 때 자동으로 호출되는 함수
    def __init__(self, model_name, color):
        # self.속성이름 = 값
        # "이 차의 모델명은 전달받은 model_name으로 할당해라"
        self.model = model_name
        # "이 차의 색상은 전달받은 color로 할당해라"
        self.color = color
        print(f"{self.model}({self.color}) 차량이 생산되었습니다.")

# 객체를 만들 때 __init__에 정의된 매개변수(self 제외)를 전달합니다.
my_sonata = Car("쏘나타", "파란색")
your_avante = Car("아반떼", "흰색")

class Car:
    def __int__(self, model_name,color):
        self.model=model_name
        self.color=color
    def drive (self):
        print(f"{self.model}({self.color})가 주행을 시작합니다.")

my_sonata= Car("쏘나타", "파란색")
