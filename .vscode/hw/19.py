# data.csv를 불러와서 기초 통계를 계산하는 프로그램

import pandas as pd

df=pd.read_csv(r"C:\Users\jhroh\OneDrive\rokey\data.csv",sep=r'\s+')
print(df)

print(df['Age'].mean(),df['Salary'].mean())
print(df['Age'].max(),df['Salary'].max())
print(df['Age'].min(),df['Salary'].min())



#  30세 이상, 연봉  60000 이상인 사람만 필터링
filtered=df[(df['Age']>=30) & (df['Salary']>=60000)]
print(filtered)


import numpy as np
arr=np.array(range(1,11))
print("원본배열:", arr)
print("제곱배열:", arr**2)
print(arr.mean(),arr.max(),arr.min())



import numpy as np
random=np.random.rand(3,4)
print(random)
print("각 행의 최댓값:", random.max(axis=1))



import matplotlib.pyplot as plt
x=range(1,6)
y=[2,4,6,8,10]
plt.plot(x,y)
plt.grid()
plt.title("line plot")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.xlim(1,5)
plt.ylim(2,10)
plt.show()
