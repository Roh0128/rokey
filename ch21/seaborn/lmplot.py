import seaborn as sns
import matplotlib.pyplot as plt

iris=sns.load_dataset('iris')

sns.lmplot(data=iris,
           x='sepal_length',
           y='sepal_width',
           hue='species',
           height=6)

plt.title("linear regression plot")
plt.show()

