a=int(input("Enter the number"))
b=int(input("Enter the number"))
print("Enter option 1-Addition,2-Subtraction,3-division,4-multiplication")
n=int(input("Enter the option"))
match n:
    case 1:
        print("Sum of two numbers:",a+b)
    case 2:
        print("Difference of two numbers:",a-b)
    case 3:
        print("Division of two number:",a/b)
    case 4:
        print("Product of two numbers:",a*b)
    case _:
        print("Invalid Choice")
        
