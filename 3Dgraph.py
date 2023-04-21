import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x=[10,2,6,8,12,14]
y=[8,10,12,13,16,17] #manually providing values without importing a csv file
z=[9,2,6,4,8,10]
 

 #file=pd.read_csv("name of file") if you want to create a graph from csv file then write this

fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')

#x==file["name of attributes in file for ex rollno"] use these steps if you are importing a csv file
#y=file["name of attribute 2"] 
#z=file["name of attribute 3"]

ax.scatter(x,y,z,c="r")
plt.xticks(rotation=60)
plt.show()
