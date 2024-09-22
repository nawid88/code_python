"""
 If all three angles are 60, output Equilateral.

 If the three angles add up to 180 and exactly two of the angles are the same, output Isosceles.
 
 If the three angles add up to 180 and no two angles are the same, output Scalene.

If the three angles do not add up to 180, output Error.
"""

angle1 = int(input("Enter angle 1: "))
angle2 = int(input("Enter angle 2: "))
angle3 = int(input("Enter angle 3: "))

if angle1 == 60 and angle2 == 60 and angle3 == 60:
    print("Equilateral")
elif (angle1 + angle2 + angle3 == 180) and (angle1 == angle2 or angle2 == angle3 or angle1 == angle3):
    print("Isosceles")
elif (angle1 + angle2 + angle3 == 180) and (angle1 != angle2 != angle3):
    print("Scalene")
else:
    print("Error")