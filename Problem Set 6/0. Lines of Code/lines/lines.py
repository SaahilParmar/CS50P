from sys import argv, exit

# If more or less than 2 command-line arguments.
if len(argv) != 2:
    exit('2 command-line arguments are allowed.')

# When exactly 2 command-line arguments.
else:
    # If file name ends with '.py'.
    if argv[1].endswith('.py'):
        try:
            # Opening the file.
            with open(argv[1]) as file:

                # Storing lines of file.
                lines = file.read().split('\n')

                # Variable to count lines of code.
                count = 0

                # Loop to start counting lines of code.
                for line in lines:

                    # If there are no comments in the line.
                    if not line.lstrip().startswith('#') and line.lstrip() != '':

                        # Adding 1 to count.
                        count += 1

            # Printing final lines of code.
            print(count)

        # If the entered file name does not exist.
        except FileNotFoundError:
            exit('File does not exist.')

    # If file name doesn't end with '.py'.
    else:
        exit('Not a Python file.')
        