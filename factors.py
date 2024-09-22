

num = int(input("Enter a number: "))
cntr = num

option = input("While or For Loop (while/for): ")

factors = []
numbers = list(range(1, num + 1))
factors2 = []

if option == "while":
    while cntr != 0:
        if num % cntr == 0:
            factors.append(cntr)
        cntr = cntr - 1
elif option == "for":
    for nums in numbers:
        if num % cntr == 0:
            factors2.append(cntr)
        cntr = cntr - 1
    
    

print(f"{num} has factors of {factors} {factors2}")
