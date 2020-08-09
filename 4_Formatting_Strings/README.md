# Formatting Strings

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

# Strings and Indexes (Indicies?)

```
name = "Chuck"
name[0] = 'C'
name[4] = 'k'
```

# Converting Data Types

Note: Don't name any of your variables 'int', 'str', etc.

In string interpolation, data types are implicitly converted into string form (more on this later in OOP).
You can also explicitly convert variables by using the name of the built-in type as a function (more on functions later):

```
decimal = 12.56345634534
integer = int(decimal) #12
```

```
my_list = [1,2,3]
my_list_as_a_string = str(my_list) # "[1,2,3]"
```

```
num = 12
type(num) <-- int
num = float(num)
type(num) <-- float
```
