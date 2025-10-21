from sklearn import svm   #알고리즘
from sklearn import metrics #평가

clf=svm.SVC() # 분류 알고리즘

# fit 학습 데이터, 학습 레이블
clf.fit(
    [
        [0,0],
        [0,1],
        [1,0],
        [1,1]
    ],
    [0,1,1,0]
) #학습(모델 생성)

pre=clf.predict([
    [0,1],
    [1,1]
])

print(pre)
# 예측값
ac_score=metrics.accuracy_score([1,0],pre)
print(f"정답률: {ac_score}")

