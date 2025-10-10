class Bag:
    def __init__(self):
        self.data=[]
    def add(self,x):
        self.data.append(x)
    def addtwice(self,x):
        self.add(x)
        self.add(x)

handbag=Bag()
print(handbag.data)
handbag.add("wallet")
handbag.add("battery")
print(handbag.data)

class Car:
    # 붕어빵 틀의 특징 (클래스 멤버)
    maker = "Hyundai"  # 제조사 (모든 차가 공유)
    car_count = 0      # 총 생산 대수 (모든 차가 공유)

    # 붕어빵의 특징 (인스턴스 멤버)
    def __init__(self, color):
        # self.변수 => 인스턴스 변수
        self.color = color  # 색상은 차마다 다름
        self.speed = 0      # 현재 속도도 차마다 다름
        
        # 새 차가 만들어질 때마다 클래스 변수를 1 증가시킴
        Car.car_count += 1

    # 인스턴스 메서드 (self가 있음)
    def accelerate(self):
        # self.speed => '나(이 인스턴스)'의 속도를 올린다.
        self.speed += 10
        print(f"{self.color} 자동차의 속도가 {self.speed}km/h가 되었습니다.")

    # 클래스 메서드 (self가 없음)
    @classmethod
    def get_car_count(cls):
        # cls는 클래스 자체(Car)를 의미함
        print(f"지금까지 총 {cls.car_count}대의 차가 만들어졌습니다.")

# --- 실행 코드 ---
# 붕어빵 찍어내기
car1 = Car("빨간색")
car2 = Car("파란색")

# 인스턴스 멤버는 각자 다름
car1.accelerate()  # 빨간색 차의 속도만 올라감
car2.accelerate()  # 파란색 차의 속도만 올라감

# 클래스 멤버는 모두가 공유함
print(f"car1의 제조사: {car1.maker}")
print(f"car2의 제조사: {car2.maker}")

# 클래스 메서드 호출 (인스턴스 없이, 클래스 이름으로 바로 호출)
Car.get_car_count()

class Cadd():
    def fadd(self,a=1,b=2):
        self.x=a
        self.y=b
        self.hap=self.x+self.y
obj=Cadd()
obj.fadd(10,20)


# init 함수
class Human:
    def __init__(self,age,name):
        self.age=age
        self.name=name
    def intro(self):
        print(self.age,self.name)
kim=Human(29,"노덩현")
kim.intro()

class Car:
    def __init__(self,pnum,pspeed):
        self.num=pnum
        self.speed=pspeed
new_car=Car(2923,90)
print("차량 번호", new_car.num)
print("speed",new_car.speed)

class Cadd:
    def fadd(self,a=1,b=2):
        self.x=a
        self.y=b
        self.hap=self.x+self.y
obj=Cadd()
obj.fadd(10,20)
print(obj.hap)

stra= 'abc' 
print(stra)
print(type(stra))
strb=stra.capitalize()
print(strb)

class Fruit:
    def __init__(self,name,color):
        self.name=name
        self.color=color
        print("과일 이름:",name,"색깔:",color)
    def taste(self):
        if self.name=="오렌지":
            print("새콤하다.")
orange=Fruit("오렌지","노란색")
orange.taste()

class Bag:
    def __init__(self,x):
        self.data=[x]
    def add(self,x):
        self.data.append(x)
    