1. Identify the Variables and Their Types

What variables exist?

What type is each variable?

Examples:

x = 5        → int
text = "hi"  → str
nums = [1,2] → list

Type determines what operations and methods are valid.

2. Determine Mutability

Is the object mutable or immutable?

Common immutable types:

int
float
str
tuple

Common mutable types:

list
dict
set

This predicts whether operations modify the object or create a new one.

Example:

text.upper()      → new string
numbers.append(4) → modifies list
3. Identify the Operation


What does this line of code do?

Common operations:
assignment
function call
method call
print
return

Examples:
x = x + 1
numbers.append(4)
print(x)
4. Trace the Value After Each Step ⭐

After each line runs, ask:

What is the value of each variable now?

Example:

x = [1,2]
y = x

Trace values:

x → [1,2]
y → [1,2]

Next line:

y.append(3)

Trace again:

x → [1,2,3]
y → [1,2,3]

Always update your mental model of the variables.

5. Determine the Function’s Return Value

Ask:

What does the function return?

If no return statement exists:

Python returns None

Examples:

return x + y → returns a value
print(x)     → returns None
6. Determine What Actually Prints

Ask:

What is passed to print()?

Remember:

print()  → displays output
return   → gives value back to caller

Only print() produces visible output.

Quick Mental Flow

When tracing code quickly, think:

Type → Operation → Trace Value → Return Value → Print Output
