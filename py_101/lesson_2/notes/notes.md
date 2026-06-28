### 5.6.26, 6.28.26 (2nd run)

#### Style Guide

 - Text editor uses characters, not tabs, for indentation. Also, spaces for 
tabs.
 - Limit lines to 72 characters
 - Use `snake_case` for function and variable names. Start with a lower case 
 letter.
 - Class names use `PascalCase`.
 - Uppercase names with underscores to represent constants. Ex: `UPPER_CASE`
 - This is also known as `SCREAMING_SNAKE_CASE`


#### Truthiness
 - A boolean is a data type whose only purpose is to convey whether it is 
 true or false.
``` 
print(True)
print(False)

def make_longer(string, longer):
    if longer:
        return string + string
    else:
        return string

print(make_longer("abc", True)) # 'abcabc'
print(make_longer("xyz", False)) #'xyz'

def is_digit(char):
    if '0' <= char <= '9':
        return True
    els
        return False

print(is_digit('5'))  # True
print(is_digit('a')) # False

```

In much the same way, a function doesn't usually return True or False
explicitly. Instead, it returns the result of a conditional expression. 

True and False values should be implicit, not necessarily explicitly written.

#### Short Circuit
Short-circuiting can be defined as an evaluation stops evaluating
sub-expressions once it can determine the final value.
 - The `and` operator evaluates as `True` only when both sub-expressions
 evaluate as `True`.
 - The `or` operator evaluates as `True` when one of the stow sub-expressions
 evaluate as `True`; it evaluates as `False` when both sub-expressions 
 evaluate as `False`.
 - The **not** operator inverts the truth value of the condition it's applied
 to.

For example:
```
print(False and len(None)) #False 
```
From text:
This type of conditional expression often appears in real-life Python code,
so get familiar with it. In particular, make sure that you understand that
Python doesn't evaluate the right side of a short-circuit operator when the
expression short-circuits.

The following values evaluate as:<br>
- False
- None
- 0
- 0.0
- 0j
- "" (an empty string)
- [] (an empty list)
- {} (an empty dictionary)
- () ( an empty tuple)
- set() ( an empty set)
- frozenset() (an empty frozenset)
range(0) (an empty range)

#### Pseudocode
Pseudocode for a function that determines which number in a collection has the 
greatest value.
- Given a collection of numbers 

  - Iterate through the collection one by one.
    - save the first value as the starting value.
    - for each iteration, compare the saved value with the current value.
      - if the current number is greater 
        - reassign the saved value as the current value 
      - otherwise, if the current value smaller or equal
        move to the next value in the collection
  - After iterating through the collection, return the saved value

Two layers to solving any problem:
  - The logical problem domain layer.
  - The syntactical programming language layer.

Pseudocode Keywords

|Keyword | Meaning |
|-------|--------|
| START | start of the program |
| SET | set a variable that we can use for later |
| GET | retrieve input from user |
| PRINT | display output to user |
| READ | retrieve a value from a variable |
| IF / ELSE IF / ELSE | show conditional branches in logic |
| WHILE | show looping logic |
| END | end of the program 

