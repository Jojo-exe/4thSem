

import numpy as np
a=eval(input("Input the size of matrix:"))
r=1
matrix=[]
vector=[]
for i in range(a):
    c=1
    row=[]
    for i in range:
        print("Enter valur for row",r,"Column",c)
        x=eval(input())
        row.append(x)
        c=c+1
    matrix.append(row)
    print("Enter Constant value of equation",r)
    x=eval(input())
    vector.append(x)
    r=r+1
m=np.asarray(matrix)
v1=np.asarray(vector)
print("your Sqaure matrix=\n",m)
print("Your constant vector=\n",v1)
aug=np.copy(m)
new_v1=[]
for i in v1:
    new_v1.append([i])
    new_v1=np.asarray(new_v1)
print("Your Coloumn vector=\n",new_v1)
aug=np.append(aug,new_v1,axis=1)
print("Final Augemented Matrix=\n",aug)
# Scalar mul
def slr_mul(mat,s1):
    return mat*s1
# add two row
def row_add(mat,vect,rownum):
     mat[rownum]=mat[rownum]+vect
     return matrix
for i in range(0,a):
    for j in range(i+1,a):
        ratio=aug[j][i]/aug[i][i]
        mul_result=slr_mul(aug[i],ratio)
        print("Multiplication Result=",mul_result)
        aug=row_add(aug,-mul_result,j)
        print("Augmented Result \n",aug)
#         Back Substitution





