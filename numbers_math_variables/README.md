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

For instance, If I were to go into my terminal and type `type(9)`, it'll return that it's an integer. 9.0 would return it's a float.

```
type(9)
<class 'int'>
type(9.0)
<class'float'>
```

If you do math with an integer + a float, Python will return a float back.

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
  - Example: If you do 1/2, it's 0.5. (A float!)

There is an order of operations for Python. PEMDAS!
P - Parentheses
E - Exponents
M - Multiplication
D - Division
A - Addition
S - Subtraction

In my terminal, if I were to do `1 + 2 * 5 / 3`, it'll look at `2 * 5` first, before `/3`, followed by `+1`. = 4.3333...
We could alter it by adding in parentheses: `(1 + 2) * 5 / 3` = 5.0

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
  - `6//7 = 0`
  - Not commonly used.
