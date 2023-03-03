from csv import DictReader, DictWriter
from sys import argv, exit

# 2 or more command-line arguments.
if len(argv) != 3:
    exit('Only 2 command-line arguements allowed. ["before.csv" file name & "after.csv" file name]')

# 2 command-line arguments.
else:
    try:
        # Opening csv file.
        with open(argv[1]) as before:

            # List to store csv file data.
            temp_list = []

            # Loop to start appending into list.
            for line in DictReader(before):

                # Splitting names into last & first name.
                lname, fname = line['name'].split(', ')

                # Appending correct format first & last name as dictionary into list.
                temp_list.append({'first': fname, 'last': lname, 'house': line['house']})

    # If file doesn't exist.
    except FileNotFoundError:
        exit('File cannot be read.')

    # If 'after' file is not a csv file.
    if argv[2].endswith('.csv') is False:
        exit('Invalid file name.')

    # If 'after' file is a csv file.
    else:
        # Opening 'after' csv file.
        with open(argv[2], 'w', newline='') as after:

            # Writing updated data of 'before' file into 'after' file.
            write = DictWriter(after, fieldnames=['first', 'last', 'house'])

            # Setting columns & correspnding items.
            write.writerow({'first': 'first', 'last': 'last', 'house': 'house'})

            # Writing list items to new file.
            write.writerows(temp_list)
            