def main():
    # Getting user input => sending to shorten & printing it's return value.
    print(f'Output: {shorten(input("Input: ").strip())}')


def shorten(word):
    """
    Removes lowercase or uppercase vowels from the given string.
    """

    # Loop to check letters in word.
    for letter in word:

        # If letter is vowel.
        if letter in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):

            # Replacing vowel with empty space.
            word = word.replace(letter, '')

    # Returning word without vowels.
    return word


if __name__ == '__main__':
    main()
         