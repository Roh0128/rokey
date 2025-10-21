import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# 샘플 데이터 셋 로드
iris=sns.load_dataset("iris")
print(iris)
print(type(iris))

# 기본 스타일 설정
sns.set_theme(style="dark")

# 그래프 표시
# sns.scatterplot(data=iris,
#                 x='sepal_length',
#                 y='sepal_width',
#                 hue='species',
#                 # style='species',
#                 )

plt.title("Iris Dataset")
# plt.show()

# set_theme()함수를 이용하여 스타일 ,팔레트 등을 설정

tips=sns.load_dataset('tips')
print(tips)

sns.set_theme(style='dark',palette='pastel')

g=sns.FacetGrid(tips,col='sex', row='time',height=3.5,aspect=0.65)
g.map_dataframe(sns.scatterplot, x='total_bill',y='tip', )
g.set_titles(row_template='{row_name}',
             col_template='{col_name}')
g.set(xlim=(0,60), ylim=(0,12))
g.savefig(r"C:\Users\jhroh\OneDrive\rokey\ch21\seaborn")
plt.show()