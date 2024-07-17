def calculator():
    num1 = float(input("Enter the first number: "))

    num2 = float(input("Enter the second number: "))

    print("Choose the operation you want to perform:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    # Taking choice by user
    operation = input("Enter the operation : ")
    
    # Addition
    if operation == '1':
        result = num1 + num2
        print(f"{num1} + {num2} = {result}.")
    # Subtraction
    elif operation == '2':
        result = num1 - num2
        print(f"{num1} - {num2} = {result}.")
    # Multiplication
    elif operation == '3':
        result = num1 * num2
        print(f"{num1} * {num2} i= {result}.")
    # Division
    elif operation == '4':
        if num2 != 0:
            result = num1 / num2
            print(f"{num1} / {num2} = {result}.")
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid choice !")

# Function Call
calculator()