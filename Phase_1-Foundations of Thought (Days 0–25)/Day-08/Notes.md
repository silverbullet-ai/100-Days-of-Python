# Day 8 Notes — Functions


## Why Functions?



Functions allow us to:

* Reuse code
* Avoid repetition
* Organize logic
* Make programs easier to read and maintain



Instead of writing the same logic again and again,
we define it once and reuse it.



---

## Defining a Function



Syntax:

def function\_name():
statements



* def → keyword to define a function
* function\_name → name of the function
* () → parameters (if any)



---

## Calling a Function



A function runs only when it is **called**.



Example:
function\_name()



---

## Parameters and Arguments



* Parameters → variables in function definition
* Arguments → values passed during function call



Example:
def greet(name):      # name is parameter
print("Hello", name)

greet("Aahish")       # "Aahish" is argument



---

## return Statement



* Sends a value back to the caller
* Ends function execution



Example:
def add(a, b):
return a + b

result = add(3, 4)


---

## Important Difference

* print() → displays output
* return → gives value back for further use
