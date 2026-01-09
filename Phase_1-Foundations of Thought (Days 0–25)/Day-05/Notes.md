# Day 5 Notes — Loops


## Why Loops?


Loops allow us to **repeat a block of code** without writing it multiple times.

Instead of:
print("Hello")
print("Hello")
print("Hello")

We use a loop.



---

## while Loop



The while loop runs **as long as a condition is True**.



Syntax:


while condition:
statement

Important:



* Condition must eventually become False
* Otherwise, it becomes an infinite loop



---

## for Loop



The for loop is used to **iterate over a sequence**.

Commonly used with range().



Syntax:


for variable in range(start, stop):


statement



range(start, stop):



* start → inclusive
* stop → exclusive



---

## break Statement



Used to **exit the loop immediately**, even if the condition is True.



---

## continue Statement



Used to **skip the current iteration** and move to the next one.



---

## Key Difference



* while → condition-based loop
* for → sequence-based loop
