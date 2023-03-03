def main():
    # Sending user input to 'convert', sending that to 'gauge', & printing it's return value.
    print(gauge(convert(input('Fraction: ').strip())))


def convert(fraction):
    """
    Converts string fraction into nearest percentage.
    """

    # Splitting string.
    x, y = fraction.split('/')

    # If y = 0.
    if int(y) == 0:
        raise ZeroDivisionError

    # When string fraction is correct.
    else:
        return round((int(x) / int(y)) * 100)


def gauge(percentage):
    """
    Converts percentage into E, F or percentage string.
    """
    if percentage <= 1:
        return 'E'
    elif percentage >= 99 or percentage == 100:
        return 'F'
    else:
        return f'{percentage}%'


if __name__ == '__main__':
    main()
