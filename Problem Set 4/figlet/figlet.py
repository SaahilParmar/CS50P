from pyfiglet import Figlet, figlet_format
from random import choice
from sys import argv, exit

# Initializing Figlet().
f = Figlet()

# Expects zero or two command-line arguments.
# Zero if the user would like to output text in a random font.
if len(argv) == 1:

    # Printing string input in random figlet font.
    print(figlet_format(input('Input: ').strip(), font=choice(f.getFonts())))

# Two if the user would like to output text in a specific font,
# in which case the first of the two should be -f or --font,
# and the second of the two should be the name of the font.
elif len(argv) == 3 and ((argv[1] == '-f' or argv[1] == '--font') and (argv[2] in f.getFonts())):

    # Printing string input in user defined figlet font.
    print(figlet_format(input('Input: ').strip(), font=argv[2]))

# If the user provides two command-line arguments and the first is not -f or --font or the second is not the name of a font,
# the program should exit via sys.exit with an error message.
else:
    exit('Error_Message.')
    