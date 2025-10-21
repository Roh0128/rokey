import matplotlib.pyplot as plt


categories=['A','B','C','D']
values=[3,7,8]

data=[7,8,5,6,8,9,6,7,5,8]
x=[1,2,3,4]
y=[10,20,25,30]
fig,axs=plt.subplots(2,2)
axs[0,0].plot(x,y)
axs[0,1].bar(categories,values)
axs[1,0].scatter(x,y)
axs[1,1].hist(data)
plt.tight_layout()
plt.show()