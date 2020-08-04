### Iterating Dictionaries 
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

#### Looping Through Keys
use `.keys()`
`student.keys()` returns things like "name", "owns_dog", "favorite_language", "is_hilarious".

#### Looping Through Values
use `.values()`
```
for value in student.values():
    print(value)
```
returns things like "Rachel", "False", "Python", "True", "my favorite number"

#### Looping Through BOTH
use `.items()`
Write two variables.
```
for key, value in student.items():
    print (key, value)
    
for k, v in student.items():
    print(f" key is {k} and value is {v}")
```
returns things like `key is name and value is Rachel`. 
        
