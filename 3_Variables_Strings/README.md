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

# Data Types

In any assignment, assigned value must always be a valid data type.

| Data Type | Description                                                                         |
| --------- | ----------------------------------------------------------------------------------- |
| bool      | Boolean - True or False values                                                      |
| int       | Integer (1, 2, 3)                                                                   |
| str       | String; a sequence of Unicode characters ("Rachel")                                 |
| list      | an ordered sequence of values of other data types [1, 2, 3] or ["a", "b", "c"]      |
| dict      | Dictionary; a collection of key values {"first_name:" "Betty", "last_name": "Boop"} |
