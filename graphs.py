import numpy as np
import matplotlib.pyplot as plt

# ypoints = np.array([3, 8, 1, 10, 5, 7])
# plt.plot(ypoints)
# plt.show()
#
# x1=np.array([1,2,6,8])
# y1=np.array([20,30,40,50])
#
# plt.title("DINGA CHIBA GRAPH")
# plt.xlabel("X-Axis")
# plt.ylabel("Y-Axis")
# plt.plot(x1,y1)
# plt.grid()
# plt.show()

# x=np.random.normal(21,12,54)
# plt.hist(x)
# plt.show()

xpoints=np.arange(0,4*np.pi,0.4)
ypoints=np.sin(xpoints)
zpoints=np.cos(xpoints)

plt.plot(ypoints,zpoints)
plt.grid()
plt.show()

# xpoints1=np.arange(0,4*np.pi,0.1)
# ypoints1=np.cos(xpoints)
#
# xpoints2=np.arange(0,4*np.pi,0.1)
# ypoints2=np.tan(xpoints)
#
# xpoints3=np.arange(0,4*np.pi,0.1)
# ypoints3=np.sinh(xpoints)
#
# xpoints4=np.arange(0,4*np.pi,0.1)
# ypoints4=np.cosh(xpoints)
#
# xpoints5=np.arange(0,4*np.pi,0.1)
# ypoints5=np.tanh(xpoints)



