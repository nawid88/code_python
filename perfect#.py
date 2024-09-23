
perfectnums = []

numbers = list(range(1, 10001))


for num in numbers:
    factor = num - 1
    factors = []
    total = 0
    while factor != 0:
        if num % factor == 0:
            factors.append(factor)
        factor -= 1
    for num2 in factors:
        total += num2
    if total == num:
        perfectnums.append(num)

print(perfectnums)

total2 = 0
for nums3 in perfectnums:
    total2 += nums3

print(f"Sum of all perfect numbers under 10,000 = {total2}")
    
