# List to store each letter of user's input.
collect = ['snake_case: ']

# Asking for user input in camel_case & starting loop on it.
for letter in input('camelCase: ').strip():

    # When uppercase letter is found.
    if letter == letter.upper():

        # Append that letter in lowercase with '_' infront.
        collect.append(f'_{letter.lower()}')

    # Append everything else as it is.
    else:
        collect.append(letter)

# Loop to print list.
for letter in collect:

    # Printing list items without empty space.
    print(letter, end='')

# Printing newline for aesthetics.
print()
