import pandas as pd
from openpyxl import Workbook, load_workbook

path=r"ch22\excel\new_example.xlsx"
df= pd.read_excel(path, sheet_name="sample Data")
print(df.head())

print("-------------------------")
# excel 파일 정보 확인
df.info()             #데이터 타입 및 개요 확인
print(df.describe())  #숫자 데이터 요약

print(df["나이"])
print(df["나이"].sum())
print(df["나이"].mean())

df["출생년도"]=2025-df["나이"]
print(df.head())


path=r"ch22\excel\new_example.xlsx"
df.to_excel(path,index=False)