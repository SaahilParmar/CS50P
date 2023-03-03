from random import randint

# Loop starting for level of the game.
while True:
    try:
        # Getting user input for int.
        user = int(input('Level: ').strip())

        # When input is a positive integer.
        if user > 0:

            # Saving a random number between 1 & user's input.
            r = randint(1, user)

            # Loop starting the guessing game.
            while True:

                # Getting guess from user.
                guess = int(input('Guess: ').strip())

                # When guess smaller than random saved number.
                if guess < r:
                    print('Too small!')
                    continue

                # When guess larger than random saved number.
                elif guess > r:
                    print('Too large!')
                    continue

                # When guess is right.
                else:
                    print('Just right!')
                    break
            break

        # When input is a negative integer.
        else:
            print('Please enter a positive integer.')
            continue

    # When user doesn't input a number.
    except ValueError:
        print('No alphabets or special characters are allowed.')
        continue
        