# Empty list to store items.
grocery_list = []

# Empty dictionary to sort items.
grocery_dict = {}

# Loop to start adding items into the list.
while True:
    try:
        # Appending user inputted items into the list.
        grocery_list.append(input('ENTER ITEM: ').upper().strip())

    # Breaking the loop when 'ctrl + d' is pressed.
    except EOFError:
        break

# Loop to sort items in the list.
for item in sorted(grocery_list):

    # When item already in the list.
    if item in grocery_dict:

        # Adding +1 to item.
        grocery_dict[item] += 1

    # When it's a new item.
    else:

        # Giving initial value of 1 to the item.
        grocery_dict[item] = 1

# Loop to print the dictionary.
for keys, values in grocery_dict.items():
    print(values, keys)
    