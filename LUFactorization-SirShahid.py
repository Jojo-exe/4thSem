import numpy as np
a=eval(input("Enter The size of the square of matrix="))
r=1
matrix=[] #list
for i in range(a):  #rows
    c=1
    row=[]
    for i in range(a):  #coloum
        print("enter the value of row",r,"column",c)
        x=eval(input()) #add element at the end ;of the list
        row.append(x)
        c=c+1
    matrix.append(row)
    r=r+1
m=np.asarray(matrix)
print("coefficient  matrix is=",m)
n5=np.linalg.det(m)
print("Size of matrix",m.shape)


####################################
def row_interchange(mat, row1, row2):
    t1=mat[row1].copy()
    t2 = mat[row2].copy()
    mat[row1]=t2
    mat[row2] =t1
    return mat




########################################
def scaler_multiplication(mat, scalar):
    return mat*scalar



##################
def row_addition(mat, vect,rownum):
    mat[rownum]=mat[rownum]+vect
    return mat
##################3

L=np.eye(a)
print("your identity matrix of order ",a,"x",a,"=",L)
for i in range(0,a):
    for j in range(i+1,a):
        if m [i][i]==0:
            m=row_interchange(m,i,j)
        else:
            ratio=m[j][i]/m[i][i]
            L[j][i]=np.round(ratio,2)
            mul_result=scaler_multiplication(m[i],np.round(ratio,2))##row
            print("mul_result",mul_result)
            U=row_addition(m,-mul_result,j)
            print("my new upper matrix is=",U)
            print("my new lower matrix is=",L)
mul=np.dot(L,U)
print("lxu=",mul)



