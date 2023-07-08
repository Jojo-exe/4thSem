import numpy as np
import matplotlib.pyplot as plt
# Step1-Give Domain
# marker-size=increse points
# line-width=thicks the line
# Step2-define funcion
# Step3-plot
# Step4-show

x1=np.arange(-20,20,0.5)
x2=np.arange(2,20,.02)
y1=x1**2
y2=np.sin(x2)

plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Random Graph")
plt.plot(x1,y1,'0',markersize=8,linewidth=2,color='black')
plt.show()
plt.grid()

# plt.xlabel("x-axis")
# plt.ylabel("y-axis")
# plt.title("Random Graph")
# plt.plot(x2,y2,'bo--')
# plt.show()
# plt.grid()




# plt.plot(x1,y1,"*--")
# plt.show()
# plt.grid()
#
# plt.plot(x2,y2,'ro--')
# plt.show()
# plt.grid()
#
# plt.plot(x2,y2,'bo--')
# plt.show()
# plt.grid()
