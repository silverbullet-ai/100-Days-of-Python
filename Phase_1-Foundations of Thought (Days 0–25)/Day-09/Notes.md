# Day 9 Notes — Function Arguments



## Positional Arguments



Arguments passed based on position.



Example:
def add(a, b):
return a + b

add(2, 3)   # a=2, b=3

Order matters.



---

## Default Arguments



Provide a default value to a parameter.



Example:
def greet(name="User"):
print("Hello", name)

greet()           # uses default
greet("Aahish")   # overrides default



---

## Keyword Arguments



Arguments passed using parameter names.



Example:
def student(name, age):
print(name, age)

student(age=21, name="Aahish")

Order does NOT matter.



---

## Mixing Arguments (Important Rule)



* Positional arguments → first
* Keyword arguments → after positional



Correct:
func(10, b=20)

Wrong:
func(a=10, 20)



---

## Why Keyword Arguments Matter



* Improves readability
* Avoids mistakes
* Safer for long parameter lists
