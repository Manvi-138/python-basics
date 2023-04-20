# import matplotlib.pyplot as plt
fig=plt.figure(figsize=(12.0,5.0))
names=["Manvi","Naresh","Shubham","Ritu"]
age=[21,20,21,21]
marks=[20,23,20,22]
birthdate=[8,13,3,10]

ax1=fig.add_subplot(131)
ax2=fig.add_subplot(132)
ax3=fig.add_subplot(133)

ax1.set_title("age")
ax2.set_title("marks")
ax3.set_title("birthdate")


ax1.set_ylabel('age')
ax2.set_ylabel('marks')
ax3.set_ylabel('birthdate')

ax1.set_xlabel('names')
ax2.set_xlabel('names')
ax3.set_xlabel('names')

ax1.bar(names,age,color='g')
ax2.bar(names,marks,color="m")
ax3.bar(names,birthdate,color="c")

plt.legend(['Data'],loc="upper right")
plt.suptitle('student data analysis')
plt.show()
