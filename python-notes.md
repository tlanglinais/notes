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

## Useful Functions

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

## Comparison operators

| Operator | Operation                |
| -------- | ------------------------ |
| ==       | Equal to                 |
| !=       | Not equal to             |
| <        | Less than                |
| >        | Greater than             |
| <=       | Less than or equal to    |
| >=       | Greater than or equal to |

## Boolean operators

| Operator | Example             |
| -------- | ------------------- |
| and      | True and True #True |
| or       | True or False #True |
| not      | not True #False     |

## if statements

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

## for loops and range()

The range function can be called with 3 arguments:

> range(start, stop, step)

Use `range()` when you need to iterate over a sequence of numbers:

```
for i in range(5):
  print(i)
```

## _break_ and _continue_

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

## while loop

```
spam = 0
while spam < 5:
  print('Hello, world.')
  spam = spam + 1
```

## pass statement

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

## Function arguments

### Default Argument Values

```
def ask_ok(prompt, retries=4, reminder='Please try again!'):
  while True:
    ok = input(prompt)
    if ok in ('y', 'ye', 'yes'):
      return True
    if ok in ('n', 'no', 'nop', 'nope):
      return False
    retries = retries - 1
    if retries < 0:
      raise ValueError('invalid user response)
    print(reminder)
```

This function can be called in serveral ways:

-   giving only the mandatory argument: `ask_ok('Do you really want to quit?')`
-   giving one of the optional arguments: `ask_ok('Ok to overwrite?', 2)`
-   giving all arguments: `ask_ok('Ok to overwrite?', 2, 'Only yes or no!')`

### arguments and keywords

```
def cheeseshop(kind, *arguments, **keywords):
  for arg in arguments:
    print(arg)
  print("-" * 40)
  for keyword in keywords:
    print(keyword)

cheeseshop('Limburger', 'It's very runny, sir.', 'It's really very runny!', shopkeeper='Michael Palin', client='John Cleese', sketch='Cheese shop sketch')
```

The `*arguments` parameter receives a `tuple` containing the positional arguments beyond the formal parameter list.

The `**keywords` parameter receives a `dictionary` containing all keyword arguments, except those corresponding to a formal paramter.

### Special parameters

By default, arguments may be passed to a function either by position or explicitly by keyword.

A function may look like this:

```
def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
      -----------    ----------     ----------
        |             |                  |
        |        Positional or keyword   |
        |                                - Keyword only
         -- Positional only
```

`/` and `*` are optional. If used, these symbols indicate the kind of parameter by how the arguments may be passed to the function:

-   positional-only
-   positional-or-keyword
-   keyword-only

## lambda expressions

> Small anonymous functions, restricted to a single expression using the `lambda` keyword

```
def make_incrementor(n):
  return lambda x: x + n
```

## Documentation Strings

Conventions

-   First line - should always be a short summary of the purpose.
-   Second line - should be blank to separate the summary
-   Following lines - one or more paragraphs describing the calling conventions, side effects, etc.

## Function annotations

> Optional metadata about the types used

Annotations are stored in the `__annotations__` attribute of the function. They are defined by a colon after the paramter name, followed by an expression evaluating to the value of the annotation.

Return annotations are defined by a literal `->` followed by an expression:

```
def f(ham: str, eggs: str = 'eggs') -> str:
  print("Annotations:",f.__annotations__)
  print("Arguments:", ham, eggs)
  return ham + " and " + eggs
```

# Data Structures

## Lists

Useful list methods:

```
>>> fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
>>> fruits.count('apple')
2
>>> fruits.count('tangerine')
0
>>> fruits.index('banana')
3
>>> fruits.index('banana', 4)  # Find next banana starting a position 4
6
>>> fruits.reverse()
>>> fruits
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']
>>> fruits.append('grape')
>>> fruits
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']
>>> fruits.sort()
>>> fruits
['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']
>>> fruits.pop()
'pear'
```

### Using lists as stacks

The list methods make it very easy to use a list as a stack, where last-in, first-out:

```
>>> stack = [3, 4, 5]
>>> stack.append(6)
>>> stack.append(7)
>>> stack
[3, 4, 5, 6, 7]
>>> stack.pop()
7
>>> stack
[3, 4, 5, 6]
>>> stack.pop()
6
>>> stack.pop()
5
>>> stack
[3, 4]
```

### Using lists as queues

