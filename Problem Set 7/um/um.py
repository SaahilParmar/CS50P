from re import findall


def main():
    # Getting user input => sending to count & printing it's return value.
    print(count(input("Text: ").strip()))


def count(s):
    """
    Returns number of times 'um' is used in string.
    """

    # Using 'findall' to look for 'um' by converting string to lowercase.
    return len(findall(r'\bum\b', s.lower()))


if __name__ == "__main__":
    main()
    