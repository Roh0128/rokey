import statsmodels.api as sm
import pandas as pd

data=sm.datasets.get_rdataset('mtcars').data
print(data)

x=data['hp']
y=data['mpg']

X=sm.add_constant(x)

model=sm.OLS(y,X).fit()
print(model.summary())
# 결과 요약= 기울기/절편 확인


