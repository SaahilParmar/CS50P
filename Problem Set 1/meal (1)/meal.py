def main():

    # Getting user input for time & sending it to convert().
    user = convert(input('What is the time? ').lower().strip())

    # If returned float is between 7 & 8.
    if 7 <= user <= 8:
        print('breakfast time')

    # If returned float is between 12 & 13.
    elif 12 <= user <= 13:
        print('lunch time')

    # If returned float is between 18 & 19.
    elif 18 <= user <= 19:
        print('dinner time')


def convert(time):
    """
    Converting time into integer.
    """

    # Checking length of inputted time.
    if len(time) == 4 or len(time) == 5:

        # Splitting hour & minutes.
        hour, minutes = time.split(':')

        # Returning float after necessary calculations.
        return float(hour) + (float(minutes) / 60)

    else:  # CHALLENGE QUESTION

        # Splitting inputted time from meridian input.
        new_time, meridian = time.split()

        # Splitting hour & minutes.
        hour, minutes = new_time.split(':')

        # Checking if meridian is 'a.m.'.
        if meridian == 'a.m.':

            # Returning float after necessary calculations.
            return float(hour) + (float(minutes) / 60)

        # Checking if meridian is 'p.m.'.
        else:

            # Returning float after necessary calculations.
            return (float(hour) + (float(minutes) / 60)) + 12


if __name__ == '__main__':
    main()
    