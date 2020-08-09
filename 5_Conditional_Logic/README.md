# Getting User Input

There's a built-in function in Python called "input" that will prompt the user and store the result to a variable.

`name = input("Enter your name here: ")`

```
print("What's your favorite color?")
data = input()
print("You said " + data)
```

# Conditional Statements

Conditional logic using if statements represents different paths a program can take based on some type of comparison of input.

```
if some condition is True:
    do something
elif some other condition is True:
    do something
else:
    do something
```

```
name = "Arya Stark"
if name == "Arya Stark":
    print("Valar Morghulis")
elif name == "Jon Snow":
    print("You know nothing")
else:
    print("Carry on)
```

## Multiple Elifs

- You can have as many elifs as you want in a single conditional statement.
- Optional to have an else, but can only have 1, since it's a catch-all statement.

# Truthiness

In Python, all conditional checks resolve to True or False.

```
x = 1
x is 1 # True
x is 0 # False
```

We can call values that will resolve to True "truthy", or values that resolve to False as "falsy".
Besides False conditional checks, other things that are naturally falsy include: empty objects, empty strings, None, and zero.

```
animal = input("enter your favorite animal")

if animal:
    print(animal + " is my favorite, too!")
else:
    print("YOU DIDN'T SAY ANYTHING!)
```

# Comparison Operators

In the examples, a = 1 and b = 1

| Op   | What it does                                  | Example       |
| ---- | --------------------------------------------- | ------------- |
| `==` | Truthy if a has the same value as b           | a==b # True   |
| `!=` | Truthy if a does NOT have the same value as b | a!=b # False  |
| `>`  | Truthy if a is greater than b                 | a > b # False |
| `<`  | Truthy if a is less than b                    | a < b # False |
| `>=` | Truthy if a is grreater than or equal to b    | a >= b # True |
| `<=` | Truthy if a is less than or equal to be       | a <= b # True |

# Logical Operators

In Python, the following operators can be used to make Boolean Logic comparisons or statements:
| Op | What it does | Example |
| ----- | ------------------------------------------------------ | --------------------------------------------- |
| `and` | Truthy if both a AND b are true (logical conjunction) | if a and b: print (c) |
| `or` | Truthy if both a ORR b are true (logical disjunction) | if am_tired or is_bedtime: print("go to sleep") |
| `not` | Truthy if the opposite of a is true (logical negation) | if not is_weekend: print("go to work") |

# is vs. "=="

In Python, "==" and "is" are veryr similar comparators, however, they're not the same.

```
a = 1
a == 1 # True
a is 1 # True
```

```
a = [1,2,3] # a list of numbers
b = [1,2,3]
a == b # True
a is b # False
```

Difference is `==` checks the values to see if they're the same. `is` checks the values to see if they're stored in the same place in memory.

With lists, they could look the same, but they're different instances.

```
c = b
b is c # True
```
