# Basics

### Operators

| Operator | Operation        | Example  |
| -------- | ---------------- | -------- |
| +        | Addition         | 2 + 2    |
| -        | Subtraction      | 2 - 1    |
| \*       | Multiplication   | 2 \* 2   |
| /        | Division         | 2 / 2    |
| //       | Integer division | 22 // 8  |
| %        | Modulus          | 22 % 8   |
| \*\*     | Exponent         | 2 \*\* 3 |

### Data Types

| Data Type | Examples            |
| --------- | ------------------- |
| Integers  | -2, -1, 0, 1, 2     |
| Floats    | -1.25, 1.0, 1.25    |
| Strings   | 'a', 'aa', 'Hello!' |

## Variables

In Python, you don't have to declare data types or use semicolons:

```
spam = 40
eggs = 2
spam = eggs + spam
```

Multiple assignment:

```
a, b = 1, 2
```

## Comments

Python comments start with `#`:

```
# This is a comment
```

## Function docstring

```
def foo():
  """
  This is a function dostring
  You can also use:
  ''' Function Docstring '''
  """
```

## Strings

Strings can be indexed:

```
word = "Python"
word[0] # character in position 0
'P'
```

Indices can also be negative

```
word[-1]
'n'
```

**Slicing** is also supported:

```
word[:2]
'Py'
word[2:]
'thon'
```

Slicing defaults:

-   An omitted first index defaults to 0
-   An omitted second index defaults to the size of the string being sliced.

## Lists

```
squares = [1, 4, 9, 16, 25]
```

Lists are basically arrays

-   Can be indexed
-   Can be sliced

> All slice operations return a **new** list containing the requested elements.

-   **append()** - adds new elements to the end of the list
-   **len()** - also works with lists

```
a, b = 0, 1
while a < 1000:
  print(a)
  a, b = b, a+b
```

# Useful Functions

-   print()

```
print('Hello World!')
```

-   input() - takes user input

```
print('What is your name?')
myName = input()
print('Nice to meet you ' + myName + '!')
```

-   len() - evaluates the integer value of the number of chars in a string

```
len('hello')
5
```

-   str() - converts input to string

```
str(29)
'29'
```

-   int() - converts input to int

```
int('12')
12
```

-   float() - converts input to a float

```
float('1.25')
1.25
```

# Flow Control

### Comparison operators

| Operator | Operation                |
| -------- | ------------------------ |
| ==       | Equal to                 |
| !=       | Not equal to             |
| <        | Less than                |
| >        | Greater than             |
| <=       | Less than or equal to    |
| >=       | Greater than or equal to |

### Boolean operators

| Operator | Example             |
| -------- | ------------------- |
| and      | True and True #True |
| or       | True or False #True |
| not      | not True #False     |

### if statements

```
if name == 'Alice':
  print('Hi, Alice!')
elif name == 'Bob':
  print('Hi, Bob!')
else:
  print('Hello, stranger!')
```

**for loop**
Python's `for` statement iterates over the items of any sequence (a list or string), in the order that they appear in the sequence.

```
words = ["cat", "windows", "defenstrate"]
for w in words:
  print(w, len(w))
# Output
cat 3
window 6
defenstrate 12
```

> When writing code that modifies a collection while iterating, make a copy and loop over the copy

```
for user, status in users.copy().items():
  if status == 'inactive":
    del users[user]

active_users = {}
for user, status in users.items():
  if status == 'active':
    active_users[user] = status
```

### for loops and range()

The range function can be called with 3 arguments:

> range(start, stop, step)

Use `range()` when you need to iterate over a sequence of numbers:

```
for i in range(5):
  print(i)
```

### _break_ and _continue_

-   **break**
    The break statement breaksout of the innermost enclosing `for` or `while` loop:

```
for n in range(2, 10):
  for x in range(2, n):
    if n % x == 0:
      print(n 'equals', x, '*', n//x)
      break
  else:
    # loop fell through without finding a factor
    print(n, 'is a prime number')
```

Here, the `else` clause has more in common with a `try` statement than an `if` statement. `else` runs when no `break` occurs.

-   **continue**
    The continue statement continues with the next iteration of the loop:

```
for num in range(2, 10):
  if num % 2 == 0:
    print("Found an even number", num)
    continue
  print("Found an odd number", num)
```

### while loop

```
spam = 0
while spam < 5:
  print('Hello, world.')
  spam = spam + 1
```

### pass statement

The pass statement does nothing. It can be used when a statement is required syntactically but the program requires no action:

```
while True:
  pass # Busy-wait for keyboard interrupt
```

# Functions

Functions are defined using the `def` keyword followed by the function name and the parenthesized list of parameters.

The first statement of the function body can optionally be the function's _docstring_.

```
def fib(n):   # write Fibonacci series up to n
  """Print a Fibonacci series up to n."""
  a, b = 0, 1
  while a < n:
    print(a, end=' ')
    a, b = b, a+b
  print()

fib(2000)
```
