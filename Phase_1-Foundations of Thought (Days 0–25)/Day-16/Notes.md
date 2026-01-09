# Day 16 Notes — Dictionaries



## What is a Dictionary?



A dictionary stores data as **key–value pairs**.



Example:
student = {
"name": "Aahish",
"age": 22,
"course": "Python"
}



---

## Dictionary Characteristics



* Unordered (conceptually)
* Keys must be unique
* Keys must be immutable (string, number, tuple)
* Values can be anything
* Mutable (can be changed)



---

## Accessing Values



Use keys, not indices.



Example:
student\["name"]

⚠ Accessing a non-existing key causes KeyError.



---

## Adding \& Updating Values



Add new key:
student\["city"] = "Gaya"



Update existing key:
student\["age"] = 23



---

## Removing Entries



* del dict\[key]
* pop(key)



---

## Iterating Over Dictionaries



* for key in dict
* for value in dict.values()
* for key, value in dict.items()



---

## When to Use Dictionaries



* Structured data
* Lookup tables
* Configurations
* API / JSON data
