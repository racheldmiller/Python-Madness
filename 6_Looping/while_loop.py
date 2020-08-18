# Use a while loop to generate a random number between 1 and 100 until you get the number 5. Every time the loop runs, increment the variable i.

# use randint(a, b) to generate a random number between a and b
from random import randint

number = 0  # store random number in here, each time through
i = 0  # i should be incremented by one each iteration

while number != 5:  # Keep looping while number isn't 5
    i += 1
    number = randint(1, 10)  # update number to be a new random
