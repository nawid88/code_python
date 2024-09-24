spot = int(input("Enter a number: "))

fibonacci_seq = []

num1 = 1
num2 = -1
cntr = -1


while cntr != spot:
    fibnum = num1 + num2
    num2 = num1
    num1 = fibnum
    cntr += 1
    

if spot % 10 == 1:
    print(f"{spot}st fibanocci number is {fibnum}")
else: 
    print(f"{spot}th fibanocci number is {fibnum}")

