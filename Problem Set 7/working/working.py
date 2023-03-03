from re import search


def main():
    # Getting user input => sending to convert() & printing it's return value.
    print(convert(input("Hours: ").strip()))


def convert(s):
    """
    Converts string time into 24-hour format string.
    """

    # Searching pattern in provided string.
    check = search(r'^([1-9][0-2]?)(:([0-5][0-9]))? (AM|PM) to ([1-9][0-2]?)(:([0-5][0-9]))? (AM|PM)$', s)

    # When pattern in string.
    if check:

        # Getting groups from 'search' pattern.
        user_time = check.groups()

        # Starting time has 'AM'.
        if user_time[3] == 'AM':

            # Input is '12'.
            if int(user_time[0]) == 12:

                # 12 AM in 24-hour format = '00'.
                start_hour = int(user_time[0]) - 12

            # Input is anything else.
            else:

                # Keeping time as it is.
                start_hour = int(user_time[0])

        # Starting time has 'PM'.
        else:

            # Input is '12'.
            if int(user_time[0]) == 12:

                # Keeping time as it is.
                start_hour = int(user_time[0])

            # Input is anything else.
            else:

                # Adding 12 to input to make 24-hour format.
                start_hour = int(user_time[0]) + 12

        # Ending time has 'AM'.
        if user_time[7] == 'AM':
            if int(user_time[4]) == 12:
                end_hour = int(user_time[4]) - 12
            else:
                end_hour = int(user_time[4])

        # Ending time has 'PM'.
        else:
            if int(user_time[4]) == 12:
                end_hour = int(user_time[4])
            else:
                end_hour = int(user_time[4]) + 12

        if user_time[2] is None:
            start_min = '00'
        else:
            start_min = user_time[2]

        if user_time[6] is None:
            end_min = '00'
        else:
            end_min = user_time[6]

        return f'{start_hour:02}:{start_min} to {end_hour:02}:{end_min}'

    # When pattern not in string.
    else:
        raise ValueError


if __name__ == '__main__':
    main()
    