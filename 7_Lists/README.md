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

### Clear

- Least commonly used.
- Removes all items from the list. Doesn't matter what's in the list.

### Pop

- Remove the item at the given position in the list, and return it.
- If no index specified, removes and returns last item in the list.
- Doesn't completely remove it. Lets you capture value.

```
first_list = [1,2,3,4]
first_list.pop() # 4
first_list.pop(1) # 2

"Please remove whatever's at the index[1]"
```

### Remove

- Works a little differently than the others in that...
  - Remove the first item from the list whose value is x.
- Throws a ValueError if the item is not found.

```
first_list = [1,2,3,4,4,4]
first_list.remove(2)
print(first_list) # [1,3,4,4,4]
```

### index

- returns the index of the specified item in the list
- can specify start and end

```
numbers = [5,6,7,8,9,10]
numbers.index(6) # 1
numbers.index(9) # 4
```

```
numbers = [5,5,6,7,5,8,8,9,10]
numbers.index(5) # 0
numbers.index(5,1) # 1 "Find the index of 5 after 1 (and it's inclusive)"
numbers.index(5,2) # 4
numbers.index(8,6,8) # 6 "Find 8 between the index of 6 and 8"
```

### count

- return the number of times x appears in the list

```
numbers = [1,2,3,4,3,2,1,4,10,2]
numbers.count(2) # 3 How many times does 2 occur? Return the frequency.
numbers.count(21) # 0 (because it doesn't exist)
numbers.count(3) # 2
```

### reverse

- reverse the elements of the list (in-place)

```
first_list = [1,2,3,4]
first_list.reverse()
print(first_list) # [4,3,2,1]
```

### sort

- sort the items of the list (in-place)
- in ascending order (like alphabetically)

```
another_list = [6,4,1,2,5]
another_list.sort()
print(another_list) # [1,2,4,5,6]
```

### join

- not a list method, it's a string method
- commonly used to convert lists to strings
- it takes an iterable argument
- concatenates (combines) a copy of the base string between each item of the iterable
- returns a new string
- can be used to make sentences out of a list of words by joining on a space.

```
words = ['Coding', 'Is', 'Fun!']
' '.join(words) # 'Coding is Fun!'
```

### Slicing

- make new lists using slices of the old list!
- where should we start making cuts, and stop. Are we including every index, or skipping every other one?
  `some_list[start:end:step]`
- similar to `range(start,stop,step)` except you're using colons and square brackets.

#### First Parameter for Slice: start

- what index to start slicing from
- If you enter a negative number, it will start the slice that many back from the end.

```
first_list = [1,2,3,4]
first_list.[1:] # [2,3,4] slice from index(1) to the end.
first_list.[3:] # [4]
```

```
first_list = [-1:] # [4]
first_list.[-3:] # [2,3,4]
```

#### Second Parameter for Slice: end

- The index to copy up to (exclusive counting)
- With negative numbers, how many items to exclude from the end (i.e. indexing by counting backwards)

```
first_list = [1,2,3,4]
first_list.[:2] # [1,2] Assumes to start at 0 index. Doesn't include index(2)
first_list.[:4] # [1,2,3,4]
first_list.[1:3] # [2,3] Index(1) = 2 (inclusive), index(3) = 4 (exclusive)
```

```
first_list = [:-1] # [1,2,3]
first_list = [1:-1] # [2,3]
```

#### Third Parameter for Slice: step

- "step" in Python is basically the number to count at a time
- works the same way as how ranges do
- for example, a step of 2 counts every other number (1,3,5)
- with negative numbers, reverse the order

```
first_list = [1,2,3,4,5,6]
first_list.[1::2] # [2,4,6]
first_list[::2] # [1,3,5]
```

```
first_list[1::-1]= [2,1]
first_list.[:1:-1] # [6,5,4,3] passing in the end point, exclusive.
first_list[2::-1] # [3,2,1]
```

# Swapping Values

```
names = ["James", "Michelle"]
names[0], names[1] = names[1], names[0]
print(names) # ['Michelle', 'James']
```

### When do you need to swap?

- when you're shuffling things
- sorting a list in place
- algorithms
