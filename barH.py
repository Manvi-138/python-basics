import matplotlib.pyplot as plt
names=['A','B','C']
values=[10,12,14]
plt.scatter(names,values,label="stars", color="red",marker="*",s=20)
plt.xlabel('names')
plt.ylabel('values')
plt.suptitle("student data")
plt.legend()
plt.show
