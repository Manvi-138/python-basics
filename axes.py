import matplotlib.pyplot as plt
fig=plt.figure()
ax=fig.add_axes([0,0,0.8,1])
names=["Manvi","Naresh","Shubham","Ritu"]
age=[21,20,21,21]
ax.bar(names,age,color='g')
plt.show()
