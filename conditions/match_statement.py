# match statement
x = int(input("enter the value of x: "))
match x:
    case 20:
        print("x is equal to 20")
    case _ if x < 20:
        print("x is less than 20")
    case _ if x > 20:
        print("x is greater than 20")

y = int(input("enter the value of y: "))
match y:
    case 0:
        print("y is equal to zero")
    case _ if y <40:
        print("y is less than 40")
    case _ if y >40:
        print("y is greater than 40")