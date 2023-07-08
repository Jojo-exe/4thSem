# Code for Translation and Rotation
# Transformation
import numpy as np
import matplotlib.pyplot as plt
# For Arrow
x=[5,5,3,8,13,11,11]
y=[0,3,3,8,3,3,0]
# for Car
# x=[2,14,14,3,5,6,7,12,12,5,5,1]
# y=[1,1,2,2,4,5,7,9,3,3,2,2]
plt.fill(x,y,"Red",alpha=0.3)
plt.grid
# Creat Traslation MAtrix
tx=2
ty=-2
T=np.array([[1,tx],[0,ty]])
# Translate tx and ty units
points_translated_x=[]
points_translated_y=[]
print("T Matrix=",T)
print("Your list=",x,y)
for i in range(len(x)):
 p_t=np.dot(T,[x[i],y[i]])
 points_translated_x.append(p_t[0])
 print("New x=",p_t[0])
 points_translated_y.append(p_t[1])
plt.fill(points_translated_x,points_translated_y,"Gray",alpha=0.2)
#Create Rotation Matrix
theta=np.pi
R=np.array([[np.cos(theta),np.sin(theta)],[-np.sin(theta),np.cos(theta)]])
# Rotation x and y units
points_rotation_x=[]
points_rotation_y=[]
for i in range(len(x)):
 p_r=np.dot(R,[x[i],y[i]])
 points_rotation_x.append(p_r[0])
 print("New x=",p_r[0])
 points_rotation_y.append(p_r[1])
plt.fill(points_rotation_x,points_rotation_y,"Yellow",alpha=0.6)
plt.grid()
plt.show()