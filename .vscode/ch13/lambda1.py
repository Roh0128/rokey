# def 함수명(매개1,매개2, ...):
#     코드블럭
#     return 반환값
def funcA(x):
    return x+x
print(funcA(1))
print(funcA(2))
print(funcA(3))

add= lambda x: x+x
print(add(3))
# 여러 줄로 나눌수 없다

adder=lambda x,y:x+y # x,y=5:x+y 기본값을 줄수 있어
print((lambda x,y: x*y)(3,4))