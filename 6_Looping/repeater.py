times = input(
    "How many times would you like to see your affirmation? ")  # string
times = int(times)  # because we need to convert this to an int

# VERSION 1
# for time in range(times):
#     print("YOU ARE A POWERFUL HUMAN BEING!")

# VERSION 2
# the +1 prevents the "time" from displaying "time 0:"
for time in range(times):
    print(f"time {time+1}: YOU ARE A POWERFUL HUMAN BEING!")
