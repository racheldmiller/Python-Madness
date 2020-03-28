# First question should ask user how many km did they cycle
print("How many kilometers did you cycle today?")

# 1 km = 1.60934 mi.
# create 2 variables, kms and mi.

kms = input()  # store user's input into a variable, kms
miles = (float(kms)/1.60934)  # take the kms and convert it to mi.
miles = round(miles, 2)  # round the miles to 2 decimal places

print(f"Your {kms}km ride was {miles}mi  ")  # use f string
