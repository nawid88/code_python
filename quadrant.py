x = int(input("Enter X coordinate: "))
y = int(input("Enter Y coordinate: "))

if y > 0 and x > 0:
    print("Quadrant 1")
elif y > 0 and x < 0:
    print("Quadrant 2")
elif y < 0 and x < 0:
    print("Quadrant 3")
elif y < 0 and x > 0:
    print("Quadrant 4")