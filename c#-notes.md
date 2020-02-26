# C# General Info

### C# vs .NET

- C# is a programming language
- .NET is a framework for building applications

## .NET

The .NET framework consists of 2 components:

- CLR (Common Language Runtime)
- Class Library

When C# is compiled, it does not compile straight to machine code. It compiles to an intermediate code called _IL Code_ - Intermediate Language. This allows your C# code to be compiled on all machines.

The **CLR** is basically an application that sits in memory whose job it is to translate the _IL Code_ to machine code through a process called _JIT_ - Just-in-time Compilation.

> **Class** - container that contains data (called **attributes**) and functions (called **methods**).

> **Namespace** - a container for related classes.

> **Assembly** is a container for related namespaces, DLL or EXE.

# Operators

| Name      | Operator | Example |
| --------- | -------- | ------- |
| Add       | +        | a + b   |
| Subtract  | -        | a - b   |
| Multiply  | \*       | a \* b  |
| Divide    | /        | a / b   |
| Remainder | %        | a % b   |
| Increment | ++       | a++     |
| Decrement | --       | a--     |

> Note: When putting the ++ **before** the variable, `b = ++a`, it increments then assigns the value.

Comparison Operators
| Name | Operator | Example |
| ------------------------- | -------- | ------- |
| Assignment | = | a = 1 |
| Addition assignment | += | a += 1 |
| Subtraction assigment | -= | a -= 1 |
| Multiplication assignment | \*= | a \*= 1 |
| Division assigment | /= | a /= 1 |

Logical Operators
| Name | Operator | Example |
| --- | -------- | ------- |
| And | && | a && b |
| Or | \|\| | a \|\| b |
| Not | ! | !a |

Bitwise Operators
| Name | Operator | Example |
| --- | -------- | ------- |
| And | & | a & b |
| Or | \| | a \| b |

# Variables

## Primitive Types

| Date Type | Size (byte) | Range |
| --------- | ----------- | ----- |
| short     | Int16       | 2     | -32,768 to 32,767 |
| int       | Int32       | 4     | -21.B to2.1B |
| long      | Int64       | 8     | … |
| float     | Single      | 4     | -3.4x10^38 to 3.4x10^38 |
| double    | Double      | 8     | … |
| decimal   | Decimal     | 16    | -7.9x10^28 to 7.9x10^28 |
| char      | Char        | 2     | Unicode Characters |
| bool      | Boolean     | 1     | True / False |

> C# defaults real numbers to doubles. To explicitly declare another type:<br> > `float number = 1.2f;`<br> > `decimal number = 1.2m;`

Non-Primitive Types

- String
- Array
- Enum
- Class

> **Constants** - variables which are immutable

## Type Conversion

- **Implicit** type conversion:

```
byte b = 1;  // 00000001
int i = b;   // 00000000 00000000 00000000 00000001
```

A byte takes 1 byte of memory while an int takes 4. So the compiler prefixes the int with 3 bytes of 0's.

- **Explicit** type conversion:
  > This is known as **casting**

```
int i = 1;
byte b = (byte)i;
```

There is also an Convert class with various methods:

- ToByte()
- ToInt16()
- ToInt32()
- ToInt64()

# Non-Primitive Types

## Classes

**Access modifier** - (public/private) - determines who can access this class

```
public class Person {}
```

When creating an object, you need to allocate the memory by using the `new` operator:

```
Person person = new Person();
```

> Unlike in C++, you don't have to worry about de-allocating memory.

_**static**_ modifier - lets you use class methods directly from the class itself

## Structs

Use when you want to declare a small simple object. Structs are similar to classes but more efficient

```
public struct RgbColor {
  public int Red;
  public int Green;
  public int Blue;
}
```

## Arrays

> **Array** - data structure to store a collection of variables of the same type

```
int[] numbers = new int[3];
number[0] = 1;
number[1] = 2;
OR
int[] numbers = new int[3] { 1, 2, 3};
```

## Strings

> **strings** - a sequence of characters
> Strings are surrounded by double quotes `string firstName = "Tanner";`

You can create strings using concatenation:

```
string name = firstName + " " + lastName;
```

> This example actually calls the `String.Concat()` method.

### String Formatting

```
string name = string.Format("{0} {1}", firstName, lastName);
```

You can also join together multiple items into a string:

```
var numbers = new int[3] { 1, 2, 3 };
string list = string.Join(",", numbers);
```

