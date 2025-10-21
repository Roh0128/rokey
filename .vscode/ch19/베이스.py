# pandas: 데이터 분석과 조작을 위한 파이썬 라이브러리
# csv 파일 등의 데이터를 읽고 원하는 데이터 형식으로 변환
# csv 파일은 데이터를 쉼표로 구분한 파일

# series: 1차원 배열, 라벨이 잇는 데이터
# dataframe: 2차원 배열, 행과 열로 구성된 데이터

# 행: 로우
# 열: 컬럼

# pip install pandas
import pandas as pd


data=[10,20,30]
series=pd.Series(data)
print(series)

data={'a':10,'b':20,'c':30}
series=pd.Series(data) #키를 인덱스 값으로 사용
print(series)



data=[[1,'alice',30],
      [2,'Bob',26],
      [3,'charlie',22]
      ]
df=pd.DataFrame(data, columns=['id','name','age'])
print(df)

data={
    'id':[1,2,3],
    'name':['alice','bob','charlie'],
    'age':[30,26,22]
}
df=pd.DataFrame(data)
print(df)
print(df['name']) #특정 컬럼
print(df.loc[0]) #특정 행
print(df.loc[0,'name']) #특정 행, 특정 컬럼
#  id name age
# 0 1 alice 30
# 1 2 bob   26
# 2 3 charlie 22


filtered= df[df['age']>25]
print(filtered)
# 데이터프레임 대괄호 안에 불리언 시리즈를 넣으면 트루인 행만 필터링

# 데이터 정렬
sorted=df.sort_values(by='age', ascending=False)
print(sorted)
# 데이터 정렬 (내림차순)
# 기본은 오름차순
sorted=df.sort_values(by='age')