from PIL import Image, ImageOps
from sys import argv, exit

# More or less than 2 command-line arguments.
if len(argv) != 3:
    exit('Only 2 command-line arguments allowed.[Name (or path) of a JPEG or PNG to read (i.e., open) as input & Name (or path) of a JPEG or PNG to write (i.e., save) as output]')

# Exactly 2 command-line arguments.
else:
    # Checking extensions of input & output files.
    if argv[1].endswith('.jpg') and argv[2].endswith('.jpg') or \
            argv[1].endswith('.jpeg') and argv[2].endswith('.jpeg') or \
            argv[1].endswith('.png') and argv[2].endswith('.png'):

        try:
            # Opening input file.
            pic_1 = Image.open(argv[1])

            # Opening shirt.png from database.
            pic_2 = Image.open('shirt.png')

            # Setting resolution of both images.
            pic_1 = ImageOps.fit(pic_1, pic_2.size)

            # Pasting shirt.png on input file.
            pic_1.paste(pic_2, pic_2)

            # Saving new image as output file name.
            pic_1.save(argv[2])

        # If inputted file does not exist.
        except FileNotFoundError:
            exit('Input file does not exist.')

    # Files have different extensions.
    else:
        exit('Input and output file have different extensions.')
        