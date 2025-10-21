import seaborn as sns
import matplotlib.pyplot as plt

iris=sns.load_dataset("iris")

sns.boxplot(data=iris,
            x='species',
            y='sepal_length',)

plt.title("Boxplot example")

plt.show()

