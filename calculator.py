num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))



while True:
    operation = input("""Choose an operation. 
-Add
-Subtract
-Multiply
-Divide
: """)
    if operation.lower() == "add":
        result = num1 + num2
        break
    elif operation.lower() == "subtract":
        result = num1 - num2
        break
    elif operation.lower() == "multiply":
        result = num1 * num2
        break
    elif operation.lower() == "divide":
        while True:
            if num2 == 0:
                num2 = int(input("A number cannot be divided by 0, please enter a new value for number 2: "))
            else:
                break
        result = num1/num2
        break
    else:
        print("Invalid Option, Please try again: ")


if operation in ["subtract", "multiply", "divide"]:
    a = "by"
else:
    a = "to"

if operation == "divide":
    b = "d"
else:
    b = "ed"

print(f"{num1} {operation}{b} {a} {num2} is equal to {result}")













