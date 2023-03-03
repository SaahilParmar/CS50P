# List to collect all letters without vowels.
collect = ['Output: ']

# Loop to check letters in word.
for letter in input('Input: ').strip():

    # If current letter is not in tuple.
    if letter not in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):

        # Append that letter in the list.
        collect.append(letter)

# Loop to print letters in list.
for letter in collect:

    # Printing letters in same line.
    print(letter, end='')

# Printing blank space for aesthetic.
print()
