
#using inverse mathode
import numpy as np
n=eval(input("Enter The size of the matrix="))
r=1
matrix=[]
while r<=n:
    c=1
    row=[]
    while c<=n:
        print("enter the value of row",r,"column",c)
        x=eval(input())
        row.append(x)
        c=c+1
    matrix.append(row)
    r=r+1
m=np.asarray(matrix)
print("coefficient  matrix is=",m)
n5=np.linalg.det(m)
print("determinant of matrix is ",n5)
m7=np.linalg.inv(m)
print("invers of the matrix is",m7)
vtr1=[]
c=1
while c<=n:
    print("plesas enter the constant of equation")
    x=eval(input())
    vtr1.append(x)
    c=c+1
vtr2=np.asarray(vtr1)
ans=np.dot(m7,vtr2)
print(ans)

for i in range(len(ans)):
    print("value of x [",i+1,"]=",np.round(ans[i],2))