# 6. 리스트에서 첫 번째 짝수와 마지막 홀수를 찾아 서로 스왑하는 프로그램을 작성하시오.
a = [3, 6, 7, 4, 9, 10, 13]
first=0
x=a[0]
for i in range(len(a)):
      x=a[i]
      if  x%2==0:
         first=i 
         break
last=0
for j in range(len(a)-1,-1,-1):
     x=a[j]
     if x%2!=0:
          last=j
          break
a[first],a[last]=a[last],a[first]
print(a)
# 7. 리스트에서 가장 큰 수와 가장 작은 수를 찾아 서로 스왑하는 프로그램을 작성하시오.
a = [3, 6, 7, 4, 9, 10, 13]
maxi=0                  
min=0
x=a[0]
for i in range(len(a)):

        x=a[i]
        if  x>a[maxi]:
             maxi=i
for j in range(len(a)):
        x=a[j]
        if  x<a[min]:
             min=j

a[maxi],a[min]=a[min],a[maxi]
print(a)  
      
         
