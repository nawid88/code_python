#From 1 to N, where N is an integer greater one. We will output the number between [1,N] that has the most factors. 
#Example: From numbers 1 to 5. → The number 4 has the most factors.

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

