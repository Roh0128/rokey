from sklearn import svm
from sklearn import metrics
import pandas as pd

# 알고리즘 관련
# 행렬, 정답률 관련
# 데이터 조작 관련

# 데이터 준비(입력) - 지도 학습(데이터/정답)
xor_data = [
    # P, Q, result
    [0, 0, 0],
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 0]
]

# 데이터 가공 - 학습을 위해 데이터와 레이블 분리
xor_df = pd.DataFrame(xor_data)  # 매개변수: 입력 데이터

# xor_df.loc[전체데이터, 추출할데이터]
# 학습 데이터
data = xor_df.loc[:, 0:1]
# 레이블(정답)
label = xor_df.loc[:, 2]

# 학습 알고리즘- 분류
# 모델 생성
clf=svm.SVC()
clf.fit(data,label)

pre=clf.predict(data)
print("예측결과:",pre)

ac_score=metrics.accuracy_score(label,pre)
print("정답률:",ac_score)
