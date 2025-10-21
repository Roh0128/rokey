def funca(na,nb):
    temp=na
    na=nb
    nb=temp

a=[1,2]
b=a
a.append(3)
print(id(a))
print(id(b))

def funca(cb): 
    temp=cb[0]
    cb[0]=cb[1]
    cb[1]=temp

ca=[1,2]
funca(ca)
print(ca)
print(id(ca))

a=[10,11,12,13]
print("list a:",a)
print(id(a))
print(id(a[0]))
print(id(a[1]))
print(id(a[2]))
print(id(a[3]))

a[1]=20
print("list a:",a)
print(id(a))
print(id(a[0]))
print(id(a[1]))
print(id(a[2]))
print(id(a[3]))

b=a # b는 a가 가리키는 주소를 복사
b=[30,40] # b가 가리키는 주소를 새로 생성

def fk(cb):
    total=0
    for sb in range(0,3,1):
        total=total+cb[sb]
    cb[2]=total

ca=[10,20,30]
print(ca)
cd=fk(ca)
print(cd)
ca[1]=100
print(ca)
print(cd)

# fids_max.py
def find_max(num_list):
    max_value=num_list[0]
    for num in num_list:
        if num>max_value:
            max_value=num
    return max_value

# selectsorting.py
ca=[20,10,30,50,40]
print("정렬 전:",ca)

mina=ca[0]
minix=0
for sb in range(1,5,1):
    if mina > ca[sb]:
        mina=ca[sb]
        minix=sb

temp=ca[0]
ca[0]=ca[minix]
ca[minix]=temp

mina=ca[1]
minix=1
for sb in range(2,5,1):
    if mina > ca[sb]:
        mina=ca[sb]
        minix=sb
ca[1],ca[minix]=ca[minix], ca[1]

mina=ca[2]
minix=2
for sb in range(3,5,1):
    if mina> ca[sb]:
        mina=ca[sb]
        minix=sb
ca[2],ca[minix]=ca[minix], ca[2]

mina=ca[3]
minix=3
for sb in range(4,5,1):
    if mina> ca[sb]:
        mina=ca[sb]
        minix=sb
ca[3],ca[minix]=ca[minix],ca[3]
print("정렬 후:",ca)


su=[5,4,7,16]
print("작업 전:",su)
def fmax(cb):
    max=cb[0]
    for sb in range(1,len(cb)):
        if max<cb[sb]:
            max=cb[sb]
    return max
a= fmax(su)
print("가장 큰 수:",a)

mina=ca[3]

for s in range(0,len(ca)):
    mina=ca[s]
    minix=s
    for sb in range(s,5,1):
        if mina> ca[sb]:
            mina=ca[sb]
            minix=sb
    ca[s],ca[minix]=ca[minix],ca[s]

print("정렬 후:",ca)

def fselsort (ca):
    for s in range(0,len(ca)-1):
        mina=ca[s]
        minix=s
        for sb in range(s,5,1):
            if mina> ca[sb]:
                mina=ca[sb]
                minix=sb
        ca[s],ca[minix]=ca[minix],ca[s]
    return ca
print("정렬 후:",ca)
print(len(ca))



