import seaborn as sns
import matplotlib.pyplot as plt

iris=sns.load_dataset('iris')

sns.violinplot(data=iris,
               x='species',
               y='sepal_length',
               inner='quart')

plt.title('violin plot example')

plt.show()