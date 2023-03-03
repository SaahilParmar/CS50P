def main():

    # Printing result of user inputted IP address which was sent to validate().
    print(validate(input("IPv4 Address: ").strip()))


def validate(arg):
    """
    Validates IP addresses to True or False.
    """
    try:
        # Splitting IP address into 4 variables.
        a, b, c, d = arg.split('.')

        # Checking if each variable int is in the given range.
        if int(a) in range(0, 256) and\
                int(b) in range(0, 256) and\
                int(c) in range(0, 256) and\
                int(d) in range(0, 256):
            return True

        # If each variable int is not in the given range.
        else:
            return False

    # If input is anything other than int.
    except ValueError:
        return False


if __name__ == '__main__':
    main()
   