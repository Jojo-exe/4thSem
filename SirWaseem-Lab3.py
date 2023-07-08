a=[1,4,6,8,-43,7,-7]

# print(a[-3:6:1])
# -->MAking tuple
# print(tuple(a))

# print(range(10)) #--> for checking range function
#
# print("First metghod")
# for i in range(10):
#     print(i)
#
# print("Second method")
# for i in range(1,10,2):
#     print(i)
#
# print("Third Method")
# for i in range(1,10):
#     print(i)
#
#
# print("Seprate and end function")
# for i in range(1,10):
#     print(i,end=',',sep='-')

# 1
print("Odd valus cube from 1 to 100:")
odd=[i*i*i for i in range(1,100,2)]
print(odd)
# 2
print("Even valus cube from 1 to 100:")
even=[i*i*i for i in range(1,100,1)]
print(even)
# 3
print ("The Prime Numbers in the range 1 to 100: ")
for number in range (30):
    if number > 1:
        for i in range (2, number):
            if (number % i) == 0:
                break
        else:
            print (number)







