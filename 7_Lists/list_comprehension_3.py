# Using a nested list comprehension and range(), create a variable called `answer` with the following value - [[0,1,2], [0,1,2], [0,1,2]]. To break it down... start by using range and a list comp to generate the list [0,1,2]. And then repeat that whole thing back 3 times in a nested list comp.

answer = [[i for i in range(0, 3)] for num in range(0, 3)]

# Using list comprehension, create a variable called answer with the following value:
# [
#     [0,1,2,3,4,5,6,7,8,9],
#     [0,1,2,3,4,5,6,7,8,9],
#     [0,1,2,3,4,5,6,7,8,9],
#     [0,1,2,3,4,5,6,7,8,9],
#     [0,1,2,3,4,5,6,7,8,9],
#     [0,1,2,3,4,5,6,7,8,9],
#     [0,1,2,3,4,5,6,7,8,9],
#     [0,1,2,3,4,5,6,7,8,9],
#     [0,1,2,3,4,5,6,7,8,9],
#     [0,1,2,3,4,5,6,7,8,9],
# ]

answer = [[i for i in range(0, 10)] for num in range(0, 10)]
