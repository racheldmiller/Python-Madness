# ask for age
age = input("How old are you: ")
if age:
    age = int(age)
    # if age >= 18 and age < 21:  # we don't want <= 21 b/c if you're 21, you can drink.
    # print("You can enter, but you'll need a wristband!") this won't work because we're comparing strings when we need int.
    if age >= 18 and age < 21:  # we don't want <= 21 b/c if you're 21, you can drink
        print("You can enter, but you'll need a wristband!")
    # 18-21 wristband
    # 21+ drink, normal entry
    elif age >= 21:
        print("You can enter AND drink!")
    # too young, sorry
    else:
        print("You're too young, sorry! :(")
else:
    print("Please enter an age!")

    # will experience a problem if you enter no value, just a space.