It's also possible to use lists as queues, where first-in, first-out. However, this is inefficient and `collections.deque` should be used.

### List comprehensions

-> Concise way to make lists

Common applications are to make new lists where each element is the result of some operations applied to each member or another sequece or iterable, or to create a subsequence of those elements that satisfy a certain condition.

```
squares = []
for x in range(10):
  squares.append(x ** 2)

# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

Better way:

```
squares = [x**2 for x in range(10)]
```

A list comprehension consists of brackets containing an expression followed by a `for` clause, then 0 or more `for` or `if` clauses.

Combining two lists if they are not equal:

```
[(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
```

### Nested list comprehensions

The initial expression in a list comprehension can be any arbitrary expression, including another list comprehension.

```
matrix = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9, 10, 11, 12]
]
[[for[i] for row in matrix] for i in range(4)]
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
```

## The del statement

> `del` - way to remove an item from a list given its index instead of value
> This differs from `pop` which returns a value

```a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
# [1, 66.25, 333, 333, 1234.5]
del a[2:4]
# [1, 66.25, 1234.5]
```

> `del` can also be used to delete entire variables

## Tuples and sequences

> Tuple - consists of a number of values separated by commas, enclosed by parenthesis

Tuples are immutable, and usually contain a sequence of elements that are accessed via unpacking or indexing.

```
>>> t = 12345, 54321, 'hello'
>>> t
(12345, 54321, 'hello')
```

A special problem is a tuple containing 0 or 1 elements. Empty tuples are constructed by an empty pair of parenthesis. A typle with one item is constructed by following a value with a comma.

```
empty = ()
single = 'hello',
```

**Unpacking**
Unpacking allows multiple assignements using tuples

```
t = 12345, 54321, 'hello'
x, y, z = t
```

Sequence unpacking requires that there are as many variables on the left side as there on the right.

## Sets

> `Set` - unordered collection with **no** duplicate elements.
> Sets can be made using curly braces or the `set()` function.

```
basket = {'apple', 'orange', 'apple', 'orange', 'banana'}
print(basket)
# {'orange', 'banana', 'pear', 'apple'}
a = set('abracadabra')
b = set('alacazam')
a
# {'a', 'r', 'b', 'c', 'd'}
a - b   # letters in a but not in b
# {'r', 'd', 'b'}
a | b   # letters in a or b or both
a & b   # letters in both a and b
a ^ b   # letters in a or b but not both
```

Similarly to list comprehensions, **set comprehensions** are also supported:

```
a = {x for x in 'abracadabra' if x not in 'abc'}
a
{'r', 'd'}
```

## Dictionaries

Dictionaries are indexed by keys, which can be any immutable type: strings and numbers can always be keys.

```
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
tel
# { 'jack': 4098, 'sape': 4139, 'guido': 4127}
```

The del keyword also works with dictionaries:

```
del tel['sape']
```

The `in` keywords works with dictionaries too:

```
'guido' in tel
# True
'jack' not in tel
# False
```

### Dict comprehension

Dict comprehensions can be used to create dictionaries from arbitrary key and value expressions:

```
>>> {x: x**2 for x in (2, 4, 6)}
{2: 4, 4: 16, 6: 36}
```

### Dict method

When the keys are simple strings, it is sometimes easier to specify pairs using keyword arguments:

```
dict(sape=4139, guido=4127, jack=4098)
# {'sape': 4139, 'guido': 4127, 'jack': 4098}
```

## Looping Techniques

### items()

When looping through dictionaries, the key and corresponding value can be retrieved at the same time using the `items()` method:

```
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
  print(k, v)
# gallahad the pure
# robin the brave
```

### enumerate()

When looping through a sequence, the position index and value can be retrieved using the `enumerate` function:

```
for i, v in enumerate(['tic', 'tac', 'toe']):
  print(i, v)
# 0 tic
# 1 tac
# 2 toe
```

### zip()

To loop over two or more sequences at the same time, the entries can be paired with the `zip` function:

```
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
  print(f'What is your name {q}? It is {a}.')
# What is your name? It is lancelot.
# What is your quest? It is the holy grail.
# What is your favorite color? It is blue.
```

# Modules

```
# import entire module
import fibo

# import specific methods
from fibo import fib, fib2

# import all names except those beginning with an underscore
from fibo import *

# name binding
import fibo as fib

from fibo import fib as fibonacci
```
