# Iterating Dictionaries

```
student = {
"name": "Rachel",
"owns_dog": False,
"favorite_language": "Python",
"is_hilarious": True,
27: "my favorite number"
}
```

Iterating over a list is more straightforward because a list on its own is already iterable.
Examples: `for num in numbers`, `for color in colors`

With a dictionary, if we wanted to print every single piece of information out, every value, we'd have to do:

```
print(student["name"])
print(student["owns_dog"])
```

There's a few different methods to access all values in a dictionary. We can:

- Loop through `keys`
- Loop through `values`
- Loop through both at the same time.

## Looping Through Keys

use `.keys()`
`student.keys()` returns things like "name", "owns_dog", "favorite_language", "is_hilarious".

## Looping Through Values

use `.values()`

```
for value in student.values():
    print(value)
```

returns things like "Rachel", "False", "Python", "True", "my favorite number"

## Looping Through BOTH

use `.items()`
Write two variables.

```
for key, value in student.items():
    print (key, value)

for k, v in student.items():
    print(f" key is {k} and value is {v}")
```

returns things like `key is name and value is Rachel`.

There are some other methods that make things even simpler!

## Clear

Clears all the keys and values in a dictionary.
Leaves you with a hollow shell of what was there before.

```
d = dict (a=1, b=2, c=3)
d.clear()
d # {}
```

## Copy

Makes a copy of the dictionary.

```
d = dict (a=1, b=2, c=3)
d.copy()
c = d.copy()
c # {'a':1, 'b':2, 'c': 3}
c is d # False
```

Just like when copying lists, they look the same and double equals. If we use "is", they are unique objects in memory. They're not stored in the same place.

== is the test for equality.
"is" is the test for equality... in memory. They're not referencing the exact same place in memory.

## fromkeys

creates key-value pairs from comma separated values.

```
{}.fromkeys("a", "b") #{'a':'b'}
{}.fromkeys("a,[1,2,3,4,5])#{'a':[1,2,3,4,5]}
```

Call it on an empty dictionary or on dict.
If we have a bunch of keys that we're trying to set up to a default value.

```
new_user = {}.fromkeys(['name', 'score', 'email', 'profile bio'], 'unknown')
```

Used to create default dictionaries to assign initial starting values

```
new_user.fromkeys(['phone'], 'unknown')
```

will create a new dictionary, even if there's an existing one.

## Get

Retrieves a key in an object and returns None instead of a KeyError if the key does not exist.

```
d= dict (a=1, b=2, c=3)
d['a'] #1
d.get('a') #1 d['b] #2
d.get('b') #2
```

# Dictionary Methods: Pop, Popitems, and Update

### pop

Takes a single argument corresponding to a key and removes that key-value pair from the dictionary. Returns the value corresponding to the key that was removed.

```
d = dict(a=1, b=2, c=3)
d.pop() # TypeError: pop expected at least 1 arguments, got 0
d.pop('a') #1
d # {'c': 3, 'b': 2}
d.pop('e') # KeyError
```

### popitem

Removes a random key in a dictionary:

```
d = dict(a=1, b=2, c=3, d=4, e=5)
d.popitem() # ('d', 4)
d.popitem('a') # TypeError: popitem() takes no arguments (1 given)
```

### update

Update keys and values in a dictionary with another set of key value pairs.

```
first = dict(a=1, b=2, c=3, d=4, e=5)
second = {}

second.update(first)
second # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e':5}

# let's overwrite an existing key
second['a'] = "AMAZING"

# if we update again
second.update(first) # {'a':1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# the update overrides our values
second # {'a':1, 'b': 2, 'c':3, 'd':4, 'e':5}
```

# Dictionary Comprehension

Instead of brackets, we use dictionary brackets.

`{__:__ for __in__}`

- iterates over keys by default
- to iterate over keys and values using .items()

```
numbers = dict(first =1, second=2, third=3)
squared_numbers = {key: value ** 2 for key,value in numbers.items()}
print(squared_numbers) # {'first': 1, 'second': 4, 'third':9}
```

Making a dictionary, but starting with a list.

```
{num: num**2 for num in [1,2,3,4,5]}
```

This time we have two strings.

```
str1 = "ABC"
str2 = "123"
combo = {str1[i]: str2[i] for i in range(0,len(str1))}
print(combo) # # {'A': '1', 'B': '2', 'C': '3'}
```

### conditional logic with dictionaries

```
num_list = [1,2,3,4]
{ num:("even" if num % 2 == 0 else "odd") for num in num_list}
# {1: 'odd', 2: 'even', 3: 'odd', 4: 'even'}
```
