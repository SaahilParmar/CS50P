from requests import get
from sys import argv, exit

# Getting price request of bitcoin from site.
bitcoin = get('https://api.coindesk.com/v1/bpi/currentprice.json').json()

# When command-line argument is less than or more than 2.
if len(argv) != 2:
    exit('Missing command-line argument')

# Trying for a integer input in command-line.
try:
    # Converting inputted number to float with current bitcoin price & printing it till 4 values after decimal.
    print(f"${(float(argv[1]) * bitcoin['bpi']['USD']['rate_float']):,.4f}")

# When 2nd command-line argument is not a number.
except ValueError:
    exit('Command-line argument is not a number.')
          