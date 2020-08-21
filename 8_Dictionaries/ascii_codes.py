# Every character has an ASCII code (basically, a number that represents it.) Python has a function called chr() that will return a string if you provide the corresponding integer ASCII code. For example: `chr(65)` will return 'A'. `chr(66)` will return 'B' all the way up to `chr(90` will return 'Z'.

answer = {count: chr(count) for count in range(65, 91)}
