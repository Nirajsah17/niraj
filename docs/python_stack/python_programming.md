# Python Programming

Python is a high-level, interpreted, interactive and object-oriented scripting language. Python is designed to be highly readable. It uses English keywords frequently where as other languages use punctuation, and it has fewer syntactical constructions than other languages.

Python is a MUST for students and working professionals to become a great Software Engineer specially when they are working in Web Development Domain. I will list down some of the key advantages of learning Python:

- **Python is Interpreted** − Python is processed at runtime by the interpreter. You do not need to compile your program before executing it. This is similar to PERL and PHP.

- **Python is Interactive** − You can actually sit at a Python prompt and interact with the interpreter directly to write your programs.

- **Python is Object-Oriented** − Python supports Object-Oriented style or technique of programming that encapsulates code within objects.

- **Python is a Beginner's Language** − Python is a great language for the beginner-level programmers and supports the development of a wide range of applications from simple text processing to WWW browsers to games.

## Python Features

Python's features include −

- **Easy-to-learn** − Python has few keywords, simple structure, and a clearly defined syntax. This allows the student to pick up the language quickly.

- **Easy-to-read** − Python code is more clearly defined and visible to the eyes.

- **Easy-to-maintain** − Python's source code is fairly easy-to-maintain.

- **A broad standard library** − Python's bulk of the library is very portable and cross-platform compatible on UNIX, Windows, and Macintosh.

- **Interactive Mode** − Python has support for an interactive mode which allows interactive testing and debugging of snippets of code.

- **Portable** − Python can run on a wide variety of hardware platforms and has the same interface on all platforms.

- **Extendable** − You can add low-level modules to the Python interpreter. These modules enable programmers to add to or customize their tools to be more efficient.

- **Databases** − Python provides interfaces to all major commercial databases.

- **GUI Programming** − Python supports GUI applications that can be created and ported to many system calls, libraries, and windows systems, such as Windows MFC, Macintosh, and the X Window system of Unix.

- **Scalable** − Python provides a better structure and support for large programs than shell scripting.

Apart from the above-mentioned features, Python has a big list of good features, few are listed below −

- It supports functional and structured programming methods as well as OOP.
- It can be used as a scripting language or can be compiled to byte-code for building large applications.
- It provides very high-level dynamic data types and supports dynamic type checking.
- It supports automatic garbage collection.
- It can be easily integrated with C, C++, COM, ActiveX, CORBA, and Java.

## Python Environment Setup 

Python is available on a wide variety of platforms including Linux and Mac OS X. Let's understand how to set up our Python environment.

### Local Environment Setup

If you are still willing to set up your environment for Python, you need to set up the Python environment on your computer. Depending on your operating system, you can follow any of the following guides to install Python on your computer.

