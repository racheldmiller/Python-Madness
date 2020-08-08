# Numbers

Everything comes down to saving space in memory. Eveyrthing we do gets turned into ones and zeros and gets stored in memory.
For example, 1.3333 potentially takes up more space than a whole number.

Python can be used as a calculator, but that's not the only magic it has.

`Integers` are whole numbers, positive or negative.
`Floating points` are also positive or negative, but are decimals. (Referred to as "floats")

| Integer | Floating Point |
| ------- | -------------- |
| 4       | 6.1            |
| 57      | 1.333          |
| -10     | 0.0            |

```
type(9)
<class 'int'>
type(9.0)
<class'float'>
```

# Math

| Symbol | Name             |
| ------ | ---------------- |
| `+`    | Addition         |
| `-`    | Subtraction      |
| `*`    | Multiplication   |
| `/`    | Division         |
| `**`   | Exponentation    |
| `%`    | Modulo           |
| `//`   | Integer Division |

- In Python, divison always returns a float.
- Modulo:
- is kind of like division, but it's the remainder operator.
- Divides a number as many times as it can, and then gives us the remainder.
- `10 % 3 = 1` (because 3x3 = 9; 10-9 = 1)
- `25 % 4 = 1` (because 6x4 = 24; 25-24 = 1)
- Used commonly to figure out if a number is even or odd.
- Integer Division:
- Results as in integer in Python.
- Because it chops off the ending, no float.
- Doesn't round to the nearest whole number; rounds down.
- `10//3 = 3`

# Variables

- Are like containers; it stores data.
- Holds all sorts of things, like numbers, booleans, and strings.
- Like math, it's a symbol that holds a value.
- I'll attach more notes about variables in Python.

# Data Types

In any assignment, assigned value must always be a valid data type.

| Data Type | Description                                                                         |
| --------- | ----------------------------------------------------------------------------------- |
| bool      | Boolean - True or False values                                                      |
| int       | Integer (1, 2, 3)                                                                   |
| str       | String; a sequence of Unicode characters ("Rachel")                                 |
| list      | an ordered sequence of values of other data types [1, 2, 3] or ["a", "b", "c"]      |
| dict      | Dictionary; a collection of key values {"first_name:" "Betty", "last_name": "Boop"} |

