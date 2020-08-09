# Randomly picks a number between 1 and 10 and saves it to a variable called choice.
# Write a conditional to check if `choice` is 7. If `choice` is 7, print out "lucky". Otherwise, print "unlucky".

from random import randint
choice = randint(1, 10)

if choice == 7:
    print("lucky")
if choice != 7:
    print("unlucky")
