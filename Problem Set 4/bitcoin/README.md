# Bitcoin Price Index


![App Screenshot](https://cs50.harvard.edu/python/2022/psets/4/bitcoin/Bitcoin.svg.png)

Bitcoin is a form of digitial currency, otherwise known as cryptocurrency. Rather than rely on a central authority like a bank, Bitcoin instead relies on a distributed network, otherwise known as a blockchain, to record transactions.

Because there’s demand for Bitcoin (i.e., users want it), users are willing to buy it, as by exchanging one currency (e.g., USD) for Bitcoin.

In a file called bitcoin.py, implement a program that:

* Expects the user to specify as a command-line argument the number of Bitcoins, , that they would like to buy. If that argument cannot be converted to a float, the program should exit via sys.exit with an error message.
* Queries the API for the CoinDesk Bitcoin Price Index at https://api.coindesk.com/v1/bpi/currentprice.json, which returns a JSON object, among whose nested keys is the current price of Bitcoin as a float. Be sure to catch any exceptions, as with code like:

import requests

try:

    ...
except requests.RequestException:

    ...
* Outputs the current cost of  Bitcoins in USD to four decimal places, using , as a thousands separator.

### Hints

* Recall that the sys module comes with argv, per - docs.python.org/3/library/sys.html#sys.argv.
* Note that the requests module comes with quite a few methods, per requests.readthedocs.io/en/latest, among which are get, per requests.readthedocs.io/en/latest/user/quickstart/#make-a-request, and json, per requests.readthedocs.io/en/latest/user/quickstart/#json-response-content. You can install it with:
pip install requests
* Note that CoinDesk’s API returns a JSON response like:
{

   "time":{

      "updated":"May 2, 2022 15:27:00 UTC",
      "updatedISO":"2022-05-02T15:27:00+00:00",
      "updateduk":"May 2, 2022 at 16:27 BST"
   },

   "disclaimer":"This data was produced from the CoinDesk Bitcoin Price Index (USD). Non-USD currency data converted using hourly conversion rate from openexchangerates.org",

   "chartName":"Bitcoin",

   "bpi":{

      "USD":{
         "code":"USD",
         "symbol":"&#36;",
         "rate":"38,761.0833",
         "description":"United States Dollar",
         "rate_float":38761.0833
      },
      "GBP":{
         "code":"GBP",
         "symbol":"&pound;",
         "rate":"30,827.6198",
         "description":"British Pound Sterling",
         "rate_float":30827.6198
      },
      "EUR":{
         "code":"EUR",
         "symbol":"&euro;",
         "rate":"36,800.2764",
         "description":"Euro",
         "rate_float":36800.2764
      }
   }
}

* Recall that you can format USD to four decimal places with a thousands separator with code like:
print(f"${amount:,.4f}")

# How to Test

Here’s how to test your code manually:

* Run your program with python bitcoin.py. Your program should use sys.exit to exit with an error message:
Missing command-line argument   
* Run your program with python bitcoin.py cat. Your program should use sys.exit to exit with an error message:
Command-line argument is not a number
* Run your program with python bitcoin.py 1. Your program should output the price of a single Bitcoin to four decimal places, using , as a thousands separator.
* Run your program with python bitcoin.py 2. Your program should output the price of two Bitcoin to four decimal places, using , as a thousands separator.
* Run your program with python bitcoin.py 2.5. Your program should output the price of 2.5 Bitcoin to four decimal places, using , as a thousands separator.

You can execute the below to check your code using check50, a program that CS50 will use to test your code when you submit. But be sure to test it yourself as well!

check50 cs50/problems/2022/python/bitcoin

Green smilies mean your program has passed a test! Red frownies will indicate your program output something unexpected. Visit the URL that check50 outputs to see the input check50 handed to your program, what output it expected, and what output your program actually gave.

# How to Submit

In your terminal, execute the below to submit your work.

submit50 cs50/problems/2022/python/bitcoin