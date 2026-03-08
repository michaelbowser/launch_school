# Data_types
# Exercise 1
#
# 'True' is a string data type
# False is a bool data type
# (1,2,3) is a tuple data type
# 1.5 is a float data type
# [1, 2, 3] is a list data type
# 2 is an int data type
# range(5) is a range data type
# {1, 2, 3} is a set data type
# None is a None class data type
# {'foo': 'bar'} is a dict data type with string data types as the key and value
#
# Exercise 2
#
# names = ('Asta', 'Butterscotch', 'Pudding', 'Neptune', 'Darwin')
#
# Exercise 3
# pets = {'Asta': 'dog', 'Butterscotch': 'cat', 'Pudding': 'cat', 'Neptune': 'fish', 'Darwin': 'lizard'}
#
#
# Errors
# 
# Exercise 1: None is a NoneType
# Exercise 2: All good
# Exercise 3: put a comma after the last value
# Exercise 4:
# Exercise 

# Basic Operations
# Exercise 1 
# mike = 'Mike' + ' ' + 'Bowser'
#
#
#
#
#
#
#
# Exercise 3 
# print('5' + '10') concatenates 5 + 10. It does convert them to ints and add them.

# Exercise 4 
# print('1' + '5')
# 
# Exercise 5 
# print(int('5') + int('10'))
# Exercise 6 
# Yes, an error will occur. It will return 'IndexError: list index out of range'. There are no indexes for nonexistent values.

# Exercise 6 
# This evaluates to the bool value False. The strings are not equivalent because the one is capitalized and the other is not.

# Exercise 7
# The code returns 'ValueError: invalid literal for int() with base 10: '3.1415'. An int() can coerce an integer of string type but not of float() type.
# Exercise 8
# The expression evaluates to True as the string on the left's first character is 1 and the first character of the string on the right is 9.


# Variables

# Exercise 1 
# idiomatic, non-idiomatic, idiomatic, non-idiomatic,non-idiomatic,idiomatic, non-idiomatic, non-idiomatic

# Exercise 2 
# idiomatic, non-idiomatic, idiomatic, non-idiomatic, illegal, idiomatic, non-idiomatic, non-idiomatic
#
# Exercise 3 
# non-idiomatic, non-idiomatic, non-idiomatic, idiomatic, illegal, non-idiomatic, idiomatic, non-idiomatic
# Exercise 4 
#  non-idiomatic, non-idiomatic, idiomatic, illegal, non-idiomatic,non-idiomatic, non-idiomatic

# Exercise 5 
# print(f' Good Morning, {name}. \n Good Afternoon, {name}. \n \
# Good Evening, {name}.')

# Exercise 6 
#
# Exercise 7
# It prints the literal string and then the string value assigned to the constant NAME

# Exercise 8

# Exercise 9

# Exercise 10
# reassign, mutate,reassign, neither, mutate, mutate, mutate,
# mutate, mutate, mutate
#
# Input/Output
#
# Exercise 1 
#
#
# Functions and Methods
#
# 1 
# A. Type: Str 
# B.Mutability: Immutable 
# C. Operations: function definition set_foo, variable assignment bar is set to foo, function set foo is called, print is called on function variable foo
# D. Stack Trace: set_foo -> bar, bar cannot be printed, out of scope variable
# E. Return Error
# F. print Error
# 2 
# A. Type Str
# B. Mutability: Immutable
# C. Operations: foo is assigned to bar, function set_foo is defined, within set_foo function foo is assigned to qux, set foo is called, print is called on foo
# D. Stack Trace: foo -> 'bar', disregarding call within set_foo, 
# E. None
# F. print bar
# 3 In programs
#
# 4 
# function name: multiply_numbers
# function_arguments: 2, 3, 4 
# function definition: def multiply_numbers
# function body: result = num1 * num2 * num3
# function invocation: product
# function return value = result 
# all identifiers = multiply_numbers,def, num1, num2, num3, result, return, product##,
# 5 
# A. Type str 
# B. Mutability: Immutable
# C. Operations (line by line): function scream is defined, function scream is called with str argument 'Yipeee'
# D. Trace (run order): function object screams is created and stored in memory,function body is stored,function call 'Yipeee' is evaluated, argument is passed to the parameter
# words + '!!!!' is run,
#
# Flow Control
#
# 1. False, True, 3 (short circuted to the first operand because of the following or. The first operand expression evaluated to a 3 ), 3 ( same theory as the previous question but this time the and operator was used thus requiring both operands to determine the final value), False, True, False, False, False, False  
# 2. see programs
# 3. 'Product2', 'Product not found' ( )
# 4. def baz():
#    if foo:
#        return('bar')
#   else:
#        return qux()
# 5. Empty, since an empty list is a falsy value.
# 6 see programs      

