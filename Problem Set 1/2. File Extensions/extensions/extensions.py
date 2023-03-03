# Getting user input.
user = input('File name: ').strip().lower()

# File name ends with '.gif'.
if user.endswith('.gif'):
    print('image/gif')

# File name ends with '.jpg' or '.jpeg'.
elif user.endswith('.jpg') or user.endswith('.jpeg'):
    print('image/jpeg')

# File name ends with '.png'.
elif user.endswith('.png'):
    print('image/png')

# File name ends with '.pdf'.
elif user.endswith('.pdf'):
    print('application/pdf')

# File name ends with '.txt'.
elif user.endswith('.txt'):
    print('text/plain')

# File name ends with '.zip'.
elif user.endswith('.zip'):
    print('application/zip')

# File name ends with unknown extension.
else:
    print('application/octet-stream')
    