total = 0
cntr = 0

while True:
    grade = input("Enter grade, type in X to exit: ")
    if grade.lower() == "x":
        break
    total += int(grade)
    cntr += 1

avg = total/cntr 
print(f"Average: {avg}")


