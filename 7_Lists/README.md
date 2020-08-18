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

## Accessing Values from the End

```
friends = ["Ashley", "Matt", "Michael"]

print(friends[-1]) # 'Michael'
print(friends[-3]) # 'Ashley'
```

You can use a negative number to index backwards.

## Check if a Value is in a List

```
friends = ["Ashley", "Matt", "Michael"]

"Ashley" in friends # True
"Colt" in friends # False
```

Capitalization matters.

## Accessing All Values in a List

```
numbers = [1,2,3,4]

print(numbers[0]) #1
print(numbers[1]) #2
print(numbers[2]) #3
print(numbers[3]) #4
```

Could print out each value... OR use a loop

FOR LOOP

```
numbers = [1,2,3,4]

for number in numbers:
    print(number)
#1
#2
#3
#4
```

WHILE LOOP

```
numbers = [1,2,3,4]
i = 0

for i < len(numbers):
    print(numbers[i])
    i += 1 # Otherwise, you'll get an infinite loop
#1
#2
#3
#4
```

If all you want to do is print out data or access data directly from inside the list, use a for loop because it's cleaner and shorter.
Something more complicated would require having the index accessible, which isn't available in the for loop by default.

# List Methods

A method is a type of function, but significant distinction. For the ones specific to lists, you append the `.(<METHOD NAME>)` to the list name.

### Append

Add an item to the end of the list.

```
first_list = [1,2,3,4]
first_list.append(5)
print(first_list) # [1,2,3,4,5]
```

### Extend

Add to the end of a list all values passed to extend.

```
first_list = [1,2,3,4]
first_list.append([5,6,7,8])
print(first_list) # [1,2,3,4, [5,6,7,8]]
correct_list = [1,2,3,4]
correct_list.extend([5,6,7,8])
print(correct_list) # [1,2,3,4,5,6,7,8]

```

Adding 1 item to the end of the list, use append. More than 1 at the end, use extend. Otherwise, use insert.

### Insert

Insert an item at a given position.
First thing you provide is the index you want to add the new data to, followed by what you want to add.

```
first_list = [1,2,3,4]
first_list.insert(2, "Hi!")
print(first_list) # [1,2,"Hi!"]
```
