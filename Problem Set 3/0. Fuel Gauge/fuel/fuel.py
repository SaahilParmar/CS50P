# Continuously asking for user input.
while True:
    try:
        # Splitting user input.
        x, y = input('Fraction: ').strip().split('/')

        # Doing calculations by converting str into int.
        output = round((int(x) / int(y))*100)

        # When fraction in correct format.
        if 0 <= output <= 100:

            # When output is smaller or equal to 1.
            if output <= 1:
                print('E')

            # When output is greater or equal to 99 or 100.
            elif output >= 99 or output == 100:
                print('F')

            else:
                print(f'{output}%')

            break

        # When fraction in incorrect format.
        else:
            print('Invalid Fraction. Numerator bigger than denominator.')
            continue

    # If something other than number is inputted.
    except ValueError:
        print('Only numbers are allowed.')
        continue

    # If 0 is in denominator's place.
    except ZeroDivisionError:
        print('Invalid Fraction.')
        continue
        