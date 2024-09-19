calculation = input('''Choose an option:
- 1. Add
- 2. Subtract
- 3. Multiply
- 4. Divide
''')

num1 = int(input(print("Enter number 1: ")))
num1 = int(input(print("Enter number 1: ")))

if calculation == 'Add':
    sum = num1 + num2
    print(f'{num1} + {num2} = {sum}')
    elif calculation == 'Subtract':
        difference = num1 - num2
        print(f'{num1} - {num2} = {difference}')
        elif calculation == 'Multiply':
            product  = num1*num2
            print(f'{num1} x {num2} = {product}')
            elif calculation == 'Divide':
                quotient = num1/num2
                print(f'{num1} / {num2} = {quotient}')
                else:
                    print('Invalid Option')




