def main():
    # Getting input for total of meal.
    dollars = dollars_to_float(input("How much was the meal? "))

    # Getting input for percentage of tip.
    percent = percent_to_float(input("What percentage would you like to tip? "))

    # Multiplying total amount with percentage of tip.
    tip = dollars * percent

    # Printing the answer.
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    """
    Converts string to float.
    """

    # When string starts with '$'.
    if d.startswith('$'):

        # Removing '$' from string & converting to float.
        return float(d.removeprefix('$'))

    # When string doesn't starts with '$'.
    else:

        # Converting string to float.
        return float(d)


def percent_to_float(p):
    """
    Convert string to int of percentage.
    """

    # When string ends with '%'.
    if p.endswith('%'):

        # Removing '%' from string & converting to int.
        return int(p.removesuffix('%')) / 100

    # When string doesn't end with '%'.
    else:

        # Converting string to int.
        return int(p) / 100


if __name__ == '__main__':
    main()
    