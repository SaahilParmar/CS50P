def main():
    # Printing return value of 'value' after sending user input to it.
    print(value(input('Greetings: ').strip().lower()))


def value(greeting):
    # When user types 'hello'.
    if 'hello' in greeting:
        return 0

    # When user types anything starting with 'h'.
    elif 'h' in greeting[0]:
        return 20

    # When user types anything else.
    else:
        return 100


if __name__ == '__main__':
    main()
   