import numpy as np
import matplotlib.pyplot as plt
list1=[10,20,30,40,50]
vtr1=np.array(list1)
print(vtr1)

list2=[[12],
       [15],
       [17],
       [19]]
print("Creating column vector from list")
vtr2=np.array(list2)
print(vtr2)
vtr1=np.array(list1)
print(vtr1)
list3=[11,12,15,17,20]
print("we are creating vector from the list ")
vtr3=np.array(list3)
print(vtr3)
print("Addition of vector:")
vtr_add=vtr1+vtr3
print(vtr_add)
print("subtraction of vectors:")
vtr_sub=vtr1-vtr3
print(vtr_sub)
print("Multiplication of vetors:")
vtr_mul=vtr1*vtr3
print(vtr_mul)
print("Dot Product of two vectors:")
vtr_dot=vtr1.dot(vtr3)
print(vtr_dot)
scalar_Val=6
print("any scalar multiplication with vector:")
vtr_Scalar=vtr1*scalar_Val
print(vtr_Scalar)
# create a matrix 2*3 dimesion
# create an origin point,from


start=[0,0]
u=[2,2]
v=[1,-1]
fig,ax=plt.subplots(figuresize=(6,26))
ax.quiver(start[0],start[1],u[0],u[1],color='r',scale=7)
plt.show()
ax.quiver(start[0],start[1],u[0],u[1],color='b',scale=7)
plt.show()


# start=[0,0,0]
# u=[2,2,3]
# v=[1,-1,4]
# w=[3,-1,2]
# fig,ax=plt.subplots(figsize=(16,16))
# ax.plt.axes(projection='3d')
# ax.quiver(start[0],start[1],start[2],u[0],u[1],v[0],v[1],color='b')
# ax.quiver(start[0],start[1],start[2],u[0],u[1],v[0],v[1],color='p')
# ax.quiver(start[0],start[1],start[2],w[0],w[1],w[2],color='r')
# ax.view_init([0,10])
# ax.set_Xlim([0,10])
# ax.set_ylim([0,10])
# ax.set_zlim([0,10])
# plt.show()





