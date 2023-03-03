def main():
    print(convert(input('TYPE: ').strip()))


def convert(s):
    """
    Converts ':)' & ':(' into emoji's.
    """
    if ':)' or ':(' in s:
        return s.replace(':)', '🙂').replace(':(', '🙁')


if __name__ == '__main__':
    main()
