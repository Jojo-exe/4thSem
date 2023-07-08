
def calculator():
    a=eval(input("Enter a Number:"))
    b=eval(input("Enter a Number:"))
    op = eval(input("1 to add \n2 to sub\n3 to multiply\n4 to divide\n5 to perform all Operations\n6 to exit\n"))


    while op!=6:
        if op==1:
            print((a + b))
            calculator()
        elif op==2:
            print((a - b))
            calculator()
        elif op==3:
            print((a*b))
            calculator()
        elif op==4:
            print((a//b))
            calculator()
        elif op==5:
            print("Sum:",(a + b))
            print("Difference:",(a - b))
            print("Product:",(a * b))
            print("Division:",(a//b))
            calculator()

        break

calculator()
