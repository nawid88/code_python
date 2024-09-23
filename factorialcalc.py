
num = int(input("Enter a number: "))
cntr = num - 1
option = input("While Loop or For Loop? (while/for): ")
factorial = num
factorial2 = num 

if option == "while":
    while cntr != 0:
        factorial = factorial * cntr
        cntr -= 1
    print(f"The factorial of {num} is {factorial}")



if option == "for":
    factorials = list(range(1, num))
    for nums in factorials:
        factorial2 = factorial2 * nums
    print(f"The factorial of {num} is {factorial2}")

