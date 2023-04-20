activities=['eat','sleep','code','play'] #defining labels
slices=[3,6,8,7] #portion covered by each label
colors=['r','m','c','g']
plt.pie(slices,labels=activities,colors=colors,startangle=90,shadow=True,explode=(0,0,0.1,0),radius=1.2,autopct='%1.1f%%')
plt.legend()
plt.show()
