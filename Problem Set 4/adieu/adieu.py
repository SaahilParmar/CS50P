from inflect import engine

# Creating empty list to store names.
names = []

# Initializing inflect module.
on = engine()

# Loop for continuously asking for user input.
while True:
    try:
        # Appending user input names into list.
        names.append(input('Name: ').strip().capitalize())

    # Program ends when 'ctrl + d' is pressed.
    except (EOFError):
        break

# Printing all the names in the list.
print(f'Adieu, adieu, to {on.join(names)}')
