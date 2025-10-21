import seaborn as sns
import matplotlib.pyplot as plt

iris=sns.load_dataset('iris')

sns.histplot(data=iris,
             x='sepal_length',
             hue='species',
             kde=True)

plt.title('Histogram Example')
plt.show()

