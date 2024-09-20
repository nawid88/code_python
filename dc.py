import random
dc = int(input("Enter the DC: "))
while True:
    if dc > 20:
        dc = int(input("DC cannot be greater than 20, please try again: "))
    else:
        break

d20 = random.choice(range(1, 21))

if d20 >= dc:
    print(f"You have rolled a {d20}, success!")
else:
    print(f"You have rolled a {d20}, failure!")

