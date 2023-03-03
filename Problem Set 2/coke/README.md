
# Coke Machine




![App Screenshot](https://cs50.harvard.edu/python/2022/psets/2/coke/coke.png)

Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents and only accepts coins in these denominations: 25 cents, 10 cents, and 5 cents.

In a file called coke.py, implement a program that prompts the user to insert a coin, one at a time, each time informing the user of the amount due. Once the user has inputted at least 50 cents, output how many cents in change the user is owed. Assume that the user will only input integers, and ignore any integer that isn’t an accepted denomination.

# How to Test
Here’s how to test your code manually:

* Run your program with python coke.py. Type 25 and press Enter. Your program should output:
Amount due: 25   
and continue prompting the user for coins.

* Run your program with python coke.py. Type 10 and press Enter. Your program should output:
Amount due: 40
and continue prompting the user for coins.

* Run your program with python coke.py. Type 5 and press Enter. Your program should output:
Amount due: 45
and continue prompting the user for coins.

* Run your program with python coke.py. Type 30 and press Enter. Your program should output:
Amount due: 50
because the machine doesn’t accept 30-cent coins! Your program should then continue prompting the user for coins.

* Run your program with python coke.py. Type 25 and press Enter, then type 25 again and press Enter. Your program should halt and display:
Change owed: 0
* Run your program with python coke.py. Type 25 and press Enter, then type 10 and press Enter. Type 25 again and press Enter, after which your program should halt and display:
Change owed: 10

You can execute the below to check your code using check50, a program that CS50 will use to test your code when you submit. But be sure to test it yourself as well!

check50 cs50/problems/2022/python/coke

Green smilies mean your program has passed a test! Red frownies will indicate your program output something unexpected. Visit the URL that check50 outputs to see the input check50 handed to your program, what output it expected, and what output your program actually gave.

# How to Submit
In your terminal, execute the below to submit your work.

submit50 cs50/problems/2022/python/coke