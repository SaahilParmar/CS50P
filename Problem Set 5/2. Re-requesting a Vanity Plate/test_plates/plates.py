def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    """
    Verifies whether given plates are in correct format or not.
    """

    if 2 <= len(s) <= 6 and s.isalnum() and s[0:2].isalpha():

        for i in s:

            if i.isnumeric():
                item = s.index(i)

                if s[item:].isnumeric() and i != '0':
                    return True

                else:
                    return False
        return True


if __name__ == '__main__':
    main()
    