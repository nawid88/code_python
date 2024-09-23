num = int(input("Enter a number: "))
factor = num
cntr = 0


while factor != 0:
    if num % factor == 0:
        cntr += 1
    factor -= 1

if cntr <= 2:
    print("This number is a prime number.")
else:
    print("This number is not a prime number.")

