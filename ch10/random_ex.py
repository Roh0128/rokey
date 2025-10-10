import random
animals=['cat', 'duck','bird']
print(random.choice(animals))
print(random.sample(animals,2))
# print(random.randint(1,3))

#  상속: 어떤 클래스가 다른 클래스의 성질을 물려받는것
class Car:
    def __init__(self,wheel, price):
        self.wheel=wheel
        self.price=price
car=Car(4,3000)
print(car.wheel)
print(car.price)

class Bicycle(Car):
    def __init__(self,year, wheel, price):
        super().__init__(wheel, price)
        self.year=year
bicycle=Bicycle(2021,2,1000)
print(bicycle.price)
print(bicycle.wheel)
print(bicycle.year)