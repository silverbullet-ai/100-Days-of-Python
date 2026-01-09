# Day 21 Notes — Error Handling



## What is an Error?



An error occurs when Python encounters something it cannot execute.

Common runtime errors:



* ValueError
* ZeroDivisionError
* TypeError
* IndexError
* KeyError



---

## try / except



Used to handle errors without crashing the program.



Syntax:


try:
	risky code
except ErrorType:
	handling code



---

## Handling Multiple Exceptions



You can catch different errors separately.



---

## else Block



Runs if no exception occurs.



---

## finally Block



Runs no matter what (error or no error).
Used for cleanup.



---

## Why Error Handling Matters



* Prevents crashes
* Improves user experience
* Makes programs reliable
