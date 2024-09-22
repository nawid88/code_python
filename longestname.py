
name = ""
nameList = list()


while name != "X":
    name = input("Enter name, enter X to exit: ")
    if name != "X":
        nameList += [name]

longestName = ""
for name in nameList:
    if len(name) > len(longestName):
        longestName = name
        longestName = longestName

print(longestName)