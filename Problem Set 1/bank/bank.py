# Asking for user greeting.
user = input('Greetings: ').lower().strip()

# When user greets with 'hello'.
if user.startswith('hello'):
    print('$0')

# When user greets with word's starting with 'h'.
elif user.startswith('h'):
    print('$20')

# When user greets with anything else.
else:
    print('$100')
    