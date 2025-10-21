import matplotlib.pyplot as plt
data=[1,2,2,3,3,3,4,4,4,4]

plt.hist(data,bins=4,color='skyblue',edgecolor='black')
plt.show()

sizes=[215,130,245,210]
labels=['A','B','C','D']
plt.pie(sizes,label=labels,autopct='%1.1f%%',startangle=90, counterclock=False)
plt.title('Pie chart')
plt.show()