# actually_sick = have the flu
# kinda_sick = feeling under the weather but want to take a day off
# hate_your_job =  work sucks

# sick_days = random number between 0-10.
# calling_in_sick = True or False

# True if
# - you're actually_sick and have sick_days remaining
# - you're kinda_sick and hate_your_job and have sick_days remaining

from random import choice, randint

# randomly assigns values to these four variables
actually_sick = choice([True, False])
kinda_sick = choice([True, False])
hate_your_job = choice([True, False])
sick_days = randint(0, 10)

calling_in_sick = None  # set this to True or False with Boolean Logic and Conditionals!

if actually_sick and sick_days > 0:
    calling_in_sick = True
elif kinda_sick and hate_your_job and sick_days > 0:
    calling_in_sick = True
else:
    calling_in_sick = False
