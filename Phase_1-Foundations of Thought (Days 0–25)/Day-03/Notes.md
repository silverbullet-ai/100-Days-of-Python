# Day 3 Notes — Operators \& Expressions



## What is an Operator?



An operator is a symbol that performs an operation on values (operands).

Example:
a + b

Here:



* \+ is the operator
* a and b are operands



---

## Arithmetic Operators



\+   Addition

\-   Subtraction

\*   Multiplication  
/   Division  
//  Floor division  
%   Modulus  
\*\*  Exponentiation



Example:
10 // 3 → 3  
10 % 3 → 1

---

## Assignment Operators



=   Assign  
+=  Add and assign  
-=  Subtract and assign  
\*=  Multiply and assign  
/=  Divide and assign



Example:
x = 5  
x += 2  → x becomes 7

---

## Comparison Operators



==  Equal to  
!=  Not equal to

>   Greater than  
<   Less than  
>=  Greater than or equal  
<=  Less than or equal  

Result is always Boolean (True or False).

---

## Logical Operators



and  → True if both conditions are True  
or   → True if at least one condition is True  
not  → Reverses the condition

Example:
age > 18 and is\_student == True

---

## Operator Precedence



Python follows a priority order:

1. ()
2. \*\*
3. \*, /, //, %
4. +, -
5. Comparison operators
6. not
7. and
8. or

Parentheses () can be used to control order.

