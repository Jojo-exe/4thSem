# a = eval(input("Enter the number:"))
# print(a)
# i = 1
# while i <= a:
#     print(i, 'My name is aleem')
#     i = i + 1
import numpy as np

# m1 = np.array([[2, 5], [3, 6]])
# print(m1)
# m2 = np.transpose(m1)
# print(m2)
# m3 = np.linalg.det(m1)
# print(m3)
# m4 = np.linalg.inv(m1)
# print(m4)
# m5 = np.dot(m1, m2)
# print(m5)

# INPUT START
n = eval(input("Enter the size of matrix= "))
r = 1
matrix = []
while r <= n:
    c = 1
    row = []
    while c <= n:
        print("Enter the value of row", r, "Column", c)
        x = eval(input())
        row.append(x)
        c = c + 1
    matrix.append(row)
    r = r + 1
m = np.array(matrix)
print(" matrix:","\n", m)
n5 = np.linalg.det(m)
# INPUT END
print("Determinant of matrix is=", n5)
m7 = np.linalg.inv(m)
print("Invese of matrix is=", m7)
vtr1 = []
c = 1
while c <= n:
    print("Please enter the constant of equation:")
    x = eval(input())
    vtr1.append(x)
    c = c + 1
    vtr2 = np.asarray(vtr1)
    ans = np.dot(m7, vtr2)
    print(ans)
    for i in range(len(ans)):
        print("Value of x[", i + 1, "]=", np.round(ans[i], 2))
