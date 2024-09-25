
num = int(input("Enter a number: "))

numbers = list(range(1, num + 1))

mostFactors = 0
mostFactorNum = 0

for num1 in numbers:
    factor = num1
    factors = 0
    while factor != 0:
        if num1 % factor == 0:
            factors += 1
        factor -= 1
    print(f"{num1} has {factors} factor(s)")
    if factors > mostFactors:
        mostFactors = factors
        mostFactorNum = num1
        
print(f"{mostFactorNum} has the most factors.")

