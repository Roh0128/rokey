import pandas as pd

# 1. 이미지의 데이터를 파이썬 딕셔너리 형태로 준비합니다.
data = {
    'ID': [1, 2, 3, 4, 5],
    '이름': ['비누', '장갑', '마스크', '손수건', '볼펜'],
    '가격': [300, 150, 230, 400, 200]
}

# 2. 딕셔너리 데이터를 사용해 DataFrame을 생성합니다.
df = pd.DataFrame(data)

# 3. DataFrame을 엑셀 파일로 저장합니다.
# 파일 이름은 'products.xlsx'로 지정됩니다.
# index=False 옵션은 엑셀 파일에 불필요한 인덱스(0,1,2,3,4)가 저장되지 않게 합니다.
df.to_excel('products.xlsx', index=False)

print("엑셀 파일('products.xlsx') 저장이 완료되었습니다.")