

import numpy as np
a=eval(input("Input size of square co-efficent matrix:"))
c=1
matrix=[]
vector=[]

for i in range(a):
    r=1
    column=[]
    for i in range (a):
        print("Enter values of column",c,) 
        x=eval(input())
        column.append(x)
        r=r+1
    c=c+1
    matrix.append(column)
    print("Your column=",matrix)

matrix=np.asarray(matrix)
print("Your Matrix Origina:",matrix)
matrix=np.transpose(matrix)
print("Requied Matrix=",matrix)
vector=np.zeros(a)
print(vector)
new_vector=[]
for i in vector:
    new_vector.append([i])
new_vector=np.array(new_vector)
aug=np.append(matrix,new_vector,axis=1)
print("Augmented Matrix:",aug)

def row_interchange(mat,row1,row2):
        t1=mat[row1].copy()
        t2=mat[row2].copy()
        mat[row1]=t2
        mat[row2]=t1
        return mat

def scalar_mul(mat,scalar):
    return mat*scalar

def row_add(mat,vect,rownum):
    mat[rownum]=mat[rownum]+vect
    return mat

for i in range(0,a):
        for j in range(i+1,a):
            ratio=aug[j][i] / aug [i][i]
            mul_result=scalar_mul(aug[i],ratio)
            print("Mul_Result",mul_result)
            aug=row_add(aug,-mul_result,j)
            print("My NEw Aug=",aug)

ans2=np.zeros(a)
ans2[a-1]=aug[a-1][a]/aug[a-1][a-1]

for i in range(a-2,-1,-1):
    ans2[i]=aug[i][a]
    for j in range(i+1,a):
        ans2[i]=ans2[i]/aug[i][i]

print("\n Requied Solution is:")


for i in range(len(ans2)):
    print("Value of X[",i+1,"]=",np.round(ans2[i],2),end="\t")
if ans2.all()==0:
    print("\n Your Given Vector From Space ",a,"X",a,"LinerLY Independent")
else:
    print("\n Your Given Vector From Space ", a, "X", a, "+LinerLY Dependent")


