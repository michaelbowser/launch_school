### 5.6.26

#### Truthiness

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
    else:
        return False

print(is_digit('5'))  # True
print(is_digit('a')) # False
```

True and False values should be implict, not necessarily explicitly written.

#### Short Circuit
Short-circuiting can be defined as an evaluation stops evaluating
sub-expressions once it can determine the final value.

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

