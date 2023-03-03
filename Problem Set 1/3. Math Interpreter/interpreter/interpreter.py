# Getting mathematical expression from user.
x, y, z = input('Expression: ').strip().split()

# If expression has addition.
if y == '+':
    print(f'{(int(x) + int(z)):.1f}')

# If expression has subtraction.
elif y == '-':
    print(f'{(int(x) - int(z)):.1f}')

# If expression has multiplication.
elif y == '*':
    print(f'{(int(x) * int(z)):.1f}')

# If expression has division.
elif y == '/':
    print(f'{(int(x) / int(z)):.1f}')