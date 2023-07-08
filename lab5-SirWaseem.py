
# a=[1,2,3,4,5]
# def sum(x):
#     sum=x[0]
#     if x==[]:
#         return 0
#     else:
#         sum+=x
#     return x[0]+(sum(x[1:]))
# print(sum(x))
#



# nested list
# Python Program to find sum
# of nested list using Recursion

# def sum_nestedlist(l):
#     total =  0
#     for j in range(len(l)):
#         if type(l[j]) == list:
#             total += sum_nestedlist(l[j])
#         else:
#             total += l[j]
#     return total
# print(sum_nestedlist([[1, 2, 3], [4, [5, 6]], 7]))


n=eval(input("Enter number:"))
count=0.0
while(n>0 ) :
    count=count+1
    n=n//10
print(count)