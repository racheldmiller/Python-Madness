# Food variable stores a randomly chosen food string like "gummy bear" and "morning bun". Print out a string if `food` is a value in `bakery_stock`. If food contained in `bakery_stock`, print out a string of how many items are left: `"3 left"` if food is "toffee cookie" or "1 left" if food is "morning bun", etc.

# This code picks a random food item:
from random import choice
food = choice(["cheese pizza", "quiche",
               "morning bun", "gummy bear", "tea cake"])

bakery_stock = {
    "almond croissant": 12,
    "toffee cookie": 3,
    "morning bun": 1,
    "chocolate chunk cookie": 9,
    "tea cake": 25
}

# SOLUTION WITH "IN"

if food in bakery_stock:
    print("{}left".format(bakery_stock[food]))
else:
    print("We don't make that")