## Enums

> **enum** - a set of name/value pairs (constants).

```
public enum ShippingMethod {
  RegularAirMail = 1,
  RegisteredAirMail = 2,
  Express = 3
}

var method = ShippingMethod.Express;
```

## Reference vs Value Types

| Value Type                            | Reference Type              |
| ------------------------------------- | --------------------------- |
| **Structures**                        | **Classes**                 |
| Allocated on stack                    | You need to allocate memory |
| Memory allocation done automatically  | Memory allocated on heap    |
| Immediately removed when out of scope | Garbage collected by CLR    |

Example:
Arrays are reference type:

```
var array1 = new int[3] { 1, 2, 3};
var array2 = array;
array2[0] = 0;
// What will array[0] be?
// array1[0] will be 0
```

# Control Flow

- **if / else**

```
if (condition)
  someStatement
else if (anotherCondition)
  anotherStatement
else
  yetAnotherStatement
```

- **switch / case**

```
switch(role)
{
  case Role.Admin:
    ...
    break;
  case Role.Moderator:
    ...
    break;
  default:
    ...
    break;
}
```

- **conditional statement**

Works exactly like JavaScript

```
bool isGoldCustomer = true;

float proce = (isGoldCustomer) ? 19.95f : 29.95f;
```

- **foreach loop**
  This is used to iterate over any innumberable object:

```
// Goal sum all positive numbers
public static int PositiveSum(int[] numbers)
{
  var sum = 0;
  foreach(var number in numbers)
  {
    if (number > 0)
    {
      sum += number;
    }
  }
  return sum;
}
```

- **while loop**

```
while ( i < 10)
{
  ...
  i++;
}
```

- **do-while loop**

```
do
{
  ...
  i++;
} while (i < 10);
```

# Arrays

In C# all arrays map to the Array type that is defined in the System namespace of the .NET framework.

> Arrays are a fixed size.

```
int[] array = new int[5];
int[] array1 = new int[] { 1, 2, 3, 4, 5 };
string[] weekDays = new string[] { "Sun", Mon", "Tue" };
```

**Useful array methods**

- Array.Length
- Array.IndexOf
- Array.Clear
- Array.Copy
- Array.Sort
- Array.Reverse

# Lists

> Lists are dynamically sized.

```
var numbers = new List<int>() { 1, 2, 3, 4 };
```

Useful Methods

- Add
- AddRange
- Remove
- RemoveAt
- IndexOf
- LastIndexOf
- Contains
- Count

# Strings

Strings are immutable so each method returns a new string. This allows you to chain methods together.

**Useful string methods**

- ToLower()
- ToUpper()
- Trim()
- IndexOf()
- LastIndexOf()
- Substring(startIndex, length)
- Replace('a', '!');
- String.IsNullOrEmpty(str)
- String.IsNullOrWhiteSpace(str)
- str.Split(' ')

**Converting strings to numbers**
To convert, use the built-in `Convert` class:

```
string s = "1234";
int i = int.Parse(s);
int j = Convert.ToInt32(s);
```

**Converting numbers to strings**
Use the `ToString()` method. You can pass formatting parameters to specify currency, decimal, etc:

```
int i = 1234;
string s = i.ToString();      // "1234"
string t = i.ToString("C");   // "1,234.00"
string t = i.ToString("C0");  // "1,234"
```

Format Strings
| Format Specifier | Description | Example |
| ---------------- | ----------- | ----------------------------------- |
| c or C | Currency | 123456 (C) → \$123,456 |
| d or D | Decimal | 1234 (D6) → 001234 |
| e or E | Exponential | 1052.0329112756 (E) → 1.052033E+003 |
| f or F | Fixed Point | 1234.567 (F1) → 1234.5 |
| x or X | Hexadecimal | 255 (X) → FF |

## StringBuilder

- Defined in System.Text
- Represents a mutable string
- Easy and fast to create and manipulate strings

> StringBuilder is not optimized for searching! It doesn't have methods like `IndexOf`, `Contains`, `StartsWith`, etc

**Manipulation methods**

- Append()
- Insert()
- Remove()
- Replace()
- Clear()

# Classes

Declaring Classes:
**Access modifier** - public / private
**Return type** - type of data the method will return

```
public class Person
// (Access modifier) (Return type) (Class name)
{
  public string Name; // This is a 'field'
  public void Introduce() // This is a 'method'
  {
    Console.WriteLine("Hi, my name is "+ Name);
  }
}
```

