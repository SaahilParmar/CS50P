# Total number of coins.
total = 50

# Initializing while loop.
while True:

    # Showing the user the amount.
    print(f'Amount Due: {total}')

    try:
        # Getting user input as integer.
        user = int(input('Insert Coin: ').strip())

        # if user input is in the list of valid coins.
        if user in [5, 10, 25]:
            total -= user

        # if user input is not in the list.
        else:
            print('Only 5, 10 & 25 is allowed.')

        # When total becomes 0.
        if total == 0:
            print(f'Change Owed: {total}')
            break

        # When total goes beyond 0.
        elif total < 0:

            # Multiplying negative total with -1 & printing positive integer.
            print(f'Change Owed: {total * -1}')
            break

    except ValueError:
        continue
        