- [How to set up Python on Windows?](https://www.tutorialspoint.com/python/python_environment.htm)
- [How to set up Python on Linux?](https://www.tutorialspoint.com/python/python_environment.htm)
- [How to set up Python on Mac?](https://www.tutorialspoint.com/python/python_environment.htm)

### Online Python Compilers

If you don't want to set up your environment, you can use online Python compilers. Here are some of the popular online Python compilers:

- [Python (v2.7.13)](https://www.tutorialspoint.com/execute_python_online.php)
- [Python (v3.2.3)](https://www.tutorialspoint.com/execute_python3_online.php)

## Python Syntax

Python was designed to for readability, and has some similarities to the English language with influence from mathematics. Python uses new lines to complete a command, as opposed to other programming languages which often use semicolons or parentheses.

Python relies on indentation, using whitespace, to define scope; such as the scope of loops, functions and classes. Other programming languages often use curly-brackets for this purpose.

Here is an example of Python code that uses indentation:

```python title="example.py" linenums="1"
for x in range(10):
    print(x)
    if x == 5:
        break
```

## Python Identifiers

A Python identifier is a name used to identify a variable, function, class, module or other object. An identifier starts with a letter A to Z or a to z or an underscore (_) followed by zero or more letters, underscores and digits (0 to 9).

Python does not allow punctuation characters such as @, $, and % within identifiers. Python is a case sensitive programming language. Thus, `Manpower` and `manpower` are two different identifiers in Python.

Here are naming conventions for Python identifiers −

- Class names start with an uppercase letter. All other identifiers start with a lowercase letter.
- Starting an identifier with a single leading underscore indicates that the identifier is private.
- Starting an identifier with two leading underscores indicates a strongly private identifier.
- If the identifier also ends with two trailing underscores, the identifier is a language-defined special name.

## Reserved Words

The following list shows the Python keywords. These are reserved words and you cannot use them as constants or variables or any other identifier names. All the Python keywords contain lowercase letters only.

``` python linenums="1"
and       exec      not      assert    finally   or        break
for       pass      class    from      print     continue  global
raise     def       if       return    del       import    try
elif      in        while    else      is        with      except
lambda    yield     False    True      None
```

## Lines and Indentation

Python provides no braces to indicate blocks of code for class and function definitions or flow control. Blocks of code are denoted by line indentation, which is rigidly enforced.

The number of spaces in the indentation is variable, but all statements within the block must be indented the same amount. For example −

``` python title="example.py" linenums="1"
if True:
    print("True")
else:
    print("False")
```

However, the following block generates an error −

``` python title="example.py" linenums="1"
if True:
    print("Answer")
    print("True")
else:
    print("Answer")
  print("False")  # IndentationError: unexpected indent
```

## Multi-Line Statements

Statements in Python typically end with a new line. Python does, however, allow the use of the line continuation character (\) to denote that the line should continue. For example −

``` python title="example.py" linenums="1"
total = item_one + \
        item_two + \
        item_three
```

Statements contained within the `[], {}, or ()` brackets do not need to use the line continuation character. For example −

``` python title="example.py" linenums="1"
days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday']
```

## Quotation in Python

Python accepts single ('), double (") and triple (''' or """) quotes to denote string literals, as long as the same type of quote starts and ends the string.

The triple quotes are used to span the string across multiple lines. For example, all the following are legal −

``` python
word = 'word'
sentence = "This is a sentence."
paragraph = """This is a paragraph. It is
made up of multiple lines and sentences."""
```

## Comments in Python

A hash sign (#) that is not inside a string literal begins a comment. All characters after the # and up to the end of the physical line are part of the comment and the Python interpreter ignores them.

``` python title="example.py" linenums="1"
# First comment
print("Hello, Python!")  # second comment
```

This produces the following result −

``` python linenums="1"
Hello, Python!
```


## Using Blank Lines

A line containing only whitespace, possibly with a comment, is known as a blank line and Python totally ignores it.

In an interactive interpreter session, you must enter an empty physical line to terminate a multiline statement.

## Waiting for the User

The following line of the program displays the prompt, the statement saying "Press the enter key to exit", and waits for the user to take action −

``` python title="example.py" linenums="1"
input("\n\nPress the enter key to exit.")
```

Here, `\n\n` is used to create two new lines before displaying the actual line. Once the user presses the key, the program ends. This is a nice trick to keep a console window open until the user is done with an application.

## Multiple Statements on a Single Line

The semicolon ( ; ) allows multiple statements on the single line given that neither statement starts a new code block. Here is a sample snip using the semicolon −

``` python title="example.py" linenums="1"
import sys; x = 'foo'; sys.stdout.write(x + '\n')
```

## Multiple Statement Groups as Suites

A group of individual statements, which make a single code block are called suites in Python. Compound or complex statements, such as if, while, def, and class require a header line and a suite.

Header lines begin the statement (with the keyword) and terminate with a colon ( : ) and are followed by one or more lines which make up the suite. For example −

``` python title="example.py" linenums="1"

if expression : 
   suite
elif expression : 
   suite 
else : 
   suite
```  

## Command Line Arguments

Many programs can be run to provide you with some basic information about how they should be run. Python enables you to do this with -h −

``` python linenums="1"
$ python -h   
usage: python [option] ... [-c cmd | -m mod | file | -] [arg] ...
Options and arguments (and corresponding environment variables):
-c cmd : program passed in as string (terminates option list)
-d     : debug output from parser (also PYTHONDEBUG=x)
-E     : ignore environment variables (such as PYTHONPATH)
-h     : print this help message and exit
[ etc. ]
```

## Python - Variable Types

Variables are nothing but reserved memory locations to store values. This means that when you create a variablstr = 'Hello World!'
print(str)           # Prints complete string
print(str[0])        # Prints first character of the string
print(str[2:5])      # Prints characters starting from 3rd to 5th

print(str[2:])       # Prints string starting from 3rd character  
print(str * 2)       # Prints string two times
print(str + "TEST")  # Prints concatenated stringlicit declaration to reserve memory space. The declaration happens automatically when you assign a value to a variable. The equal sign (=) is used to assign values to variables.

The operand to the left of the = operator is the name of the variable and the operand to the right of the = operator is the value stored in the variable. For example −

``` python title="example.py" linenums="1"
counter = 100          # An integer assignment
miles   = 1000.0       # A floating point
name    = "John"       # A string

print(counter)
print(miles)
print(name)
```

Here, 100, 1000.0 and "John" are the values assigned to counter, miles, and name variables, respectively. This produces the following result −

``` python linenums="1"
100 
1000.0
John
```

## Multiple Assignment

Python allows you to assign a single value to several variables simultaneously. For example −

``` python title="example.py" linenums="1"
a = b = c = 1
```

Here, an integer object is created with the value 1, and all three variables are assigned to the same memory location. You can also assign multiple objects to multiple variables. For example −

``` python title="example.py" linenums="1"
a, b, c = 1, 2, "john"
``` 

Here, two integer objects with values 1 and 2 are assigned to variables a and b, and one string object with the value "john" is assigned to the variable c.

## Standard Data Types

The data stored in memory can be of many types. For example, a person's age is stored as a numeric value and his or her address is stored as alphanumeric characters. Python has various standard data types that are used to define the operations possible on them and the storage method for each of them.

Python has five standard data types −

- Numbers
- String
- List
- Tuple
- Dictionary

## Python Numbers

Number data types store numeric values. Number objects are created when you assign a value to them. For example −

``` python linenums="1"
var1 = 1
var2 = 10
```


You can also delete the reference to a number object by using the del statement. The syntax of the del statement is −

``` python title="example.py" linenums="1"
del var1[,var2[,var3[....,varN]]]
```

You can delete a single object or multiple objects by using the del statement. For example −

``` python title="example.py" linenums="1"
del var
del var_a, var_b
```

Python supports four different numerical types −

- int (signed integers)
- long (long integers, they can also be represented in octal and hexadecimal)
- float (floating point real values)
- complex (complex numbers)

Here are some examples of numbers −

``` python linenums="1"
int
long
float
complex
```

## Python Strings

Strings in Python are identified as a contiguous set of characters represented in the quotation marks. Python allows for either pairs of single or double quotes. Subsets of strings can be taken using the slice operator ([ ] and [:] ) with indexes starting at 0 in the beginning of the string and working their way from -1 at the end.

The plus (+) sign is the string concatenation operator and the asterisk (*) is the repetition operator. For example −

``` python title="example.py" linenums="1"
str = 'Hello World!'
print(str)           # Prints complete string
print(str[0])        # Prints first character of the string
print(str[2:5])      # Prints characters starting from 3rd to 5th

print(str[2:])       # Prints string starting from 3rd character  
print(str * 2)       # Prints string two times
print(str + "TEST")  # Prints concatenated string
```

This will produce the following result −

``` python
Hello World!
H
llo
llo World!
Hello World!Hello World!
Hello World!TEST
```

## Python Lists

Lists are the most versatile of Python's compound data types. A list contains items separated by commas and enclosed within square brackets ([]). To some extent, lists are similar to arrays in C. One difference between them is that all the items belonging to a list can be of different data type.

The values stored in a list can be accessed using the slice operator ([ ] and [:]) with indexes starting at 0 in the beginning of the list and working their way to end -1. The plus (+) sign is the list concatenation operator, and the asterisk (*) is the repetition operator. For example −

``` python title="example.py" linenums="1"
list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']
print(list)            # Prints complete list
print(list[0])         # Prints first element of the list
print(list[1:3])       # Prints elements starting from 2nd till 3rd
print(list[2:])        # Prints elements starting from 3rd element
print(tinylist * 2)    # Prints list two times
print(list + tinylist) # Prints concatenated lists
```

This will produce the following result −

``` python linenums="1"
['abcd', 786, 2.23, 'john', 70.200000000000003]
abcd
[786, 2.23]
[2.23, 'joif expression:
   statement(s) 'john', 123, 'john']
['abcd', 786, 2.23, 'john', 70.200000000000003, 123, 'john']
```

## Python Tuples

A tuple is another sequence data type that is similar to the list. A tuple consists of a number of values separated by commas. Unlike lists, however, tuples are enclosed within parentheses.

The main differences between lists and tuples are: Lists are enclosed in brackets ( [ ] ) and their elements and size can be changed, while tuples are enclosed in parentheses ( ( ) ) and cannot be updated. Tuples can be thought of as read-only lists. For example −

``` pytif expression1:
   statement(s)
elif expression2:
   statement(s)
elif expression3:
   statement(s)
else:
   statement(s)            # Prints complete tuple
print(tuple[0])          # Prints first element of the tuple
print(tuple[1:3])        # Prints elements starting from 2nd till 3rd
print(tuple[2:])         # Prints elements starting from 3rd element
print(tinytuple * 2)     # Prints tuple two times 
print(tuple + tinytuple) # Prints concatenated tuple
```

This will produce the following result −

``` python linenums="1"
('abcd', 786, 2.23, 'john', 70.20000000000if expression1:
   statement(s)
elif expression2:
   statement(s)
elif expression3:
   statement(s)
else:
   statement(s)00000000003, 123, 'john')
```

## Python Dictionary

Python's dictionaries are kind of hash table type. They work like associative arrays or hashes found in Perl and consist of key-value pairs. A dictionary key can be almost any Python type, but are usually numbers or strings. Values, on the other hand, can be any arbitrary Python object.

Dictionaries are enclosed by curly braces ({ }) and values can be assigned and accessed using square braces ([]). For example −

``` python title="example.py" linenums="1"
dict = {}
dict['one'] = "This is one"
dict[2]     = "This is two"
tinydict = {'name': 'john','code':6734, 'dept': 'sales'}
print(dict['one'])       # Prints value for 'one' key
print(dict[2])           # Prints value for 2 key
print(tinydict)          # Prints complete dictionary
print(tinydict.keys())   # Prints all the keys
print(tinydict.values()) # Prints all the values
```

This will produce the following result −

``` python linenums="1"
This is one
This is two
{'dept': 'sales', 'code': 6734, 'name': 'john'}
['dept', 'code', 'name']
['sales', 6734, 'john']
```

## Data Type Conversion

Sometimes, you may need to perform conversions between the built-in types. To convert between types, you simply use the type-name as a function.

There are several built-in functions to perform conversion from one data type to another. These functions return a new object representing the converted value.

- `int(x [,base])` − Converts x to an integer. The base specifies the base if x is a string.
- `long(x [,base] )` − Converts x to a long integer. The base specifies the base if x is a string.
- `float(x)` − Converts x to a floating-point number.
- `complex(real [,imag])` − Creates a complex number.
- `str(x)` − Converts object x to a string representation.
- `repr(x)` − Converts object x to an expression string.
- `eval(str)` − Evaluates a string and returns an object.
- `tuple(s)` − Converts s to a tuple.
- `list(s)` − Converts s to a list.
- `set(s)` − Converts s to a set.
- `dict(d)` − Creates a dictionary. d must be a sequence of (key,value) tuples.

## Python - Basic Operators

Operators are the constructs which can manipulate the value of operands. Consider the expression 4 + 5 = 9. Here, 4 and 5 are called operands and + is called operator.

Python language supports the following types of operators − 

- Arithmetic Operators
- Comparison (Relational) Operators
- Assignment Operators
- Logical Operators
- Bitwise Operators
- Membership Operators
- Identity Operators

## Python - Decision Making

Decision making is required when we want to execute a code only if a certain condition is satisfied.

The `if…elif…else` statement is used in Python for decision making.

### if statement syntax

``` python title="example.py" linenums="1"
if expression:
   statement(s)
```

Here, the program evaluates the `expression` and will execute `statement(s)` only if the `expression` is `True`.

If the `expression` is `False`, the statement(s) is not executed.

Python interprets non-zero values as `True`. `None` and `0` are interpreted as `False`.

### if...elif...else statement

An `if` statement can be followed by an optional `elif...else` statement, which is very useful to test various conditions using single `if...elif...else` statement.

Here is the syntax of `if...elif...else` statement −

``` python title="example.py" linenums="1"
if expression1:
   statement(s)
elif expression2:
   statement(s)
elif expression3:
   statement(s)
else:
   statement(s)
```

The `elif` is short for else if. It allows us to check for multiple expressions.


If the `expression1` is `True`, it executes the `statement(s)` that are present inside the `if` block. If `expression1` is `False`, it checks the `expression2` and executes the `statement(s)` that are present inside the `elif` block.

The `elif` block is `executed` if the `first` `expression` is `False`.

If none of the expressions is `True`, the `else` block is executed.

## Python - Loops

Python programming language provides following types of loops to handle looping requirements.

- `while` loop
- `for` loop

### The `while` Loop

A `while` loop statement in Python programming language repeatedly executes a target statement as long as a given condition is `True`.

Here, `statement(s)` may be a single statement or a block of statements. The `condition` may be any expression, and `true` is any non-zero value. The loop iterates while the `condition` is `true`.

When the `condition` becomes `false`, program control passes to the line immediately following the loop.

The syntax of a `while` loop in Python programming language is −

``` python title="example.py" linenums="1"
while expression:
   statement(s)
```

Here, `statement(s)` may be a single statement or a block of statements. The `condition` may be any expression, and `true` is any non-zero value. The loop iterates while the `condition` is `true`.

When the `condition` becomes `false`, program control passes to the line immediately following the loop.


### The `for` Loop

The `for` loop in Python is used to iterate over a sequence (list, tuple, string) or other iterable objects. Iterating over a sequence is called traversal.

The syntax of the `for` loop is as follows −

``` python title="example.py" linenums="1"
for iterating_var in sequence:
   statements(s)
```

If a sequence contains an expression list, it is evaluated first. Then, the first item in the sequence is assigned to the iterating variable `iterating_var`. Next, the statements block is executed. Each item in the list is assigned to `iterating_var`, and the statement(s) block is executed until the entire sequence is exhausted.

## Python - Functions

A function is a block of organized, reusable code that is used to perform a single, related action. Functions provide better modularity for your application and a high degree of code reusing.

As you already know, Python gives you many built-in functions like `print()`, etc. but you can also create your own functions. These functions are called user-defined functions.

### Defining a Function

You can define functions to provide the required functionality. Here are simple rules to define a function in Python.

- Function blocks begin with the keyword `def` followed by the function name and parentheses `( )`.
- Any input parameters or arguments should be placed within these parentheses. You can also define parameters inside these parentheses.
- The first statement of a function can be an optional statement - the documentation string of the function or docstring.
- The code block within every function starts with a colon (:) and is indented.
- The statement `return [expression]` exits a function, optionally passing back an expression to the caller. A return statement with no arguments is the same as `return None`.

### Syntax

``` python title="example.py" linenums="1"
def functionname( parameters ):
   "function_docstring"
   function_suite
   return [expression]
```

By default, parameters have a positional behavior and you need to inform them in the same order that they were defined.

### Example

Here is a simple example of a function −

``` python title="example.py" linenums="1"
def printme( str ):
   "This prints a passed string into this function"
   print(str)
   return
```

### Calling a Function

Defining a function only gives it a name, specifies the parameters that are to be included in the function and structures the blocks of code.

Once the basic structure of a function is finalized, you can execute it by calling it from another function or directly from the Python prompt. Following is the example to call printme() function −

``` python title="example.py" linenums="1"
# Function definition is here
def printme( str ):
   "This prints a passed string into this function"
   print(str)
   return

# Now you can call printme function

printme("I'm first call to user defined function!")
printme("Again second call to the same function")
```

This will produce the following result −

``` python title="example.py" linenums="1"
I'm first call to user defined function!
Again second call to the same function
```