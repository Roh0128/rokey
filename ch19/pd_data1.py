import pandas as pd


data={
    'id':[1,2,3],
    'name':['alice','bob','charlie'],
    'age':[30,26,22]
}
df=pd.DataFrame(data)

print(df)
print("----------------------   ")

df['salary']=[1000,20000,30000] #새로운 컬럼 추가

df.loc[3]=[4,'david',40,40000]  #새로운 행 추가
df.loc[len(df)]=[5,'eva',34,500000] #새로운 행 추가


# 행 삭제, 행 번호 주의
df=df.drop(1) #인덱스 1 행 삭제 
print(df)



print("데이터 연결 ------------------")
data2={
    'id':[6,7],
    'name':['frank','grace'],
    'age':[29,31],
    'salary':[60000,70000]
}
df2=pd.DataFrame(data2)
concated=pd.concat([df,df2])
print(concated)

# print("인덱스 재설정 ------------------")
# reseted=concated.reset_index(drop=True) #인덱스 재설정
# print(reseted)

print("데이터 병합------------------ ")

data3={
    'id':[1,2,3,4,5],
    'dept':['영업','개발','기획','인사','총무']
}
df3=pd.DataFrame(data3)
merged=pd.merge(df,df3) #inner, outer, left, right
print(merged)

print(merged.isnull().sum()) #컬럼별 null 값 개수

meanVal=merged['salary'].mean() #평균값
merged['salary']=merged['salary'].fillna(meanVal) #null 값을 평균값으로 대체
print(merged)

print('중복 제거------------------------')
data4={
    'id':[1,2,2,3,4,4,5],
    'name':['alice','bob','bob','charlie','david','david','eva'],
    'age':[30,26,26,22,40,40,34],
    'salary':[1000,20000,20000,30000,40000,40000,500000]
}
df4=pd.DataFrame(data4)
print(df4)
df1_=pd.concat([merged,df4])
print(df1_)
print(df4.duplicated) #중복 여부 불리언 시리즈
df1_=df1_.drop_duplicates() #중복 행 제거
print(df1_)