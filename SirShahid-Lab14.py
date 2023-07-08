#code for translation and rotation transformation
import numpy as np
import matplotlib.pyplot as plt

x=[-9,-9,-10,-10,-7,-7,-7,-6,-6,-7,-7,-4,-4,-5,-5,-4,-4,-5,-5,-4,-4,-2,-2,-5,-5,-6,-6,-8,-8,-9]
y=[-2,0,0,3,3,6,7,7,6,6,7,7,7,7,7,6,6,7,6,6,3,3,0,0,-2,-2,0,0,-2,-2]

print(len(x))
print(len(y))
x=np.asarray(x)
y=np.asarray(y)

plt.fill(x,y,color="Red",alpha=0.7)
plt.scatter(x,y,color="blue",alpha=1)
plt.xticks(np.arange(-30,30,1))
plt.yticks(np.arange(-30,30,1))

# t=np.array([[-1,0],[0,1]])   #y-axis
# t=np.array([[1,0],[0,-1]])   #X-axis
t=np.array([[-1,0],[0,-1]])   #X-axis

new_points_x=[]
new_points_y=[]
for i in range(len(x)):
    p_t=np.dot(t,[x[i],y[i]])
    new_points_x.append(p_t[0])
    new_points_y.append(p_t[1])
plt.fill(new_points_x,new_points_y,color="green", alpha=1)
plt.grid(color="black", linestyle="-." ,linewidth=0.4)

plt.show()
