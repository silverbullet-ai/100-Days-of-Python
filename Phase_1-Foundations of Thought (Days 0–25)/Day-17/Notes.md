# Day 17 Notes — Dictionary Methods \& Nested Dictionaries



## Safe Access: get()



Using \[] raises KeyError if key is missing.



Use get():
student.get("name")
student.get("grade", "Not Available")

This avoids crashes.



---

## Common Dictionary Methods



* dict.keys()   → returns keys
* dict.values() → returns values
* dict.items()  → returns key-value pairs
* dict.update() → merge dictionaries
* dict.clear()  → remove all entries
* 

---

## Nested Dictionaries



A dictionary inside another dictionary.



Example:
students = {
"Aahish": {"age": 23, "course": "Python"},
"Swati": {"age": 22, "course": "C++"}
}



Used for:

* User profiles
* API responses
* Configuration files
* 

---

## Iterating Nested Dictionaries



Use nested loops to access inner data.

---

## Key Idea



Dictionaries model **meaningful relationships**, not positions.

