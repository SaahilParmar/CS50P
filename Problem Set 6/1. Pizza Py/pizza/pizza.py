from csv import reader
from sys import argv, exit
from tabulate import tabulate

# When more or less than 1 command-line argument.
if len(argv) != 2:
    exit('ONLY 1 COMMAND-LINE ARGUMENT ALLOWED. [FILE NAME WITH FORMAT]')

# Exactly 1 command-line argument.
else:
    # When file name has '.csv' extension.
    if argv[1].endswith('.csv'):
        try:
            # Opening '.csv' file.
            with open(argv[1]) as file:

                # Creating table to store items of csv file.
                table = []

                # Appending csv file data into list as list.
                for row in reader(file):
                    table.append(row)

            # Printing table in tabulate. ['headers' is the first line of csv file, rest of it to be printed so 'table[1:]' is used.]
            print(tabulate(table[1:], headers=table[0], tablefmt='grid'))

        # When inputted csv file doesn't exist.
        except FileNotFoundError:
            exit('File does not exist.')

    # When file name doesn't have '.csv' extension.
    else:
        exit('Not a CSV file.')
        