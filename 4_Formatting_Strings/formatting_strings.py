# Set the variable called `first` to your first name.
# Set the variable `last` to your last name.
# Then set the variable called `formatted` that interpolates both using the .format() method. Make sure you follow this pattern:
# "First Name: __, Last Name: __"

# USING .format()
first = "Rachel"
last = "Miller"

formatted = "First Name: {}, Last Name: {}".format(first, last)

# USING F-STRING
first = "Rachel"
last = "Miller"

formatted = f"First Name: {first}, Last Name: {last}"
