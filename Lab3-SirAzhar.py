# end--> for spaceing
# sep --> for seprating with special chaRActer
# table=[[1,2,3,4],[,5,6,7,8]] -->Embeded list
# table=[[1,2,3,4],[,5,6,7,[8]]] --> embeded list with in a list (row in table , col in table)

# for a,b in [[1,2],[3,4],[5,6]]:
#     print(a)
#     print(b)
# for x*x in x list

# a=[1,2,3,4,5,6,7,8,9]
# b=[n for n in a if n%2==1]
# print(b)

# filter method with lambda
# listN=list(filter(lambda a:a!=1,[2,1,3,1,4,1,5,7,1]))
# print(listN)

# listN=list(filter(lambda a:a%2==1,[2,1,3,1,4,1,5,7,1]))
# print(listN)

# UserDefineFunction
#     -->Dev
#     --> def printH(name)
#         print('hello',name)

    # def printH(name):
    #     print('hello '+name)
    # printH(qad)

def calculator():
    a = eval(input("Enter 1st  Number:"))
    b = eval(input("Enter 2nd Number:"))
    # op = input("Enter operator:")
    # com =a+op+b
    # print(com)
    # exec(com)

    op=eval(input(print("Press 1 to add:\nPress 2 to Subtract:\nPress 3 to mutilpy:\nPress 4 to Divide:\nPress 5 to exit:\n")))

    while op!=5:

        if op==1:
            print((a+b))
            calculator()
        elif op==2:
            print((a-b))
            calculator()
        elif op==3:
            print((a*b))
            calculator()
        elif op==4:
            print((a//b))
            calculator()
        break

calculator()
