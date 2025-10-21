import matplotlib.pyplot as plt

x=[1,2,3,4,5]
y=[10,20,25,30,40]
# 선 그래프
plt.plot(x,y)
plt.title("line plot")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.show()

#  막대 그래프
categories=['A','B','C']
values=[3,7,8,5]
plt.bar(categories, values)
plt.title("Bar chart")
plt.show()


# 히스토그램
data=[1,2,2,3,3,3,4,4,4,4]
plt.hist(data,bins=4,color='skyblue',edgecolor='black')
plt.title('Histogram')
plt.show()

# 산점도
x=[5,7,7,4,3,19,3,65,33]
y=[99,86,87,88,100,86,103,87,94]
plt.scatter(x,y,color='green')
plt.title('Scatter plot')
plt.show()
# 원 그래프
sizes=[215,130,245,210]
labels=['A','B','C','D']
plt.pie(sizes,labels=labels,autopct='%1,1f%%',startangle=90)
plt.title('Pie chart')
plt.show()
#  %[flags][width][.precision][type]

data=[7,8,5,6,8,9,6,7,5,8]
plt.boxplot(data)
plt.title("Box plot")
plt.show()

# linestyle:'-','--',':','-.'
# marker:'o','s','^','*'

plt.plot(x,y,color='red',linestyle='--',marker='o')
plt.title("Customized line plot")
plt.show()

plt.plot(x,y)
plt.xlim(0,6)
plt.ylim(0,50)
plt.xticks(range(1,5))
plt.yticks(range(0,41))
plt.title("Customized axis limits")
plt.show()

x=[1,2,3,4]
y=[10,20,25,30]
x1=[1,2,3,4]
y2=[3,5,9,7]

plt.plot(x,y,label='Data 1')
plt.plot(x1,y2,label='Data 2')
plt.legend(loc='upper left')
plt.show()
# plt.savefig('myplot.png')

fig,axs=plt.subplots(2,2)
axs[0,0].plot(x,y)
axs[0,1].bar(categories,values)
axs[1,0].scatter(x,y)
axs[1,1].hist(data)
plt.tight_layout()
plt.show()