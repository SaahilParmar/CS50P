# Dictionary with items on menu with respective price.
menu = {"Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00}

# Variable to store final amount.
total = 0

while True:
    try:
        # Getting user input.
        user = input('Item: ').strip().title()

        # Checking if input in menu.
        if user in menu:

            # If input in menu, adding respective amount into total.
            total = total + menu.get(user)

            # Printing final total.
            print(f'Total: ${total}0')

        # If item not in menu.
        else:
            continue

    # When 'ctrl + d' is pressed.
    except (EOFError):
        break
        