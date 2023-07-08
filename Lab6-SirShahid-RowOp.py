#fOR ROW INTERCHANGE
import numpy as np
# Mat1=np.array([[2,3,-4],[4,6,1],[3,7,-2]])
# print("your original matrix is=",Mat1)
# def row_interchange(mat,r1,r2):
#     t1=mat[[r1-1]].copy()
#     t2=mat[[r2-1]].copy()
#     mat[[r1-1]]=t2
#     mat[[r2-1]]=t1
# row_interchange(Mat1,1,2)
# print(Mat1)
# #construction of function for Scalar Multiplication
# Mat1=np.array([[2,3,-4],[4,6,1],[3,7,-2]])
# print("Your original matrix is=",Mat1)
# def sclr_mul(mat,scalar,row):
#     mat[row]=scalar*mat[row]
# sclr_mul(Mat1,-8,1)
# print("after scalar multiplication,matrix is=",Mat1)
# #construction of the function for adding rwo rows
# Mat1=np.array([[2,3,-4],[4,6,1],[3,7,-2]])
# print("Your original matrix is=",Mat1)
# def add_mat(mat,r1,r2):
#     mat[r1-1]=mat[r1-1]+mat[r2-1]
# add_mat(Mat1,2,3)
# print("after addition,matrix is=",Mat1)



#code for solving n*n system of linear equation by using  crammer rule
import numpy as np
n=eval(input("enter the size pf matrix= "))
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
print("coefficient matrix=",m)
n5=np.linalg.det(m)
print("determinant of matrix is=",n5)
m7=np.linalg.inv(m)
print("inverse of the matrix is=",m7)
vtr1=[]
c=1
while c<=n:
    print("please enter the constantof equations")
    x=eval(input())
    vtr1.append(x)
    c=c+1
vtr2=np.asarray(vtr1)
ans=np.dot(m7,vtr2)
print(ans)
for i in range(len(ans)):
    print("value of x[",i+1,"]=",np.round(ans[i],2))
#crammer
det=[]
ans1=[]
print("Your original matrix=",m)
print("ypur original vecto=",vtr2)
for i in range(n):
    m1=m.copy()
    m1[:,i]=vtr2
    print("after =",m1)
    d=np.linalg.det(m1)
    ans1.append(d/n5)
ans1=np.asarray(ans1)
for i in range(len(ans1)):
    print(ans1)
    print("value of x[",i+1,"]=",np.round(ans[i],2))