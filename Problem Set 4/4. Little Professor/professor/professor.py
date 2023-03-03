from random import randint


def main():
    # Calling function & storing the value.
    l = get_level()

    # Variable to store user score.
    score = 0

    # Variable for how many questions to ask.
    time = 10
    while time != 0:
        # Calling function to get random value according to level.
        x = generate_integer(l)

        # Calling function to get random value according to level.
        y = generate_integer(l)

        # Variable for chances.
        chance = 4

        while chance != 1:
            try:
                # Asking user for answer of mathematical equation.
                user = int(input(f'{x} + {y} = ').strip())

                # Checking if answer is right.
                if user == x + y:

                    # Adding to total score.
                    score += 1
                    break

                # If answer is wrong.
                else:
                    print('EEE')

                    # Subtracting chance & asking again.
                    chance -= 1

            # If other than integer is inputted.
            except ValueError:
                print('EEE')

                # Subtracting chance & asking again.
                chance -= 1

            # When chances are over.
            if chance == 1:

                # Printing correct answer.
                print(f'Correct Answer: {x} + {y} = {x + y}')

        # Subtracting 'time' each time loop has run.
        time -= 1

    # Printing final score.
    print(f'Score: {score}')


def get_level():
    """
    This function returns level, chosen by the user.
    """
    while True:
        try:
            # Getting user input for level.
            level = int(input('Level: ').strip())

            # Checking for correct user input.
            if 1 <= level <= 3:
                return level

            # If incorrect input.
            else:
                print('Only positive integer between 1 to 3 is allowed. Try again.')
                continue

        # If invalid input.
        except ValueError:
            print('Only 1, 2 or 3 is allowed. Try again.')
            continue


def generate_integer(level):
    """
    Generates random integers according to the level given.
    """
    # When level is 1.
    if level == 1:

        # Return random integer between 0 & 9.
        return randint(0, 9)

    # When level is 2.
    elif level == 2:

        # Return random integer between 10 & 90.
        return randint(10, 99)

    # When level is 3.
    elif level == 3:

        # Return random integer between 100 & 999.
        return randint(100, 999)


if __name__ == '__main__':
    main()
    