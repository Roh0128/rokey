b=0
print("b의 값은",b)
b=1
print("b의 값은",b)
def scope_test():
    a=1
    print("scope_test() 함수 내 a값",a)
a=0
print("scope_test()함수 밖 a값",a)
scope_test()
print("scope_test() 함수 안 a값",a)


