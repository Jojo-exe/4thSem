# import numpy as np
#             # 0,1,2,3
# arr=np.array([[1,2,3,4],
#               [4,5,6,7],
#               [5,1,1,4]],)
# print(arr.shape)
# print(arr.size)
# print(arr.dtype)
# print(arr.max())
# print(arr.min())
# print(arr.T)
# print([0])



# importing the modules
import numpy as np
import matplotlib.pyplot as plt

# data to be plotted
x = np.arange(1, 11)
y = x * x

# plotting
plt.title("Line graph")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.plot(x, y, color ="red")
plt.show()