**Creating object instance**:

```
Person person = new Person();
var person = new Person();
```

### Class members

There are 2 types - instance and static

- Instance - accessible from an object:

```
var person = new Person();
person.Introduce();
```

- Static - accessible from the class:

```
Console.WriteLine();
```

> So why use static members? To represent concepts that are singleton

**Declaring static members:**
Just add the `static` keyword after the access modifier.

```
public class Person
{
  public static int PeopleCount = 0;
}
```

### Constructors

A constuctor has the same name as the class and do not have a return type. If you don't create a constuctor, C# creates a hidden on for you.

```
public class Customer
{
  public string Name;
  public Customer(string name)
  {
    this.Name = name;
  }
}
```

### Constructor Overloading

> Overloading - having multiple methods with the same name with different signitures.
> A _signature_ is what uniquely identifies a method.

```
public class Customer
{
  public Customer() {...}
  public Customer(string name) {...}
  public Customer(int id, string name) {...}
}
```

To make overloaded constructors call another constructor, use `: this()`:

### Object initialization syntax

Used to quickly initialize an object without the need to call one of its constructors:

```
var person = new Person
{
  FirstName = "Tanner",
  LastName = "Langlinais"
};
```

## Methods

Signature of a method:

- Name
- Number and type of parameters

```
public class point
{
  public void Move(int x, int y) {}
}
```

**Overloading methods**
Methods with the same name but different signatures:

```
public class Point
{
  public void Move(int x, int y) {}
  public void Move(Point newLocation) {}
  public void Move(Point newLocation, int speed) {}
}
```

You can also use the `params` modifier to pass in an array or any number or arguments:

```
public class Calculator
{
  public int Ad(params int[] numbers) {}
}
var result = calculator.Add(new int[] { 1, 2, 3, 4 });
var result = calculator.Add(1, 2, 3, 4);
```

## Fields

> Field - variable declared at the class level used to store data about the class

```
public class Customer
{
  List<Order> Orders;
  public Customer()
  {
    Orders = new List<Order>();
  }
}
```

Some developers think it's only necessary to use a constructor when passed outside values. If so how do you initialize a list?

**Read-only fields**

```
public class Customer
{
  readonly List<Order> Orders = new List<Order>();
}
```

## Access Modifiers

> **Access Modifier** - way to control access to a class and its members. If a member is declared private, you can't access that member outside of that class.

**OOP 3 Main Concepts**

1. Encapsulation / Information Hiding
2. Inheritance
3. Polymorphism

## Encapsulation

In practice, fields are defined as private. Getters and setters are used to access/modify the fields from outside the class.

When naming private fields, use an underscore before the name:

```
private string _name;
```

### Properties

A property is a class member that encapsulates a getter/setter for accessing a field:

```
public class Person
{
  private DateTime _birthdate;
  public DateTime Birthdate
  {
    get { return _birthdate; }
    set { _birthdate = value; }
  }
}
```

**Auto-implemented properties**:
You can also declare a property as showd to let the compiler auto-create a private member with a getter/setter:

```
public class Person
{
  public DateTime Birthdate { get; set; }
}
```

To set private auto-implemented properties, add private before the method:

```
public class Person
{
  public DateTime Birthdate { get; private set; }
}
```

## Inheritance

Relationship between two classes that allow one to inherit code from the other. Has a 'is-a' relationship.
Benefits:

- Code re-use
- Polymorphic behavior

```
public class PresentationObject
{
  // Common shared code
}
public class Text : PresentationObject
{
  // Code specific to text
}
```

### Access modifiers

- **public** - accessible from anywhere

```
public class Customer
{
  public void Promote() {...}
}
var customer = new Customer();
customer.Promote();
```

- **private** - accessible only from the class

```
public class Customer
{
  private int CalculateRating() {...}
}
var customer = new Customer();
customer.CalculateRating(); // ERROR
```

- **protected** - accessible only from the class and its derived classes.
  A problem with protected is any derived classes can use methods which contradicts encapsulation.

```
public class Customer
{
  protected int CalculateRating() {...}
}
var customer = new Customer();
customer.CalculateRating(); // ERROR
```

- **internal** - accessible only from the same assembly

- **protected internal** - accessible only from the same assembly or any derived classes

### Constructors and Inheritance

- Base class constructors are always executed first.
- Base class constructors are not inherited
