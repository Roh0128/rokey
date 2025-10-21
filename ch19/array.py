import numpy as np

arr=np.array([1,2,3,4,5])
print(type(arr))
print(arr)

print(arr.shape)
print(arr.dtype)

zeros=np.zeros((3,3))
print(zeros)
print("ddddddddddddddddddd" )
ones=np.ones((2,4))
print(ones) # 2행 4열

np.full((2,2),7)
print(np.full((2,2),7)) # 2행 2열, 모든 값이 7

print(np.eye(2,3)) # 직사각 단위 행렬
print(np.identity(3)) # 3x3 단위 행렬
print(np.eye(2,3),np.identity(3)) # 단위 행렬

print(np.random.rand(3,3)) # 0~1 사이의 균등 분포 난수

print(np.random.randint(1,10,(3,3))) # 1~10 사이의 정수 난수, 3x3 행렬


arr=np.array([1,2,3,4])
arr2=np.array([[1],[2],[3],[4]])
arr+5
arr*2

arr.sum()
arr.mean() #평균
arr.max()
arr.min()
result=arr+arr2
print(result)
np.dot(arr,arr2) # 행렬 곱

arr[0,:]
arr[:,2]

filtered = arr[arr > 3]

import pandas as pd
df = pd.DataFrame(arr, columns=['Value'])

#  빠른 연산, 다양한 초기화 방법, 편리한 데이터 조작 기능 제공
#  데이터 분석 및 과학 계산에 널리 사용
