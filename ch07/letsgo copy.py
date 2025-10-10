b=0
print("b의 값은 ",b)
b=1
print("b의 값은",b)
def scope_test():
    global a
    a=1
    print("scope_test() 함수 내 a값",a)