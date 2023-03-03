from validator_collection import checkers

# Getting user input for Email ID.
user = input('Email: ').strip()

# If ID is correct.
if checkers.is_email(user) is True:
    print('Valid')

# If ID is incorrect.
else:
    print('Invalid')
    