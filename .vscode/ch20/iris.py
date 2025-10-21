from sklearn.datasets import load_iris
iris= load_iris()
# print(iris)

import pandas as pd

df=pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['target']=iris.target

target_names={
    0:iris.target_names[0],
    1:iris.target_names[1],
    2:iris.target_names[2]
}
df['target']=df['target'].map(target_names)

print(df.head())

from sklearn.model_selection import train_test_split

iris_data=df[[
    "sepal length (cm)",
    "sepal width (cm)",
    "petal length (cm)",
    "petal width (cm)"
]]
iris_label=df['target']

print(iris_data)
print(iris_label)
#  학습 전용 데이터와 테스트 전용 데이터 분리
train_data, test_data, train_label, test_label= \
train_test_split(iris_data,iris_label)

from sklearn import svm
from sklearn import metrics
clf=svm.SVC()
clf.fit(train_data,train_label)
pre=clf.predict(test_data)
ac_score=metrics.accuracy_score(test_label,pre)
print("정답률:", ac_score)
