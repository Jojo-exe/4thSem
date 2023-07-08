import numpy as np
n=eval(input("Enter the size of matrix: "))
r=1
m=[]
d=[]
while r<=n:
    c=1
    row=[]
    while c<=n:
        print("Enter the value of row ",r," column ",c)
        x=eval(input())
        row.append(x)
        c=c+1
    m.append(row)
    r=r+1

A=np.asarray(m)
c=1
while c<=n:
    print("please enter the constant of equations (b matrix ) ")
    x=eval(input())
    d.append(x)
    c=c+1
b=np.asarray(d)

def cramer(A, b):
    n = A.shape[0]
    x = np.zeros(n)
    det_A = np.linalg.det(A)

    for i in range(n):
        Ai = A.copy()
        Ai[:, i] = b
        det_Ai = np.linalg.det(Ai)
        x[i] = det_Ai / det_A

    return x

x = cramer(A, b)
print(x)