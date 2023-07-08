import numpy as np
m=np.array([[2,9,-3,5,7],[-3,2,5,-4,4],[5,1,9,-10,4],[4,2,3,-4,3],[3,4,5,7,1]])
m1=np.asarray(m)
m2=np.linalg.inv(m)
print(m2)
vector=np.array([7,8,-1,5,2])
print(vector)
ans=np.dot(m2,vector)
print(ans)
for i in range(len(ans)):
    print("value of x[",i+1,"]=",np.round(ans[i],2))
det=[]
ans1=[]
for i in range (m):
    m3=m.copy()
    m3[:,i]=vector
    print(m3)
    d=np.linalg.det(m3)
    ans1.append(d/m2)
ans1=np.asarray(ans1)
for i in range(len(ans1)):
    print(ans1)
    print("value of x {",i + 1,"}=",np.round(ans[i],2))
