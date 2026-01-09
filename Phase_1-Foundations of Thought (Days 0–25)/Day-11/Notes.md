# Day 11 Notes — Lists



## Why Lists?



Lists allow us to store **multiple values in a single variable**.

Instead of:
a = 10
b = 20
c = 30



We use:
numbers = \[10, 20, 30]



---

## Creating a List



Syntax:
list\_name = \[value1, value2, value3]



Lists can store:

* Integers
* Floats
* Strings
* Mixed data types



Example:
data = \[1, 2.5, "Python", True]



---

## Indexing



Lists are **zero-indexed**.



Example:
numbers = \[10, 20, 30]

numbers\[0] → 10  
numbers\[1] → 20



Negative indexing:
numbers\[-1] → last element



---

## Modifying Lists



Lists are **mutable**, meaning they can be changed.



Example:
numbers\[1] = 50



---

## Iterating Over a List



Use a for loop to access each element.



Example:
for item in numbers:
print(item)



---

## Key Concept



Lists store **references to objects**, not copies.

