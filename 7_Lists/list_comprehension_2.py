# For all numbers between 1 and 100(including 100), create a variable called answer, which contains a list with all the numbers that are divisible by 12. (12,24,etc.)

answer = [val for val in range(1, 101) if val % 12 == 0]

# Given the string "amazing", create a variable called answer, which is a list containing all the letters from "amazing" but not the vowels (a,e,i,o,u). The answer should look like ['m', 'z', 'n', 'g'].

# Using a string (preferable solution):
answer = [char for char in "amazing" if char not in "aeiou"]

# Using a list:
answer = [char for char in "amazing" if char not in [
    "a", "e", "i", "o", "u"]]
