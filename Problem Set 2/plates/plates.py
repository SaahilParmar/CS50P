def main():

    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    """
    Returns True if plate is valid or False if plate is invalid.
    """

    # All vanity plates must start with at least two letters.
    # vanity plates may contain a maximum of 6 characters (letters or numbers) and
    # a minimum of 2 characters.
    # No periods, spaces, or punctuation marks are allowed.
    if s[0:2].isalpha and s.isalnum and 2 <= len(s) <= 6:

        # Looping through the string.
        for i in s:

            # If ith value is number.
            if i.isnumeric():

                # If all the values after i are numeric & not starting with 0.
                if s[s.index(i):].isnumeric() and i != '0':
                    return True

                else:
                    return False
        return True


main()
