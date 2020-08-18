donations = dict(sam=25.0, jessica=88.99, gary=13.0,
                 cyrus=99.5, katherine=150.0)

# Loop to calculate the total value of donations. Save it to a variable called total_donations.

# Loop over donations, add all values together and store it in a value called total_donations.

total_donations = 0
for donation in donations.values():
    total_donations += donation

# Advanced Solutions
total_donations = sum(donation for donation in donations.value)

# or
total_donations = sum(donations.values())
