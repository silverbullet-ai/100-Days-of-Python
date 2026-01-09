# Day 12 Notes — List Operations \& Methods



## Adding Elements to a List



1. append()
   Adds an element to the end of the list.



Example:
numbers.append(50)



---

2. extend()
   Adds multiple elements to the list.



Example:
numbers.extend(\[60, 70])



---

3. insert()
   Adds an element at a specific index.



Example:
numbers.insert(1, 15)



---

## Removing Elements from a List



1. remove()
   Removes the first occurrence of a value.



Example:
numbers.remove(20)

⚠ Error if value not found.



---

2. pop()
   Removes and returns an element by index.



Example:
numbers.pop()
numbers.pop(2)



---

## Other Useful Operations



* len(list) → number of elements
* value in list → membership check
* list.count(value) → count occurrences
* list.index(value) → index of first occurrence



---

## Important Note



List methods modify the list **in place**.
They usually return None.

