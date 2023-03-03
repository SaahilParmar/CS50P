from datetime import date
from inflect import engine
from sys import exit


def main():

    # Printing user input sent to date_checking(), sent to no_of_days().
    print(no_of_days(date_checking(input('Date of Birth (YYYY-MM-DD): ').strip())))

    #print(type(date_checking(input('Date of Birth (YYYY-MM-DD): ').strip())))


def date_checking(s):
    try:
        # Returning ISO format date from given string.
        return date.fromisoformat(s)

    # If given string cannot be converted to ISO format date.
    except ValueError:
        exit('Invalid Date. Please enter date in the prescribed format.')


def no_of_days(d):

    # Counting days from birth till today.
    total_days = date.today() - d

    # Initialising inflect module.
    on = engine()

    # Returning how old you are in minutes.
    return on.number_to_words(total_days.days * 24 * 60, andword='').capitalize() + ' minutes'


if __name__ == '__main__':
    main()
    