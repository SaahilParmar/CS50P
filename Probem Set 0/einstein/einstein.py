# Continuously asking user for integer input.
while True:
    try:
        mass = int(input('M: ').strip())

        # Printing the value of mass & breaking the loop.
        print(f'E: {mass * (300000000 * 300000000)}')
        break

    # If user inputs other than a integer.
    except ValueError:
        print('Input must be a number.')
        continue
        