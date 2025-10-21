su=[5,4,7,10,6]
print("작업 전:",su)
def fmax(a,b,c,d,e):
    max=a
    if max<b:
        max=b
    if max<c:
        max=c
    if max<d:
        max=d
    if max<e:
        max=e
    return max
a= fmax(su[0],su[1],su[2],su[3],su[4])
print("가장 큰 수:",a)
print("작업 후:",su)

def fmax(a,b,c,d,e):
    fu=[a,b,c,d,e]
    max=fu[0]
    if max<fu[1]:
        max=fu[1]
    if max<fu[2]:
        max=fu[2]
    if max<fu[3]:
        max=fu[3]
    if max<fu[4]:
        max=fu[4]
    return max

def fmax(a,b,c,d,e):
    fu=[a,b,c,d,e]
    max=fu[0]
    for i in range(1,5):
        if max<fu[i]:
            max=fu[i]
    return max
def fmax(a,b,c,d,e):
    fu=[a,b,c,d,e]
    max=fu[0]
    for sfu in fu:
        if max<sfu:
            max=sfu
    return max
    # max=fu[0]
    # if max<fu[1]:
    #     max=fu[1]
    # if max<fu[2]:
    #     max=fu[2]
    # if max<fu[3]:
    #     max=fu[3]
    # if max<fu[4]:
#     max=fu[4]
    # return max
    def fmin(fu):
        min=fu[0]
        for sfu in fu:
            if min>sfu:
                min=sfu
        return min
    
    # 딕셔너리를 매개변수로 사용하는 코드
dic={1:'월',2:'화',3:'수',4:'목',5:'금',6:'토',7:'일'}
x=dic
x[1]='Monday'
print(dic)
def fch(a):
    a[2]='tueday'
fch(x)
print(dic)