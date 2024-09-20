import math

side1_length = int(len(input("Enter Section 1: ")))
side2_length = int(len(input("Enter Section 2: ")))
side3_length = int(len(input("Enter Section 3: ")))

cans_needed = side1_length + side2_length + side3_length

cases_needed = math.ceil(cans_needed/12)

cans_bought = cases_needed * 12

left_over = cans_bought - cans_needed

cost = cases_needed * 14.95

print(f""" 
Cans Needed: {cans_needed}
Left Over: {left_over}
Cost: ${cost}""")
