# Day 22 Notes — File Handling



## What is File Handling?



File handling allows a program to:

* Read data from files
* Write data to files
* Store information permanently



---

## Opening a File



Syntax:
file = open("filename", "mode")



Common modes:

* "r" → read
* "w" → write (overwrites file)
* "a" → append
* "r+" → read \& write



---

## Reading Files



* read() → reads entire file
* readline() → reads one line
* readlines() → reads all lines into a list



---

## Writing Files



* write(text)
* writelines(list)



---

## with Statement (BEST PRACTICE)



Automatically closes the file.



Example:
with open("file.txt", "r") as file:
content = file.read()



---

## Why Use with?



* No need to close file manually
* Prevents memory leaks
* Cleaner and safer code
