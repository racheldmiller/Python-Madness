## What is a List?

A collection or grouping of items! (String, floats, boolean values, other lists, dictionaries).
One strucutre, a data structure. A data structure is a higher level up of a data type that'll store other data types inside it.
(Other languages would call a "list" an "array")

```
item1 = "bananas"
item2 = "lego set"
```

^ This would only work if you kept adding the different variables and defining what each one means.

A list allows us to have as many pieces of data we want in a structure. A little database stored inside a Python variable. We could reorder the items, add, delete, etc.

## How are Lists Useful?

A fundamental data strucutre for organizing collections of items.

```
first_task = "install Python"
second_task = "Learn Python"
third_task = "take a break"
```

With these variables, they are unordered and separated. We want them to be associated.

## What Lists Look Like

- The key syntax that we'll see all the time are the square brackets.
- Comma separated values.
- Values do not need to be the same type. You could have a number, boolean, a string, etc.

```
tasks = ["Install Python", "Learn Python", "Take a break"]
OR
tasks = [first_task, second_task, third_task]
```

We could use a variable that references a string and add it in.

## How Many Elements Exist?

`len` stands for "length"
This is useful because let's say you needed to loop through a list. You'd need to know how many items are in the list first.

```
tasks = ["Install Python", "Learn Python", "Take a break"]
len(tasks) #3
```

## Another Way to Make a List

`list()`

```
tasks = list(range(1,4))
```

Another way if you need a list of numbers, so you're not just using a range to loop through things. You can convert the range into a list.

## Accessing Values in a List

```
friends = ["Ashley", "Matt", "Michael"]

print(friends[0]) # 'Ashley'
print(friends[1]) # 'Michael'
```

Like ranges, lists ALWAYS start counting at zero. So the first element lives at index 0.

```
colors = ["purple", "teal", "orange"]
colors[0]
'purple'
the_best = colors[0]
the_best
'purple'

# Note that colors remains unchanged. All this does is retrieve the value.
```
