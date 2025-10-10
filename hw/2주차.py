dic={'애플':'apple.com'}


for i in range(1,4):
    for k in range(1,10):
        print(f"{i}*{k}={i*k}")

def funca(na,nb):
    nc=na+nb
    print(na,"+",nb,nc)
    return nc


# 함수기능 print_get_number
#snake case: 소문자+_(언더바)
# camel case: 대문자+소문자
# printGetnumber

def fplusminus(arg):
    if arg>0:
        return "plus"
    elif arg<0:
        return "minus"
    
print(fplusminus(0))


def myabs (arg):
    if arg<0:
        result=arg*-1
    else:
        result=arg
    return result

# split(): 한줄에 여려개 입력받을 때


print(2)