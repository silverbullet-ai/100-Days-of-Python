# Day 18 Notes — Strings (Advanced)



## Strings as Sequences



Strings behave like sequences:

* Indexed
* Sliceable
* Iterable



But they are **immutable**.



---

## Common String Methods



* upper() → convert to uppercase
* lower() → convert to lowercase
* title() → title case
* strip() → remove leading/trailing spaces
* replace(old, new)
* split(separator)
* join(iterable)



---

## String Slicing



Same rules as lists:

text\[start:end:step]



Example:
text\[1:5]
text\[::-1]  → reverse string



---

## String Formatting



1. f-strings (recommended)
   Example:
   name = "Aahish"
   age = 22
   f"My name is {name} and I am {age} years old"
   
2. format()
   "My name is {} and I am {}".format(name, age)



---

## Important Note



Strings cannot be modified in place.
Every operation creates a **new string**.

