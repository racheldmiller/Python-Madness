# For Loops

- Have a collection of data we can iterate or loop through.
- We want to do something FOR every item in this list, for every character in this string, for every number in the range.
- item is a new variable that can be called whatever you want.
- item references the current position of our iterator within the iterable. It will iterate over (run through) every item of the collection and then go away when it has visited all items.

In Python, for loops are written like this:

```
for item in iterable_object:
    # do something with item
```

```
[40, 32, 73]
for char in "hello":

range(1,10)
```

# For loops with ranges

Let's print numbers 1-7 using our knowledge of looping through ranges.

```
for number in range(1,8):
    print(number)
```

```
for x in range(1,10):
    print(x)
    print(x*x)
```

```
for letter in "coffee":
    print(letter)
```

# Ranges

- We need to know for loops to use ranges. We also need to know ranges to use for loops.
- Generating sequences of numbers that are ordered in a particular way. Not random.
- If we just want to print numbers, we can simply iterate over a range.
- A range is just a slice of the number line.

Range(7) gives you integers from 0 through 6. Count starts at 0 and is exclusive. Doesn't contain 7.
Range(1,8) will give you integers from 1 to 7. Starts at 1, includes 1, but doesn't include 8. Two parameters are (start,end)
Range(1,10,2) will give you odds from 1 to 10. Third param is called the "step", meaning how many to skip. Also, which way to count: up+ or down-.
Range(7,0,-1) will give you integers from 7 to 1.

```
range(10)
range(0,10)
list(r)
[0,1,2,3,4,5,6,7,8,9]
nums = range(1,10,2)
nums
range(1,10,2)
list(nums)
[1,3,5,7,9]
```

for num in range(10):
print(num)

for num in range(10,20,2):
print(num)

# while loops

- Both for and while loops can be used to iterate over a collection or to repeat something 10x.
- Anything you can do with a for loop, you can do with a while loop.

```
while im_tired:
    # seek caffeine
```

- While loops continue to execute while a certain condition is truthy, and will end when they become falsy.

```
user_response = None
while user_response != "please":
    user_response = input("Ah ah ah, you didn't say the magic word: ")
```

- while loops require more careful setup than for loops, since you have to specify the termination conditions manually.
- Be careful! If the condition doesn't become false at some point, your loop will continue forever.

```
msg = input("what's the secret password?")
while msg != "bananas":
    print("WRONG!")
    msg = input("what's the secret password?")
print("CORRECT!")
```

```
for num in range(1,11):
    print(num)

num = 1
while num < 11:
    print(num) <-- this will create an infinite loop because 1 is < 11.
```

- with a while loop, you have to declare the variable first.
- while loop example will be fine if you add `num += 1` on the next line after print.
