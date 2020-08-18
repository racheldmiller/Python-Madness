# List called `sounds`.
# sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]
# Write code that loops over the list and adds the strings together to form one large combined string.
# Save in CAPS and in a variable called `result`

sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]
# Define your code below:
result = ''
for s in sounds:
    result += s.upper()


# Or, add all strings to result, and then capitalize the whole thing once at the end.

sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]
# Define your code below:
result = ''
for s in sounds:
    result += s
result = result.upper()
