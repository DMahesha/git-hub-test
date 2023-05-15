def addition (x,y):
    return x + y
def subtraction (x,y):
    return x - y
def multiplication (x,y):
    return x * y
def division (x,y):
    return x / y

print ("""
Select Operation:
1. Addition
2. Substraction
3. Multiplication
4. Division
""")

while True:
    choice = int(input("Enter choice: "))

    if choice in (1, 2, 3, 4):
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print ("Invalid selection. Please pick a number.")
            continue

        if choice == 1:
            print (num1, " + ", num2, " = ", addition(num1,num2))
            break
        elif choice == 2:
            print (num1, " - ", num2, " = ", subtraction(num1,num2))
            break
        elif choice == 3:
            print (num1, " * ", num2, " = ", multiplication(num1,num2))
            break
        elif choice == 4:
            print (num1, " / ", num2, " = ", division(num1,num2))
            break
    else:
        print("Invalid input.")