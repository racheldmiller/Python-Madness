# Variables

- Are like containers; it stores data that you can pull out later.
- Holds all sorts of things, like numbers, booleans, and strings.
- Like math, it's a named symbol that holds a value.

```
x = 100
khaleesi_mother_of_dragons = 1
print(khaleesi_mother_of_dragons + x)
101
```

- Variables are always assigned with the variable name on the left and the value on the right of the equals sign.
- Variables must be assigned before they can be used.

In my terminal, if I were to do: `num_of_cats = 99`, when I enter `num_of_cats`, Python returns `99`.
`print(num_of_cats)` returns `99`.

## Variable Assignment

Variables can be:

- Assigned to other variables.
- Reassigned at any time.
- Assigned at the same time as other variables.

```
python_is_awesome = 100
just_another_var = python_is_awesome
python_is_awesome = 1337
all, at, once = 5, 10, 15 <-- only makes sense if it's being assigned together, because it treats it respectively.
```

# Naming Restrictions

In Python, you can name variables whatever you like, but with some restrictions:

1. Must start with a letter or underscore.
2. Rest of the name must consist of letters, numbers, or underscores.
3. Names are case-sensitive.
   `Cats != cats`

Most variables are snake_case. camelCase is ok, but hello, Python? Snake?
`dog_name = "Lucky"`

CAPITAL_SNAKE_CASE refers to a constant. So it won't change.
`THIS_IS_PI = 3.14`

Upper CamelCase usually refers to a class.

Variables that start and end with two underscores is called "dunder"

- Dunder = double underscore
- Supposed to be private or left alone.
- Common for open source code. Don't tamper with it; it could mess up the application.
  `__no_touchy_my_code__`

# Data Types

In any assignment, assigned value must always be a valid data type. Python data types include: (also includes floats.)
Reminder: You can use `type(<insert variable name>)` in Terminal to return what kind of `<class '???'>` it is.

| Data Type | Description                                                                         |
| --------- | ----------------------------------------------------------------------------------- |
| bool      | Boolean - True or False values                                                      |
| int       | Integer (1, 2, 3)                                                                   |
| str       | String; a sequence of Unicode characters ("Rachel")                                 |
| list      | an ordered sequence of values of other data types [1, 2, 3] or ["a", "b", "c"]      |
| dict      | Dictionary; a collection of key values {"first_name:" "Betty", "last_name": "Boop"} |

For booleans, Python only recognizes uppercase True or False. If it's lowercase, it's no longer a boolean.

# Dynamic Typing

Python is highly flexible about reassigning variables to different types:

```
awesomeness = True
print (awesomeness) # True

awesomeness = "a dog" <-- changing from boolean to a string
print (awesomeness) # a dog

awesomeness = None <-- change from a string to "nothing"
print(awesomeness) # None

awesomeness = 22 / 7 <-- change from "nothing" to a float
print(awesomeness) # 3.14285714...
```

We call this dynamic typing, since variables can change types readily.
Other languages, such as C++, are statically-typed, and variables are stuck with their originally-assigned type:
... Meaning if something is a boolean, it stays as a boolean. You'd have to create a brand new variable.

```
int not_awesomeness = 5;
not_awesomeness = "cool"; // !Error
```

# None

- Python's `None` is other languages' version of `null`.
- If I were to do `print(child)`, it'll return `None`.
- None means there's no value, but there could be. (Rather than just using 0 or False)

```
name = "Daisy"
age = 30
child = None
```

# Declaring Strings

- String literals in Python can be declared with either single or double quotes.
- Doesn't matter, but needs to be consistent with the convention throughout the same file.
- If you're using a quote inside of a quote, then you'll need to use both: `msg = "he said 'hello there!'"` (or vice-versa)

# String Escape Characters (Escape Sequences)

- In Python, there are also "escape characters", which are "metacharacters" - they get interpreted by Python to do something special: `\`
  (Check Python documentation for a complete table of the different options.)

```
new_line = "hello \n world"
print (new_line)
# hello
# world
```

# String Concatenation

- Concatenation is combining multiple strings together. In Python, you can simple do this with the "+" operator.
- Only works with strings.

```
str_one = "your"
str_two = "face"
str_three = str_one + " " + str_two # your face
```

```
username = "bluethecat"
print("Hello there and welcome to the game, " + username)
returns --> Hello there and welcome to the game, bluethecat
```

- You can also use the "+-" operator!
- Can use this with integers.

```
str_one = "ice"
str_one += " cream"
str_one # ice cream
```

```
people = 99
people += 1
people
100
```
