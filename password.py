import random

passlength = int(input("Enter length of passsword: "))

lowercase = list(range(97, 123))
uppercase = list(range(65, 91))
numbers = list(range(48, 58))
special = list(range(33, 65))

pswdlist = lowercase.copy()

uppercase_include = input("Include UpperCase? (y/n): ")
if uppercase_include == "y" or uppercase_include == "Y":
    pswdlist.extend(uppercase)

numbers_include = input("Include Numbers? (y/n): ")
if numbers_include == "y" or numbers_include == "Y":
    pswdlist.extend(numbers)

special_include = input("Special Characters? (y/n): ")
if special_include == "y" or special_include == "Y":
    pswdlist.extend(special)

password = ""

while len(password) != passlength:
    password = password + chr(random.choice(pswdlist))

print(f"Password Generated: {password}")


