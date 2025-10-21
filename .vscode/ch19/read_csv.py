# 줄바꿈으로 구분되는 1개 이상의 행으로 구성
# 각 행은 1개 이상의 열로 구성
# 필드는 큰따옴표로 둘러싸도 됨

import pandas as pd

path=r"C:\Users\jhroh\OneDrive\rokey\ch19\data.csv"

df_csv=pd.read_csv(path)

print(df_csv)
print(type(df_csv))


import openpyxl

path=r"C:\Users\jhroh\OneDrive\rokey\ch19\products.xlsx"
df_xl=pd.read_excel(path)
print(df_xl)
print(type(df_xl))


print("----------------------")

print(df_csv.head()) #처음 5행
print(df_csv.tail()) #마지막 5행
print(df_csv.info()) # 데이터 요약 정보

print(df_csv.describe()) #기술 통계 요약

print(df_csv.sample(2)) #랜덤 2행
print(df_csv.sample(frac=0.3)) #랜덤 30% 행


