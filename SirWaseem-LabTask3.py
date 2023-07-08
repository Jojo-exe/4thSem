l1=[]
n=eval(input("Enter a Number:"))
while n<100 or n>999:
    n=eval(input("Enter 3 Digit Number"))
a=n
while a!=0:
    l1.append(a%10)
    a=a//10
print(l1,n)
l2=l1.copy()

while l2!=[]:
    a=a*10
    a=a+l2.pop(0)
    print(a)






