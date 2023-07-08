import numpy as np
a=eval(input("INput size of The Space:"))
b=eval(input("Input Number of Vectores:"))
c=1
matrix=[]
vector=[]
for i in range(b):
    r=1
    column=[]
    for i in range(a):
        print("Enter Value of Column:",c)
        x=eval(input())
        column.append(x)
        r=r+1
    c=c+1
    matrix.append(column)
matrix=np.asarray(matrix)
matrix=np.transpose(matrix)
print(matrix)
aug=np.copy(matrix)

##################################################################

def row_interchange(mat,row1,row2):
    t1=mat[row1].copy()
    t2=[row2].copy()
    mat[row1]=t2
    mat[row2]=t1
    return mat

##################################################################

def scalar_mul(mat,scalar):
    return mat*scalar

#################################################################

def row_add(mat,vect,rownum):
    mat[rownum]=mat[rownum]+vect
    return mat


#################################################################

for i in range(0,b):
        for j in range(i+1,a):
            ratio=aug[j][i] / aug [i][i]
            mul_result=scalar_mul(aug[i],ratio)
            print("Mul_Result",mul_result)
            aug=row_add(aug,-mul_result,j)
            print("My NEw Aug=",aug)

#################################################################

for i in range(a):
    for j in range(b):
        if aug[i][j]!=0:
            print("youR Vector:",matrix[:,j])
            break




