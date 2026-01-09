# Day 2 Notes — Variables \& Data Types



## What is a Variable?



A variable is a **name that refers to a value stored in memory**.

Example:
x = 10

Here:

* x is the variable name
* 10 is the value

---

## Variable Naming Rules



* Must start with a letter or underscore
* Cannot start with a number
* Cannot use spaces
* Case-sensitive (age and Age are different)
* Should be meaningful

Good:
total\_marks, user\_name, age

Bad:
1value, my value, @data

---

## Common Data Types in Python



1. int  
   Example: 10, -5, 100
2. float  
   Example: 3.14, 2.0
3. str  
   Example: "hello", 'Python'
4. bool  
   Example: True, False

Python automatically decides the type — this is called **dynamic typing**.

---

## Checking Data Type



Use:
type(variable)

Example:
type(x)

---

## Taking Input from User



input() always returns a **string**.

Example:
name = input("Enter your name: ")

If you need a number:
age = int(input("Enter your age: "))

---

## Important Concept


Python does NOT need you to declare types explicitly.
Types are decided at runtime.
