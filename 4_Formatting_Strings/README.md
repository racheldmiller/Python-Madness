There are several ways to format strings in Python to interpolate variables.
The new way (new in Python 3.6+) => F-Strings

```
x = 10
formatted = f"I've told you {x} times already!"
```

```
guess = 8
print(f"your guess of {guess} was incorrect!")

print(f"your guess of {guess + 1} was incorrect!")
which returns as
your guess of 9 was incorrect!

```

The tried-and-true way (Python 2 -> 3.5) => .format method
So the variable doesn't go inside the curly braces, it comes afterward in the parentheses.

```
x = 10
formatted = "Ive told you {} times already!".format(10)
```

The old way => % operator (deprecated)

```
x = 10
formatted = "I've told you %d times already! % (x)
```
