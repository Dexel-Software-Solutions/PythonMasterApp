import tkinter as tk
from tkinter import ttk, font
import tkinter.messagebox as messagebox
import webbrowser
import threading
import io
import contextlib
import traceback
import time
import re

# ─────────────────────────────────────────────
#  COLOUR PALETTE  (Navy Blue + White)
# ─────────────────────────────────────────────
C = {
    "bg_dark":    "#0A1628",   # deep navy background
    "bg_mid":     "#0D1F3C",   # section panels
    "bg_card":    "#112240",   # card / code blocks
    "accent":     "#1565C0",   # primary navy blue
    "accent2":    "#1976D2",   # lighter blue
    "highlight":  "#42A5F5",   # bright accent
    "gold":       "#FFC107",   # badge / star accent
    "white":      "#FFFFFF",
    "off_white":  "#E8F0FE",
    "muted":      "#90A4AE",
    "success":    "#00C853",
    "warning":    "#FF6D00",
    "code_bg":    "#060E1E",
    "code_text":  "#80CBC4",
    "tag_lib":    "#00695C",
    "ide_bg":     "#1E1E2E",
    "ide_line":   "#2A2A3E",
    "ide_gutter": "#181826",
    "cli_bg":     "#0C0C0C",
    "cli_text":   "#CCCCCC",
    "cli_prompt": "#00FF41",
    "tag_basic":  "#1565C0",
    "tag_adv":    "#6A1B9A",
    "tag_ext":    "#B71C1C",
    "tag_bh":     "#212121",
}

# ─────────────────────────────────────────────
#  FULL CURRICULUM DATA
# ─────────────────────────────────────────────
CURRICULUM = {

    # ══════════════════════════════════════════
    #  BASIC PYTHON
    # ══════════════════════════════════════════
    "🐍 Basic Python": [

        {
            "title": "Python හැඳින්වීම (Introduction)",
            "tag": "BASIC",
            "tag_color": C["tag_basic"],
            "content": """Python යනු 1991 දී Guido van Rossum විසින් සාදන ලද high-level, interpreted programming language එකක්.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Python ගේ විශේෂ ලක්ෂණ
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✦ Simple, readable syntax
  ✦ Interpreted language (line by line execute)
  ✦ Dynamically typed
  ✦ Object-Oriented, Functional, Procedural
  ✦ Huge standard library
  ✦ Cross-platform (Windows, Mac, Linux)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Python Install කරන්නෙ කොහොමද?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. python.org ට යන්න
  2. Download Python 3.x.x
  3. Install කරන්න ("Add to PATH" tick කරන්න!)
  4. CMD/Terminal: python --version

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  First Python Program
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""",
            "code": '''# ඔබේ පළමු Python Program
print("Hello, World!")
print("Python ඉගෙනගන්නෙ ගොඩක් ලේසියි!")

# නිෂ්පාදිත Output:
# Hello, World!
# Python ඉගෙනගන්නෙ ගොඩක් ලේසියි!'''
        },

        {
            "title": "Variables සහ Data Types",
            "tag": "BASIC",
            "tag_color": C["tag_basic"],
            "content": """Variables යනු data store කරගන්න memory locations.
Python වල variable declare කරන්ට type specify කරන්ට ඕනෙ නෑ!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Python Data Types
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  int       →  Integers (1, 2, -5, 1000)
  float     →  Decimals (3.14, -0.5)
  str       →  Strings ("Hello", 'World')
  bool      →  Boolean (True, False)
  list      →  [1, 2, 3]
  tuple     →  (1, 2, 3)
  dict      →  {"key": "value"}
  set       →  {1, 2, 3}
  NoneType  →  None

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Type Checking
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  type(variable)  →  type බලන්න
  isinstance()    →  type check කරන්න""",
            "code": '''# Variables declare කරන්නෙ කොහොමද?
name = "Demiyan"          # str
age = 25                  # int
height = 5.9              # float
is_student = True         # bool
nothing = None            # NoneType

# Multiple assignment
x = y = z = 0

# Swap variables
a, b = 10, 20
a, b = b, a               # a=20, b=10 දැන්

# Type checking
print(type(name))         # <class 'str'>
print(type(age))          # <class 'int'>
print(isinstance(age, int))  # True

# Type conversion
num_str = "42"
num_int = int(num_str)    # str → int
num_float = float(num_str)  # str → float
back_str = str(num_int)   # int → str'''
        },

        {
            "title": "Strings (String Manipulation)",
            "tag": "BASIC",
            "tag_color": C["tag_basic"],
            "content": """String යනු characters sequence එකක්. Python වල strings immutable.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  String Methods (වැදගත් ඒවා)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  .upper()       →  CAPITALS
  .lower()       →  lowercase
  .strip()       →  whitespace remove
  .split()       →  list into split
  .join()        →  list to string
  .replace()     →  replace text
  .find()        →  index find
  .count()       →  count occurrences
  .startswith()  →  starts with check
  .endswith()    →  ends with check
  .format()      →  string formatting
  .zfill()       →  zero padding

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  String Slicing
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  s[start:end:step]
  s[0]     →  first character
  s[-1]    →  last character
  s[::-1]  →  reverse""",
            "code": '''text = "Python Programming"

# Basic operations
print(text.upper())          # PYTHON PROGRAMMING
print(text.lower())          # python programming
print(len(text))             # 18
print(text[0])               # P
print(text[-1])              # g

# Slicing
print(text[0:6])             # Python
print(text[7:])              # Programming
print(text[::-1])            # gnimmargorP nohtyP

# String formatting (3 ways)
name = "Demiyan"
age = 25

# 1. f-string (නවතම, best method)
print(f"My name is {name}, I am {age} years old")

# 2. .format()
print("Hello {}! You are {}".format(name, age))

# 3. % operator (පරණ method)
print("Hello %s! Age: %d" % (name, age))

# Multiline strings
poem = """
Python is simple,
Python is great,
Let's learn today!
"""
print(poem)

# String methods
sentence = "  Hello, World!  "
print(sentence.strip())      # "Hello, World!"
print(sentence.split(","))   # ['  Hello', ' World!  ']'''
        },

        {
            "title": "Lists, Tuples, Sets, Dictionaries",
            "tag": "BASIC",
            "tag_color": C["tag_basic"],
            "content": """Python data structures - data organize කරගන්ට.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  List  [ ]  →  Ordered, Mutable
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  .append()    →  end එකට add
  .insert()    →  position add
  .remove()    →  value remove
  .pop()       →  index remove
  .sort()      →  sort කරනු
  .reverse()   →  reverse
  .index()     →  index find
  .count()     →  count

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Tuple  ( )  →  Ordered, Immutable
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Tuples change කරන්ට බෑ!
  Faster than lists
  Data protect කරන්ට use කරනු

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Dictionary  { }  →  Key-Value pairs
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  .keys()      →  all keys
  .values()    →  all values
  .items()     →  key-value pairs
  .get()       →  safe get
  .update()    →  update/add""",
            "code": '''# ── LIST ──────────────────────────────
fruits = ["apple", "banana", "cherry"]
fruits.append("mango")
fruits.insert(1, "grape")
fruits.remove("banana")
print(fruits)            # ['apple', 'grape', 'cherry', 'mango']
print(fruits[0])         # apple
print(fruits[-1])        # mango

# List comprehension (Advanced shortcut)
squares = [x**2 for x in range(1, 6)]
print(squares)           # [1, 4, 9, 16, 25]

# ── TUPLE ─────────────────────────────
coords = (10, 20, 30)
x, y, z = coords         # unpacking
print(x, y, z)           # 10 20 30

# ── DICTIONARY ────────────────────────
student = {
    "name": "Demiyan",
    "age": 25,
    "city": "Colombo",
    "skills": ["Python", "Java", "C++"]
}

print(student["name"])           # Demiyan
print(student.get("email", "N/A"))  # N/A (default)
student["email"] = "test@email.com"

for key, value in student.items():
    print(f"{key}: {value}")

# Dict comprehension
doubled = {k: v*2 for k, v in {"a":1,"b":2,"c":3}.items()}

# ── SET ───────────────────────────────
nums = {1, 2, 3, 3, 4, 4}    # duplicates remove
print(nums)                    # {1, 2, 3, 4}
a = {1, 2, 3}; b = {3, 4, 5}
print(a | b)   # union:        {1,2,3,4,5}
print(a & b)   # intersection: {3}
print(a - b)   # difference:   {1,2}'''
        },

        {
            "title": "If/Else සහ Control Flow",
            "tag": "BASIC",
            "tag_color": C["tag_basic"],
            "content": """Program flow control කරන statements.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Comparison Operators
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ==   equal to
  !=   not equal
  >    greater than
  <    less than
  >=   greater or equal
  <=   less or equal

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Logical Operators
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  and   →  both True
  or    →  one True
  not   →  opposite

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Ternary Operator (One-liner)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  value = X if condition else Y""",
            "code": '''# Basic if/elif/else
age = 20

if age < 13:
    print("Child")
elif age < 18:
    print("Teenager")
elif age < 60:
    print("Adult")
else:
    print("Senior")

# Logical operators
username = "admin"
password = "1234"

if username == "admin" and password == "1234":
    print("Login successful!")
else:
    print("Invalid credentials!")

# Ternary operator
score = 75
grade = "Pass" if score >= 50 else "Fail"
print(f"Result: {grade}")

# Nested conditions
num = 15
if num > 0:
    if num % 2 == 0:
        print("Positive even")
    else:
        print("Positive odd")
else:
    print("Negative")

# match/case (Python 3.10+)
day = "Monday"
match day:
    case "Saturday" | "Sunday":
        print("Weekend!")
    case "Monday":
        print("Start of week")
    case _:
        print("Weekday")'''
        },

        {
            "title": "Loops (for / while)",
            "tag": "BASIC",
            "tag_color": C["tag_basic"],
            "content": """Loops use කරලා code repeatedly execute කරනු.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  for Loop  →  known iterations
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  range(n)         →  0 to n-1
  range(a, b)      →  a to b-1
  range(a, b, s)   →  step s
  enumerate()      →  index + value
  zip()            →  multiple lists

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  while Loop  →  condition based
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  break     →  loop exit
  continue  →  skip iteration
  pass      →  do nothing
  else      →  loop end execute""",
            "code": '''# ── FOR LOOPS ─────────────────────────
# Basic range
for i in range(5):
    print(i, end=" ")   # 0 1 2 3 4

print()

# Iterating list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"Fruit: {fruit}")

# Enumerate (index + value)
for idx, fruit in enumerate(fruits, start=1):
    print(f"{idx}. {fruit}")

# Zip (multiple lists)
names = ["Alice", "Bob", "Charlie"]
scores = [90, 85, 92]
for name, score in zip(names, scores):
    print(f"{name}: {score}")

# Nested loops (Multiplication table)
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i}×{j}={i*j}", end="  ")
    print()

# ── WHILE LOOPS ───────────────────────
count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1

# break and continue
for num in range(10):
    if num == 3:
        continue      # skip 3
    if num == 7:
        break         # stop at 7
    print(num, end=" ")   # 0 1 2 4 5 6

# while with else
x = 0
while x < 3:
    print(x)
    x += 1
else:
    print("Loop completed!")'''
        },

        {
            "title": "Functions",
            "tag": "BASIC",
            "tag_color": C["tag_basic"],
            "content": """Functions - reusable code blocks. DRY principle (Don't Repeat Yourself).

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Function Types
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Regular functions    →  def keyword
  Lambda functions     →  anonymous
  Recursive functions  →  self-calling

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Parameters
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Positional   →  order matters
  Keyword      →  name=value
  Default      →  default value
  *args        →  variable positional
  **kwargs     →  variable keyword

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Scope
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Local    →  function inside
  Global   →  file level
  Nonlocal →  nested function""",
            "code": '''# Basic function
def greet(name):
    return f"Hello, {name}!"

print(greet("Demiyan"))       # Hello, Demiyan!

# Default parameters
def power(base, exp=2):
    return base ** exp

print(power(3))      # 9  (3²)
print(power(3, 3))   # 27 (3³)

# *args - multiple positional arguments
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3, 4, 5))  # 15

# **kwargs - multiple keyword arguments
def profile(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

profile(name="Demiyan", age=25, city="Colombo")

# Lambda function
square = lambda x: x ** 2
double = lambda x: x * 2
add = lambda x, y: x + y

print(square(5))      # 25
print(add(3, 4))      # 7

# Sorted with lambda
students = [("Alice", 90), ("Bob", 75), ("Charlie", 85)]
students.sort(key=lambda x: x[1], reverse=True)
print(students)

# Recursive function (Factorial)
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))   # 120

# Type hints (best practice)
def add_numbers(a: int, b: int) -> int:
    """Two numbers add කරනු."""
    return a + b'''
        },

        {
            "title": "File Handling (Files Read/Write)",
            "tag": "BASIC",
            "tag_color": C["tag_basic"],
            "content": """Files සමගම work කරන්නෙ කොහොමද?

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  File Modes
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  'r'   →  Read (default)
  'w'   →  Write (overwrite)
  'a'   →  Append
  'x'   →  Create (error if exists)
  'rb'  →  Read binary
  'wb'  →  Write binary

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  File Methods
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  .read()       →  whole file
  .readline()   →  one line
  .readlines()  →  list of lines
  .write()      →  write string
  .writelines() →  write list
  .seek()       →  cursor move
  .tell()       →  cursor position
  .close()      →  file close

⚠  ALWAYS use 'with' statement!
   (automatic file close guaranteed)""",
            "code": '''import os

# ── WRITE FILE ────────────────────────
with open("test.txt", "w", encoding="utf-8") as f:
    f.write("Hello, Python!\\n")
    f.write("File handling ඉගෙනගන්නෙ ලේසියි!\\n")
    f.writelines(["Line 3\\n", "Line 4\\n"])

# ── READ FILE ─────────────────────────
# Method 1: Full file
with open("test.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)

# Method 2: Line by line
with open("test.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())

# Method 3: readlines() → list
with open("test.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    print(lines)

# ── APPEND ────────────────────────────
with open("test.txt", "a", encoding="utf-8") as f:
    f.write("Appended line!\\n")

# ── OS MODULE (File system) ───────────
print(os.getcwd())               # current directory
print(os.listdir("."))           # list files
os.makedirs("new_folder", exist_ok=True)
os.rename("test.txt", "renamed.txt")
print(os.path.exists("renamed.txt"))  # True
print(os.path.getsize("renamed.txt")) # file size

# ── JSON FILES ────────────────────────
import json

data = {"name": "Demiyan", "age": 25, "skills": ["Python"]}

with open("data.json", "w") as f:
    json.dump(data, f, indent=4)

with open("data.json", "r") as f:
    loaded = json.load(f)
    print(loaded["name"])'''
        },

        {
            "title": "Exception Handling (Error Management)",
            "tag": "BASIC",
            "tag_color": C["tag_basic"],
            "content": """Errors handle කරලා program crash නොකරවන්නෙ කොහොමද?

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Common Exceptions
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ValueError        →  wrong value type
  TypeError         →  wrong data type
  IndexError        →  list out of range
  KeyError          →  dict key missing
  FileNotFoundError →  file not found
  ZeroDivisionError →  divide by zero
  AttributeError    →  no attribute
  ImportError       →  import fail
  NameError         →  var not defined

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  try/except Structure
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  try:      →  risky code
  except:   →  error handler
  else:     →  if no error
  finally:  →  always runs""",
            "code": '''# Basic try/except
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Multiple exceptions
try:
    num = int("abc")
    items = [1, 2, 3]
    print(items[10])
except ValueError as e:
    print(f"ValueError: {e}")
except IndexError as e:
    print(f"IndexError: {e}")
except Exception as e:
    print(f"Unknown error: {e}")
else:
    print("No errors occurred!")
finally:
    print("This always runs!")

# Custom Exception
class InsufficientFundsError(Exception):
    def __init__(self, amount, balance):
        self.amount = amount
        self.balance = balance
        super().__init__(
            f"Cannot withdraw {amount}. Balance: {balance}"
        )

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(amount, self.balance)
        self.balance -= amount
        return self.balance

account = BankAccount(1000)
try:
    account.withdraw(2000)
except InsufficientFundsError as e:
    print(e)

# Raising exceptions
def validate_age(age):
    if not isinstance(age, int):
        raise TypeError("Age must be an integer")
    if age < 0 or age > 150:
        raise ValueError(f"Invalid age: {age}")
    return age'''
        },
    ],

    # ══════════════════════════════════════════
    #  ADVANCED PYTHON
    # ══════════════════════════════════════════
    "⚙️ Advanced Python": [

        {
            "title": "Object-Oriented Programming (OOP)",
            "tag": "ADVANCED",
            "tag_color": C["tag_adv"],
            "content": """OOP - real world objects code කරන programming paradigm.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  4 Pillars of OOP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Encapsulation   →  data hiding
  2. Inheritance     →  parent → child
  3. Polymorphism    →  many forms
  4. Abstraction     →  hide details

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Class Special Methods (Dunder)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  __init__     →  constructor
  __str__      →  string repr
  __repr__     →  developer repr
  __len__      →  len() support
  __eq__       →  == operator
  __lt__       →  < operator
  __add__      →  + operator
  __del__      →  destructor""",
            "code": '''# ── CLASS DEFINITION ─────────────────
class Animal:
    species_count = 0  # class variable

    def __init__(self, name, sound):
        self.name = name        # instance variable
        self.__sound = sound    # private (encapsulation)
        Animal.species_count += 1

    def speak(self):
        return f"{self.name} says {self.__sound}"

    def __str__(self):
        return f"Animal({self.name})"

    def __repr__(self):
        return f"Animal(name='{self.name}')"

    @classmethod
    def get_count(cls):
        return cls.species_count

    @staticmethod
    def is_animal(obj):
        return isinstance(obj, Animal)

# ── INHERITANCE ──────────────────────
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Woof!")
        self.breed = breed

    def fetch(self):
        return f"{self.name} fetches the ball!"

    def speak(self):  # Method Override
        return f"{self.name} barks loudly!"

class Cat(Animal):
    def speak(self):  # Polymorphism
        return f"{self.name} meows softly!"

# ── USAGE ─────────────────────────────
dog = Dog("Rex", "German Shepherd")
cat = Cat("Whiskers", "Woof")

print(dog.speak())              # Rex barks loudly!
print(cat.speak())              # Whiskers meows softly!
print(Dog.get_count())          # 2

# Polymorphism in action
animals = [dog, cat]
for animal in animals:
    print(animal.speak())       # Each has own speak()

# Multiple Inheritance
class FlyingAnimal(Animal):
    def fly(self): return "Flying!"

class Duck(Dog, FlyingAnimal):
    pass'''
        },

        {
            "title": "Decorators සහ Context Managers",
            "tag": "ADVANCED",
            "tag_color": C["tag_adv"],
            "content": """Decorators - functions modify කරන powerful Python feature.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Decorator Types
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Function decorators
  Class decorators
  @property
  @classmethod
  @staticmethod
  @functools.wraps
  @dataclass

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Context Managers
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  with statement
  __enter__ / __exit__
  contextlib module
  @contextmanager""",
            "code": '''import time
import functools
from contextlib import contextmanager

# ── FUNCTION DECORATOR ────────────────
def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end-start:.4f}s")
        return result
    return wrapper

def logger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

# ── STACKING DECORATORS ───────────────
@timer
@logger
def slow_function(n):
    time.sleep(0.1)
    return n * 2

slow_function(5)

# ── DECORATOR WITH ARGUMENTS ──────────
def repeat(n):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Demiyan")   # prints 3 times

# ── CONTEXT MANAGER ───────────────────
@contextmanager
def timer_context(name):
    start = time.time()
    try:
        yield
    finally:
        elapsed = time.time() - start
        print(f"{name}: {elapsed:.4f}s")

with timer_context("My block"):
    time.sleep(0.2)

# Custom context manager class
class DatabaseConnection:
    def __enter__(self):
        print("Connecting to DB...")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Closing DB connection...")
        return False  # don't suppress exceptions

with DatabaseConnection() as db:
    print("Querying database...")'''
        },

        {
            "title": "Generators සහ Iterators",
            "tag": "ADVANCED",
            "tag_color": C["tag_adv"],
            "content": """Memory-efficient data processing - large datasets handle කරන්ට.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Generator vs List
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  List        →  all in memory (RAM)
  Generator   →  one at a time (lazy)

  1 million numbers:
  List      →  ~8 MB RAM
  Generator →  ~120 bytes RAM!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  yield keyword
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  yield         →  value produce
  yield from    →  delegate generator
  next()        →  next value get
  StopIteration →  exhausted signal

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Iterator Protocol
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  __iter__()   →  return self
  __next__()   →  next value""",
            "code": '''import sys

# ── GENERATOR FUNCTION ────────────────
def count_up(n):
    i = 0
    while i < n:
        yield i       # pause and produce
        i += 1

gen = count_up(5)
print(next(gen))     # 0
print(next(gen))     # 1
print(next(gen))     # 2

for num in count_up(3):
    print(num)        # 0, 1, 2

# Memory comparison
list_nums = list(range(1_000_000))
gen_nums = (x for x in range(1_000_000))  # generator expression

print(sys.getsizeof(list_nums))  # ~8 MB
print(sys.getsizeof(gen_nums))   # ~120 bytes!

# ── INFINITE GENERATOR ────────────────
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
first_10 = [next(fib) for _ in range(10)]
print(first_10)  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# ── CUSTOM ITERATOR CLASS ─────────────
class Range:
    def __init__(self, start, stop, step=1):
        self.current = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.stop:
            raise StopIteration
        value = self.current
        self.current += self.step
        return value

for num in Range(0, 10, 2):
    print(num, end=" ")  # 0 2 4 6 8

# ── GENERATOR PIPELINE ────────────────
def read_numbers():
    for i in range(100):
        yield i

def filter_even(numbers):
    for n in numbers:
        if n % 2 == 0:
            yield n

def square(numbers):
    for n in numbers:
        yield n ** 2

pipeline = square(filter_even(read_numbers()))
print(list(pipeline)[:5])  # [0, 4, 16, 36, 64]'''
        },

        {
            "title": "Threading සහ Multiprocessing",
            "tag": "ADVANCED",
            "tag_color": C["tag_adv"],
            "content": """Concurrent programming - multiple tasks same time execute.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Threading vs Multiprocessing
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Threading
  ├─ Shared memory
  ├─ Best for I/O bound tasks
  ├─ GIL limitation (CPython)
  └─ Lightweight

  Multiprocessing
  ├─ Separate memory
  ├─ Best for CPU bound tasks
  ├─ True parallelism
  └─ Higher overhead

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  async/await (asyncio)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Single thread, cooperative
  Best for network I/O
  await = pause and let others run""",
            "code": '''import threading
import multiprocessing
import asyncio
import time

# ── THREADING ─────────────────────────
def download_file(filename, delay):
    print(f"Downloading {filename}...")
    time.sleep(delay)
    print(f"{filename} downloaded!")

# Sequential (slow)
start = time.time()
download_file("file1.txt", 2)
download_file("file2.txt", 2)
print(f"Sequential: {time.time()-start:.1f}s")  # 4.0s

# Threaded (fast)
start = time.time()
t1 = threading.Thread(target=download_file, args=("file1.txt", 2))
t2 = threading.Thread(target=download_file, args=("file2.txt", 2))
t1.start(); t2.start()
t1.join();  t2.join()
print(f"Threaded: {time.time()-start:.1f}s")    # 2.0s

# Thread synchronization (Lock)
counter = 0
lock = threading.Lock()

def increment():
    global counter
    for _ in range(1000):
        with lock:
            counter += 1

# ── MULTIPROCESSING ───────────────────
def cpu_intensive(n):
    return sum(i**2 for i in range(n))

if __name__ == "__main__":
    with multiprocessing.Pool(4) as pool:
        results = pool.map(cpu_intensive, [1000]*4)
    print(results)

# ── ASYNCIO ───────────────────────────
async def fetch_data(url, delay):
    print(f"Fetching {url}...")
    await asyncio.sleep(delay)  # non-blocking wait
    print(f"{url} fetched!")
    return f"Data from {url}"

async def main():
    tasks = [
        fetch_data("api1.com", 2),
        fetch_data("api2.com", 1),
        fetch_data("api3.com", 3),
    ]
    results = await asyncio.gather(*tasks)
    return results

# asyncio.run(main())  # Run event loop'''
        },

        {
            "title": "Regular Expressions (RegEx)",
            "tag": "ADVANCED",
            "tag_color": C["tag_adv"],
            "content": """Pattern matching - text search/validate කරන powerful tool.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Special Characters
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  .     any char (except newline)
  ^     start of string
  $     end of string
  *     0 or more
  +     1 or more
  ?     0 or 1 (optional)
  {n}   exactly n times
  {n,m} n to m times

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Character Classes
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  \\d    digit [0-9]
  \\D    non-digit
  \\w    word [a-zA-Z0-9_]
  \\W    non-word
  \\s    whitespace
  \\S    non-whitespace
  [abc] any of a, b, c
  [^abc] not a, b, c

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  re Module Functions
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  re.match()    →  start of string
  re.search()   →  anywhere
  re.findall()  →  all matches (list)
  re.finditer() →  all matches (iter)
  re.sub()      →  replace
  re.split()    →  split by pattern""",
            "code": '''import re

# ── BASIC MATCHING ────────────────────
text = "Contact us at info@example.com or support@test.org"

# Email pattern
email_pattern = r"[\\w.-]+@[\\w.-]+\\.\\w+"
emails = re.findall(email_pattern, text)
print(emails)  # ['info@example.com', 'support@test.org']

# ── PHONE NUMBERS ─────────────────────
phones = "Call 071-2345678 or 011-9876543 now!"
pattern = r"\\d{3}-\\d{7}"
found = re.findall(pattern, phones)
print(found)   # ['071-2345678', '011-9876543']

# ── GROUPS ────────────────────────────
log = "2024-01-15 10:30:45 ERROR Database connection failed"
pattern = r"(\\d{4}-\\d{2}-\\d{2}) (\\d{2}:\\d{2}:\\d{2}) (\\w+) (.+)"
match = re.search(pattern, log)
if match:
    date, time, level, message = match.groups()
    print(f"Date: {date}, Level: {level}")

# ── VALIDATION ────────────────────────
def validate_email(email):
    pattern = r"^[\\w.-]+@[\\w.-]+\\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))

def validate_password(pwd):
    # Min 8 chars, uppercase, lowercase, digit, special
    checks = [
        len(pwd) >= 8,
        re.search(r"[A-Z]", pwd),
        re.search(r"[a-z]", pwd),
        re.search(r"\\d", pwd),
        re.search(r"[!@#$%^&*]", pwd),
    ]
    return all(checks)

print(validate_email("test@example.com"))  # True
print(validate_password("Secure@123"))     # True

# ── SUBSTITUTION ─────────────────────
text = "My phone: 071-1234567"
# Mask phone number
masked = re.sub(r"\\d{3}-\\d{7}", "XXX-XXXXXXX", text)
print(masked)  # My phone: XXX-XXXXXXX

# ── SPLIT ─────────────────────────────
data = "apple;banana,cherry|grape"
fruits = re.split(r"[;,|]", data)
print(fruits)  # ['apple', 'banana', 'cherry', 'grape']'''
        },

        {
            "title": "Database (SQLite / SQLAlchemy)",
            "tag": "ADVANCED",
            "tag_color": C["tag_adv"],
            "content": """Python සමගම databases use කරන්නෙ කොහොමද?

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  SQLite (Built-in)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  No server needed!
  File-based database
  Perfect for small apps

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  CRUD Operations
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  CREATE  →  Table create
  INSERT  →  Data add
  SELECT  →  Data read
  UPDATE  →  Data update
  DELETE  →  Data delete

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  SQLAlchemy ORM
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Python objects → SQL
  Database agnostic
  Query building""",
            "code": '''import sqlite3
from datetime import datetime

# ── SQLITE BASIC ──────────────────────
conn = sqlite3.connect("school.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        grade REAL,
        enrolled_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
""")
conn.commit()

# Insert data
students_data = [
    ("Alice", 20, 3.8),
    ("Bob", 22, 3.2),
    ("Charlie", 21, 3.9),
]
cursor.executemany(
    "INSERT INTO students (name, age, grade) VALUES (?, ?, ?)",
    students_data
)
conn.commit()

# Select data
cursor.execute("SELECT * FROM students ORDER BY grade DESC")
rows = cursor.fetchall()
for row in rows:
    print(f"ID:{row[0]} | {row[1]} | Age:{row[2]} | GPA:{row[3]}")

# Update
cursor.execute(
    "UPDATE students SET grade = ? WHERE name = ?",
    (4.0, "Alice")
)
conn.commit()

# Delete
cursor.execute("DELETE FROM students WHERE grade < ?", (3.5,))
conn.commit()

# Parameterized queries (SQL injection prevention!)
name = "Alice"
cursor.execute("SELECT * FROM students WHERE name = ?", (name,))

# Context manager (auto close)
with sqlite3.connect("school.db") as conn:
    df = conn.execute("SELECT COUNT(*) FROM students")
    print(f"Total: {df.fetchone()[0]}")

conn.close()'''
        },
    ],

    # ══════════════════════════════════════════
    #  EXTREME PYTHON
    # ══════════════════════════════════════════
    "🔥 Extreme Python": [

        {
            "title": "Metaclasses සහ Descriptors",
            "tag": "EXTREME",
            "tag_color": C["tag_ext"],
            "content": """Python's most powerful (and dangerous) features.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Metaclass
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  "Class of a class"
  Classes are objects in Python!
  type() is the default metaclass

  class MyClass:
      metaclass = type  (implicit)

  Metaclass controls:
  ├─ Class creation
  ├─ Attribute validation
  ├─ Method injection
  └─ Singleton pattern

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Descriptor Protocol
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  __get__    →  attribute access
  __set__    →  attribute assign
  __delete__ →  attribute delete

  Powers behind:
  @property, @classmethod, @staticmethod""",
            "code": '''# ── METACLASS ─────────────────────────
class SingletonMeta(type):
    """Only one instance allowed!"""
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Database(metaclass=SingletonMeta):
    def __init__(self, url):
        self.url = url

db1 = Database("localhost:5432")
db2 = Database("localhost:5432")
print(db1 is db2)  # True! Same object!

# ── VALIDATION METACLASS ──────────────
class ValidatedMeta(type):
    def __new__(mcs, name, bases, namespace):
        for key, value in namespace.items():
            if callable(value) and not key.startswith("_"):
                # All public methods must have docstrings
                if not value.__doc__:
                    raise TypeError(
                        f"Method {key} must have a docstring!"
                    )
        return super().__new__(mcs, name, bases, namespace)

# ── DESCRIPTOR ────────────────────────
class TypeValidator:
    def __init__(self, name, expected_type):
        self.name = name
        self.expected_type = expected_type

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return getattr(obj, f"_{self.name}", None)

    def __set__(self, obj, value):
        if not isinstance(value, self.expected_type):
            raise TypeError(
                f"{self.name} must be {self.expected_type.__name__}"
            )
        setattr(obj, f"_{self.name}", value)

class Person:
    name = TypeValidator("name", str)
    age = TypeValidator("age", int)

    def __init__(self, name, age):
        self.name = name  # triggers __set__
        self.age = age

p = Person("Demiyan", 25)
try:
    p.age = "twenty"  # raises TypeError!
except TypeError as e:
    print(e)'''
        },

        {
            "title": "Memory Management සහ Performance",
            "tag": "EXTREME",
            "tag_color": C["tag_ext"],
            "content": """Python internals - memory optimize කරන්නෙ කොහොමද?

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Python Memory Model
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Everything is an object!
  Reference counting (main GC)
  Cyclic garbage collector
  Memory pools (pymalloc)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Performance Tools
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  timeit     →  code timing
  cProfile   →  profiling
  memory_profiler → RAM usage
  __slots__  →  memory reduce
  weakref    →  weak references

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Optimization Techniques
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  List comp > loops
  Local vars > global
  Generator > list (large data)
  dict/set > list (lookups)
  join() > + (strings)
  numpy > pure Python (math)""",
            "code": '''import sys
import timeit
import cProfile
import weakref
from functools import lru_cache

# ── MEMORY: __slots__ ─────────────────
class WithoutSlots:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class WithSlots:
    __slots__ = ("x", "y")  # no __dict__!
    def __init__(self, x, y):
        self.x = x
        self.y = y

a = WithoutSlots(1, 2)
b = WithSlots(1, 2)
print(sys.getsizeof(a.__dict__))  # 232 bytes
# WithSlots has no __dict__ → much smaller!

# ── CACHING with lru_cache ────────────
@lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2: return n
    return fibonacci(n-1) + fibonacci(n-2)

# First call: computes
# Subsequent calls: instant (cached)!
print(fibonacci(50))   # instant!

# ── WEAK REFERENCES ───────────────────
class BigData:
    def __init__(self, data):
        self.data = data

data = BigData([1] * 1000000)
weak_ref = weakref.ref(data)

print(weak_ref())   # BigData object
del data            # garbage collected!
print(weak_ref())   # None (gone!)

# ── PERFORMANCE COMPARISON ────────────
# String concatenation
def bad_concat(n):
    s = ""
    for i in range(n):
        s += str(i)  # creates new string each time!
    return s

def good_concat(n):
    return "".join(str(i) for i in range(n))  # fast!

t1 = timeit.timeit(lambda: bad_concat(1000), number=100)
t2 = timeit.timeit(lambda: good_concat(1000), number=100)
print(f"Bad: {t1:.3f}s | Good: {t2:.3f}s")

# ── PROFILING ─────────────────────────
def profile_me():
    data = [i**2 for i in range(10000)]
    total = sum(data)
    return total

cProfile.run("profile_me()")

# ── OBJECT INTERNING ──────────────────
# Small ints (-5 to 256) are cached!
a = 256; b = 256
print(a is b)    # True (same object)
a = 257; b = 257
print(a is b)    # False (different objects)'''
        },

        {
            "title": "Design Patterns (Gang of Four)",
            "tag": "EXTREME",
            "tag_color": C["tag_ext"],
            "content": """Professional software architecture patterns.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Creational Patterns
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Singleton   →  one instance only
  Factory     →  object creation
  Builder     →  step-by-step build
  Prototype   →  clone objects

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Structural Patterns
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Adapter     →  interface convert
  Decorator   →  add functionality
  Facade      →  simple interface
  Proxy       →  access control

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Behavioral Patterns
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Observer    →  event system
  Strategy    →  algorithm swap
  Command     →  action encapsulate
  Iterator    →  sequential access""",
            "code": '''from abc import ABC, abstractmethod

# ── FACTORY PATTERN ───────────────────
class Animal(ABC):
    @abstractmethod
    def speak(self): pass

class Dog(Animal):
    def speak(self): return "Woof!"

class Cat(Animal):
    def speak(self): return "Meow!"

class AnimalFactory:
    @staticmethod
    def create(animal_type: str) -> Animal:
        animals = {"dog": Dog, "cat": Cat}
        cls = animals.get(animal_type.lower())
        if not cls:
            raise ValueError(f"Unknown: {animal_type}")
        return cls()

dog = AnimalFactory.create("dog")
print(dog.speak())   # Woof!

# ── OBSERVER PATTERN ──────────────────
class EventSystem:
    def __init__(self):
        self._subscribers = {}

    def subscribe(self, event, callback):
        self._subscribers.setdefault(event, []).append(callback)

    def emit(self, event, data=None):
        for cb in self._subscribers.get(event, []):
            cb(data)

events = EventSystem()
events.subscribe("login", lambda u: print(f"User {u} logged in"))
events.subscribe("login", lambda u: print(f"Sending welcome email to {u}"))
events.emit("login", "Demiyan")

# ── STRATEGY PATTERN ──────────────────
class SortStrategy(ABC):
    @abstractmethod
    def sort(self, data: list) -> list: pass

class BubbleSort(SortStrategy):
    def sort(self, data):
        # Implementation
        return sorted(data)  # simplified

class QuickSort(SortStrategy):
    def sort(self, data):
        if len(data) <= 1: return data
        pivot = data[0]
        left = [x for x in data[1:] if x <= pivot]
        right = [x for x in data[1:] if x > pivot]
        return self.sort(left) + [pivot] + self.sort(right)

class Sorter:
    def __init__(self, strategy: SortStrategy):
        self._strategy = strategy

    def sort(self, data):
        return self._strategy.sort(data)

data = [3, 1, 4, 1, 5, 9, 2, 6]
sorter = Sorter(QuickSort())
print(sorter.sort(data))'''
        },

        {
            "title": "Type System සහ Protocol",
            "tag": "EXTREME",
            "tag_color": C["tag_ext"],
            "content": """Python 3.x type system - production code quality.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Type Hints (PEP 484+)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Basic types
  Optional[T]   →  T | None
  Union[T1, T2] →  T1 | T2 (3.10+)
  List[T]       →  list of T
  Dict[K, V]    →  dict
  Tuple[T, ...] →  tuple
  Callable[[A], R] →  function
  TypeVar       →  generic type

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  dataclasses
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Auto __init__, __repr__, __eq__
  field() for defaults
  post_init for validation
  frozen=True for immutable

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Protocol (Structural Subtyping)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  "If it walks like a duck..."
  No inheritance needed
  Static duck typing""",
            "code": '''from typing import TypeVar, Generic, Protocol, runtime_checkable
from dataclasses import dataclass, field
from typing import Optional, List, Dict, Callable

# ── DATACLASS ─────────────────────────
@dataclass
class Product:
    name: str
    price: float
    quantity: int = 0
    tags: List[str] = field(default_factory=list)

    def __post_init__(self):
        if self.price < 0:
            raise ValueError("Price cannot be negative!")
        if self.quantity < 0:
            raise ValueError("Quantity cannot be negative!")

    @property
    def total_value(self) -> float:
        return self.price * self.quantity

@dataclass(frozen=True)  # immutable!
class Point:
    x: float
    y: float

    def distance_to(self, other: "Point") -> float:
        return ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5

p1 = Point(0, 0)
p2 = Point(3, 4)
print(p2.distance_to(p1))   # 5.0

# ── GENERICS ──────────────────────────
T = TypeVar("T")

class Stack(Generic[T]):
    def __init__(self):
        self._items: List[T] = []

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> T:
        return self._items.pop()

int_stack: Stack[int] = Stack()
int_stack.push(1)
int_stack.push(2)

# ── PROTOCOL ──────────────────────────
@runtime_checkable
class Drawable(Protocol):
    def draw(self) -> str: ...
    def get_area(self) -> float: ...

class Circle:
    def __init__(self, radius: float):
        self.radius = radius
    def draw(self) -> str: return "○"
    def get_area(self) -> float: return 3.14 * self.radius**2

class Square:
    def __init__(self, side: float):
        self.side = side
    def draw(self) -> str: return "□"
    def get_area(self) -> float: return self.side**2

def render_all(shapes: List[Drawable]) -> None:
    for shape in shapes:
        print(f"{shape.draw()} Area: {shape.get_area():.2f}")

shapes = [Circle(5), Square(4)]
render_all(shapes)   # Works without inheritance!'''
        },
    ],

    # ══════════════════════════════════════════
    #  BLACK HAT PYTHON
    # ══════════════════════════════════════════
    "🖤 Black Hat Python": [

        {
            "title": "⚠️ Ethics & Legal Disclaimer",
            "tag": "BLACK HAT",
            "tag_color": C["tag_bh"],
            "content": """⚠  IMPORTANT DISCLAIMER ⚠

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ⚖  LEGAL & ETHICAL NOTICE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  මෙහි ඇති knowledge EDUCATIONAL
  purposes ONLY සදහා!

  ✦ Own systems/networks ONLY test
  ✦ Permission ලැබූ systems only
  ✦ CTF (Capture The Flag) events
  ✦ Penetration Testing (with auth)
  ✦ Security Research

  ❌ ILLEGAL activities සදහා
     use කිරීම PROHIBITED!

  Sri Lanka Computer Crimes Act
  (No. 24 of 2007) violations
  serious penalties!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Ethical Hacker vs Black Hat
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  White Hat  →  Permission + Fix
  Gray Hat   →  No permission, disclose
  Black Hat  →  Malicious intent ❌

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Certifications (Legal Path)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  CEH   - Certified Ethical Hacker
  OSCP  - Offensive Security
  CompTIA Security+
  CISSP - Information Security

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  This section covers:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Network Programming fundamentals
  Socket programming
  Port scanning (own network!)
  Basic network tools
  Cryptography basics""",
            "code": '''# ⚠  EDUCATIONAL PURPOSES ONLY ⚠
#
# සියලු code examples:
# - Own machines/VMs only
# - Lab environments only
# - Legal permission ඇති systems only
#
# Responsible Disclosure:
# Vulnerabilities find කළාම:
# 1. System owner ට notify කරන්න
# 2. Reasonable time දෙන්න fix කරන්ට
# 3. Public ට disclose කරන්න
#
# Bug Bounty Programs:
# - HackerOne (hackerone.com)
# - Bugcrowd (bugcrowd.com)
# - Google VRP
# - Microsoft MSRC

print("Be a White Hat, not a Black Hat!")
print("Protect systems, don't attack them!")'''
        },

        {
            "title": "Network Programming Fundamentals",
            "tag": "BLACK HAT",
            "tag_color": C["tag_bh"],
            "content": """Network programming - cybersecurity foundation.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Socket Types
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  SOCK_STREAM   →  TCP (reliable)
  SOCK_DGRAM    →  UDP (fast)
  SOCK_RAW      →  Raw packets

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Address Families
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  AF_INET   →  IPv4
  AF_INET6  →  IPv6
  AF_UNIX   →  Local socket

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  TCP Handshake
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Client → SYN      → Server
  Client ← SYN-ACK  ← Server
  Client → ACK      → Server
  Connection established!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Common Ports
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  21   FTP     80  HTTP
  22   SSH     443 HTTPS
  23   Telnet  3306 MySQL
  25   SMTP    5432 PostgreSQL
  53   DNS     8080 HTTP Alt""",
            "code": '''import socket
import threading

# ── TCP SERVER ────────────────────────
def start_server(host="127.0.0.1", port=9999):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((host, port))
    server.listen(5)
    print(f"[*] Server listening on {host}:{port}")

    def handle_client(conn, addr):
        print(f"[+] Connection from {addr}")
        while True:
            data = conn.recv(4096)
            if not data:
                break
            message = data.decode("utf-8")
            print(f"[{addr}]: {message}")
            conn.send(f"Echo: {message}".encode("utf-8"))
        conn.close()

    while True:
        conn, addr = server.accept()
        t = threading.Thread(target=handle_client, args=(conn, addr))
        t.daemon = True
        t.start()

# ── TCP CLIENT ────────────────────────
def tcp_client(host="127.0.0.1", port=9999):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    try:
        while True:
            message = input("Message: ")
            if message.lower() == "quit":
                break
            client.send(message.encode("utf-8"))
            response = client.recv(4096)
            print(f"Server: {response.decode('utf-8')}")
    finally:
        client.close()

# ── UDP EXAMPLE ───────────────────────
def udp_server(port=9998):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("0.0.0.0", port))
    while True:
        data, addr = sock.recvfrom(65535)
        print(f"UDP from {addr}: {data.decode()}")
        sock.sendto(b"ACK", addr)

# ── HOSTNAME RESOLUTION ───────────────
print(socket.gethostbyname("google.com"))
print(socket.gethostname())

# ── BANNER GRABBING ───────────────────
def grab_banner(ip, port, timeout=3):
    try:
        sock = socket.socket()
        sock.settimeout(timeout)
        sock.connect((ip, port))
        sock.send(b"HEAD / HTTP/1.0\\r\\n\\r\\n")
        banner = sock.recv(1024)
        return banner.decode(errors="ignore")
    except Exception as e:
        return str(e)
    finally:
        sock.close()'''
        },

        {
            "title": "Port Scanner (Own Network Only!)",
            "tag": "BLACK HAT",
            "tag_color": C["tag_bh"],
            "content": """Port scanner - network security testing tool.
⚠  Own network / Lab ONLY!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  How Port Scanning Works
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  TCP Connect Scan
  ├─ Full TCP handshake
  ├─ Reliable, slow
  └─ Easily detected

  SYN Scan (Half-Open)
  ├─ SYN → SYN-ACK → RST
  ├─ Fast, less logged
  └─ Root required

  UDP Scan
  ├─ Send UDP packet
  ├─ ICMP unreachable = closed
  └─ Slow, unreliable

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Tools (Industry Standard)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  nmap      →  professional scanner
  masscan   →  ultra-fast
  zmap      →  internet-scale""",
            "code": '''import socket
import concurrent.futures
import ipaddress
from datetime import datetime

# ⚠  OWN SYSTEMS ONLY - EDUCATIONAL ⚠

COMMON_PORTS = {
    21: "FTP", 22: "SSH", 23: "Telnet",
    25: "SMTP", 53: "DNS", 80: "HTTP",
    110: "POP3", 143: "IMAP", 443: "HTTPS",
    445: "SMB", 3306: "MySQL", 3389: "RDP",
    5432: "PostgreSQL", 6379: "Redis",
    8080: "HTTP-Alt", 27017: "MongoDB"
}

def check_port(host: str, port: int, timeout: float = 1.0):
    """Check if a port is open."""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((host, port))
        sock.close()
        if result == 0:
            service = COMMON_PORTS.get(port, "unknown")
            try:
                sock2 = socket.socket()
                sock2.settimeout(1)
                sock2.connect((host, port))
                sock2.send(b"\\r\\n")
                banner = sock2.recv(100).decode(errors="ignore").strip()
                sock2.close()
            except:
                banner = ""
            return port, True, service, banner
        return port, False, "", ""
    except Exception:
        return port, False, "", ""

def port_scanner(host: str, start: int = 1, end: int = 1024):
    """Multi-threaded port scanner."""
    print(f"\\n{'='*50}")
    print(f"  Port Scanner - Target: {host}")
    print(f"  Range: {start}-{end}")
    print(f"  Started: {datetime.now():%Y-%m-%d %H:%M:%S}")
    print(f"{'='*50}\\n")

    try:
        ip = socket.gethostbyname(host)
        print(f"  IP: {ip}\\n")
    except socket.gaierror:
        print(f"  Cannot resolve: {host}")
        return

    open_ports = []
    ports = range(start, end + 1)

    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        futures = {executor.submit(check_port, ip, p): p for p in ports}
        for future in concurrent.futures.as_completed(futures):
            port, is_open, service, banner = future.result()
            if is_open:
                open_ports.append((port, service, banner))
                print(f"  [OPEN] {port:5d}/tcp  {service:12s}  {banner[:30]}")

    print(f"\\n  Found {len(open_ports)} open ports")
    print(f"  Completed: {datetime.now():%H:%M:%S}")
    return open_ports

# Usage (localhost only for safety!):
# port_scanner("127.0.0.1", 1, 1024)
# port_scanner("192.168.1.1", 1, 100)  # own router'''
        },

        {
            "title": "Cryptography සහ Hashing",
            "tag": "BLACK HAT",
            "tag_color": C["tag_bh"],
            "content": """Encryption, decryption, hashing - data security.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Symmetric Encryption
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Same key for encrypt + decrypt
  AES (Advanced Encryption Standard)
  AES-128, AES-192, AES-256
  Modes: ECB, CBC, GCM, CTR

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Asymmetric Encryption
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Public key + Private key pair
  RSA (most common)
  ECC (Elliptic Curve)
  Public: encrypt
  Private: decrypt

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Hashing (One-Way)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  MD5    →  128-bit (broken!)
  SHA-1  →  160-bit (weak!)
  SHA-256 → 256-bit (secure)
  SHA-512 → 512-bit (very secure)
  bcrypt  → password hashing
  Argon2  → best for passwords""",
            "code": '''import hashlib
import hmac
import secrets
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding

# ── HASHING ───────────────────────────
def hash_password(password: str, salt: bytes = None) -> tuple:
    if salt is None:
        salt = secrets.token_bytes(32)
    key = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        salt,
        iterations=100000  # slow = harder to brute-force
    )
    return key, salt

def verify_password(password: str, key: bytes, salt: bytes) -> bool:
    new_key, _ = hash_password(password, salt)
    return hmac.compare_digest(key, new_key)  # timing-safe!

key, salt = hash_password("SecurePass@123")
print(verify_password("SecurePass@123", key, salt))  # True
print(verify_password("WrongPass", key, salt))        # False

# ── SHA HASHING ───────────────────────
data = "Hello, Python!"
print(hashlib.md5(data.encode()).hexdigest())     # (DON'T use for passwords)
print(hashlib.sha256(data.encode()).hexdigest())  # secure hash
print(hashlib.sha512(data.encode()).hexdigest())  # very secure

# ── SYMMETRIC (Fernet/AES) ────────────
# Generate key
key = Fernet.generate_key()
f = Fernet(key)

message = b"Secret message!"
encrypted = f.encrypt(message)
decrypted = f.decrypt(encrypted)

print(f"Original:  {message}")
print(f"Encrypted: {encrypted}")
print(f"Decrypted: {decrypted}")

# ── ASYMMETRIC (RSA) ──────────────────
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)
public_key = private_key.public_key()

message = b"Secret RSA message"
ciphertext = public_key.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
plaintext = private_key.decrypt(ciphertext, padding.OAEP(
    mgf=padding.MGF1(algorithm=hashes.SHA256()),
    algorithm=hashes.SHA256(), label=None
))
print(f"RSA Decrypted: {plaintext}")

# ── SECURE RANDOM ─────────────────────
token = secrets.token_hex(32)      # random hex
url_token = secrets.token_urlsafe() # URL-safe
otp = secrets.randbelow(1000000)   # 0-999999'''
        },

        {
            "title": "Web Scraping සහ OSINT",
            "tag": "BLACK HAT",
            "tag_color": C["tag_bh"],
            "content": """Web scraping - publicly available data collect.
⚠  robots.txt respect කරන්න!
⚠  Terms of Service read කරන්න!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Tools
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  requests     →  HTTP requests
  BeautifulSoup →  HTML parse
  Scrapy       →  full framework
  Selenium     →  browser automation
  Playwright   →  modern browser

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  OSINT (Open Source Intelligence)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Publicly available information
  Social media analysis
  Domain/IP research
  Employee enumeration
  Technology fingerprinting

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Legal OSINT Sources
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Shodan      →  Internet devices
  Censys      →  Certificate data
  WHOIS       →  Domain info
  Wayback Machine → Historical
  Hunter.io   →  Email finder""",
            "code": '''import requests
from bs4 import BeautifulSoup
import socket
import whois    # pip install python-whois
import json
import time

# ── BASIC WEB SCRAPER ─────────────────
def scrape_website(url: str) -> dict:
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    try:
        resp = requests.get(url, headers=headers, timeout=10)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")

        return {
            "title": soup.title.text if soup.title else "N/A",
            "links": [a.get("href") for a in soup.find_all("a", href=True)][:10],
            "headings": [h.text.strip() for h in soup.find_all(["h1","h2","h3"])[:5]],
            "meta_description": soup.find("meta", {"name":"description"}),
        }
    except requests.RequestException as e:
        return {"error": str(e)}

# ── DOMAIN OSINT ──────────────────────
def domain_recon(domain: str) -> dict:
    result = {}

    # IP Resolution
    try:
        result["ip"] = socket.gethostbyname(domain)
        result["hostname"] = socket.getfqdn(domain)
    except socket.gaierror as e:
        result["ip_error"] = str(e)

    # WHOIS
    try:
        w = whois.whois(domain)
        result["registrar"] = w.registrar
        result["creation_date"] = str(w.creation_date)
        result["expiration_date"] = str(w.expiration_date)
        result["name_servers"] = w.name_servers
    except Exception as e:
        result["whois_error"] = str(e)

    # Check common subdomains
    subdomains = ["www", "mail", "ftp", "admin", "api", "dev"]
    result["subdomains"] = []
    for sub in subdomains:
        try:
            full = f"{sub}.{domain}"
            ip = socket.gethostbyname(full)
            result["subdomains"].append({"sub": full, "ip": ip})
        except:
            pass

    return result

# ── HEADER ANALYSIS ───────────────────
def analyze_headers(url: str) -> dict:
    try:
        r = requests.head(url, timeout=5, allow_redirects=True)
        headers = dict(r.headers)
        security_headers = {
            "X-Frame-Options": headers.get("X-Frame-Options", "MISSING ⚠"),
            "X-Content-Type-Options": headers.get("X-Content-Type-Options", "MISSING ⚠"),
            "Strict-Transport-Security": headers.get("Strict-Transport-Security", "MISSING ⚠"),
            "Content-Security-Policy": headers.get("Content-Security-Policy", "MISSING ⚠"),
            "Server": headers.get("Server", "Hidden"),
        }
        return security_headers
    except Exception as e:
        return {"error": str(e)}

# Usage:
# info = domain_recon("example.com")
# print(json.dumps(info, indent=2, default=str))'''
        },

        {
            "title": "Exploit Development Basics",
            "tag": "BLACK HAT",
            "tag_color": C["tag_bh"],
            "content": """⚠  CTF / Lab environments ONLY!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Common Vulnerabilities
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  SQL Injection
  ├─ Input validation bypass
  ├─ Database extract
  └─ Prevention: parameterized queries

  XSS (Cross-Site Scripting)
  ├─ Malicious script inject
  ├─ Cookie stealing
  └─ Prevention: output encoding

  Buffer Overflow
  ├─ Memory boundary exceed
  ├─ Code execution
  └─ Prevention: bounds checking

  Command Injection
  ├─ OS commands inject
  ├─ Shell access
  └─ Prevention: subprocess safe args

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  CTF Platforms (Practice!)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  HackTheBox     →  hackthebox.com
  TryHackMe      →  tryhackme.com
  PicoCTF        →  picoctf.org
  OverTheWire    →  overthewire.org
  VulnHub        →  vulnhub.com""",
            "code": (
"# EDUCATIONAL - Vulnerable code examples\n"
"# These show WHAT TO AVOID and how to fix!\n"
"\n"
"import sqlite3, subprocess, html, base64, codecs\n"
"\n"
"# SQL INJECTION (Vulnerable vs Safe)\n"
"# VULNERABLE - Never do this!\n"
"def get_user_bad(username):\n"
"    conn = sqlite3.connect('users.db')\n"
"    # Attacker: username = \"admin' OR 1=1 --\"\n"
"    query = 'SELECT * FROM users WHERE name=' + username\n"
"    return conn.execute(query).fetchall()\n"
"\n"
"# SAFE - Parameterized queries (prevent SQL injection)\n"
"def get_user_safe(username):\n"
"    conn = sqlite3.connect('users.db')\n"
"    query = 'SELECT * FROM users WHERE name = ?'\n"
"    return conn.execute(query, (username,)).fetchall()\n"
"\n"
"# XSS Prevention\n"
"# VULNERABLE\n"
"def render_bad(user_input):\n"
"    return f'<div>{user_input}</div>'\n"
"    # Input: <script>steal_cookies()</script>\n"
"\n"
"# SAFE - Escape output!\n"
"def render_safe(user_input):\n"
"    safe = html.escape(user_input)\n"
"    return f'<div>{safe}</div>'\n"
"\n"
"# COMMAND INJECTION Prevention\n"
"# VULNERABLE\n"
"def ping_bad(host):\n"
"    import os\n"
"    os.system('ping ' + host)  # DANGER!\n"
"    # Input: 8.8.8.8; rm -rf / => DISASTER!\n"
"\n"
"# SAFE - Use list arguments\n"
"def ping_safe(host):\n"
"    import ipaddress\n"
"    ipaddress.ip_address(host)  # validate first\n"
"    result = subprocess.run(\n"
"        ['ping', '-c', '4', host],\n"
"        capture_output=True, text=True, timeout=10\n"
"    )\n"
"    return result.stdout\n"
"\n"
"# CTF TOOLS\n"
"encoded = base64.b64encode(b'Hello CTF!')\n"
"decoded = base64.b64decode(encoded)\n"
"print(decoded)           # b'Hello CTF!'\n"
"\n"
"hex_str = '48656c6c6f'\n"
"print(bytes.fromhex(hex_str).decode())  # Hello\n"
"\n"
"print(codecs.encode('Hello World', 'rot_13'))\n"
"\n"
"def xor_cipher(data: bytes, key: int) -> bytes:\n"
"    return bytes(b ^ key for b in data)\n"
"\n"
"encrypted = xor_cipher(b'Secret!', 0x42)\n"
"decrypted = xor_cipher(encrypted, 0x42)\n"
"print(decrypted)         # b'Secret!'\n"
            ),
        },
    ],
}

# ─────────────────────────────────────────────
#  MAIN APPLICATION
# ─────────────────────────────────────────────
class PythonMasterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🐍 Python Master — Complete Learning Platform")
        self.root.geometry("1280x800")
        self.root.minsize(1100, 700)
        self.root.configure(bg=C["bg_dark"])

        self._setup_fonts()
        self._build_ui()

    # ── FONTS ─────────────────────────────────
    def _setup_fonts(self):
        self.font_title   = ("Segoe UI", 22, "bold")
        self.font_heading = ("Segoe UI", 14, "bold")
        self.font_sub     = ("Segoe UI", 11)
        self.font_body    = ("Segoe UI", 10)
        self.font_code    = ("Consolas", 10)
        self.font_tag     = ("Segoe UI", 8, "bold")
        self.font_nav     = ("Segoe UI", 10, "bold")
        self.font_small   = ("Segoe UI", 8)

    # ── ROOT LAYOUT ───────────────────────────
    def _build_ui(self):
        # Top bar
        self._build_topbar()

        # Main content area
        main = tk.Frame(self.root, bg=C["bg_dark"])
        main.pack(fill="both", expand=True, padx=0, pady=0)

        # Left nav
        self._build_sidebar(main)

        # Right content
        self._build_content(main)

        # Bottom bar
        self._build_bottombar()

        # Default selection
        first_cat = list(CURRICULUM.keys())[0]
        self._select_category(first_cat)

    # ── TOP BAR ───────────────────────────────
    def _build_topbar(self):
        bar = tk.Frame(self.root, bg=C["accent"], height=64)
        bar.pack(fill="x", side="top")
        bar.pack_propagate(False)

        # Logo area
        logo_frame = tk.Frame(bar, bg=C["accent"])
        logo_frame.pack(side="left", padx=20, pady=8)

        tk.Label(logo_frame, text="🐍", font=("Segoe UI", 24),
                 bg=C["accent"], fg=C["white"]).pack(side="left")
        tk.Label(logo_frame, text="Python Master",
                 font=("Segoe UI", 18, "bold"),
                 bg=C["accent"], fg=C["white"]).pack(side="left", padx=8)
        tk.Label(logo_frame, text="Complete Learning Platform",
                 font=("Segoe UI", 9),
                 bg=C["accent"], fg=C["off_white"]).pack(side="left", padx=4)

        # Right info
        right = tk.Frame(bar, bg=C["accent"])
        right.pack(side="right", padx=20)

        stats = f"📚 {sum(len(v) for v in CURRICULUM.values())} Topics  •  4 Levels"
        tk.Label(right, text=stats, font=("Segoe UI", 10),
                 bg=C["accent"], fg=C["off_white"]).pack(side="right")

    # ── SIDEBAR ───────────────────────────────
    def _build_sidebar(self, parent):
        self.sidebar = tk.Frame(parent, bg=C["bg_mid"], width=270)
        self.sidebar.pack(side="left", fill="y")
        self.sidebar.pack_propagate(False)

        # Section label
        tk.Label(self.sidebar, text="CURRICULUM",
                 font=("Segoe UI", 9, "bold"),
                 bg=C["bg_mid"], fg=C["muted"]).pack(anchor="w", padx=16, pady=(16, 4))

        # Category buttons
        self.cat_buttons = {}
        for cat in CURRICULUM:
            self._make_cat_button(cat)

        # Separator
        sep = tk.Frame(self.sidebar, bg=C["accent"], height=1)
        sep.pack(fill="x", padx=16, pady=12)

        # Topic list header
        tk.Label(self.sidebar, text="TOPICS",
                 font=("Segoe UI", 9, "bold"),
                 bg=C["bg_mid"], fg=C["muted"]).pack(anchor="w", padx=16, pady=(0, 4))

        # Topic listbox
        list_frame = tk.Frame(self.sidebar, bg=C["bg_mid"])
        list_frame.pack(fill="both", expand=True, padx=8, pady=(0, 8))

        self.topic_listbox = tk.Listbox(
            list_frame,
            bg=C["bg_card"], fg=C["off_white"],
            font=self.font_body,
            selectbackground=C["accent2"],
            selectforeground=C["white"],
            relief="flat", borderwidth=0,
            activestyle="none",
            highlightthickness=0,
            cursor="hand2"
        )
        self.topic_listbox.pack(side="left", fill="both", expand=True)
        self.topic_listbox.bind("<<ListboxSelect>>", self._on_topic_select)

        sb = ttk.Scrollbar(list_frame, orient="vertical",
                            command=self.topic_listbox.yview)
        sb.pack(side="right", fill="y")
        self.topic_listbox.configure(yscrollcommand=sb.set)

    def _make_cat_button(self, cat):
        btn = tk.Button(
            self.sidebar, text=cat,
            font=self.font_nav,
            bg=C["bg_mid"], fg=C["off_white"],
            activebackground=C["accent"],
            activeforeground=C["white"],
            relief="flat", borderwidth=0,
            anchor="w", padx=16, pady=8,
            cursor="hand2",
            command=lambda c=cat: self._select_category(c)
        )
        btn.pack(fill="x", padx=4, pady=2)
        self.cat_buttons[cat] = btn

    def _select_category(self, cat):
        # Highlight selected
        for c, b in self.cat_buttons.items():
            if c == cat:
                b.configure(bg=C["accent"], fg=C["white"])
            else:
                b.configure(bg=C["bg_mid"], fg=C["off_white"])

        self.current_cat = cat
        topics = CURRICULUM[cat]

        self.topic_listbox.delete(0, "end")
        for i, topic in enumerate(topics):
            self.topic_listbox.insert("end", f"  {i+1:02d}. {topic['title']}")

        if topics:
            self.topic_listbox.selection_set(0)
            self._show_topic(0)

    def _on_topic_select(self, event):
        sel = self.topic_listbox.curselection()
        if sel:
            self._show_topic(sel[0])

    # ── CONTENT AREA ──────────────────────────
    def _build_content(self, parent):
        self.content_frame = tk.Frame(parent, bg=C["bg_dark"])
        self.content_frame.pack(side="left", fill="both", expand=True)

        # Canvas + scrollbar for full scrollability
        self.canvas = tk.Canvas(self.content_frame,
                                bg=C["bg_dark"], highlightthickness=0)
        self.v_scroll = ttk.Scrollbar(self.content_frame, orient="vertical",
                                       command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.v_scroll.set)

        self.v_scroll.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)

        self.inner = tk.Frame(self.canvas, bg=C["bg_dark"])
        self.canvas_window = self.canvas.create_window(
            (0, 0), window=self.inner, anchor="nw"
        )

        self.inner.bind("<Configure>", self._on_frame_configure)
        self.canvas.bind("<Configure>", self._on_canvas_configure)
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

    def _on_frame_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def _on_canvas_configure(self, event):
        self.canvas.itemconfig(self.canvas_window, width=event.width)

    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    # ── SHOW TOPIC ────────────────────────────
    def _show_topic(self, index):
        cat = self.current_cat
        topic = CURRICULUM[cat][index]

        # Clear inner
        for w in self.inner.winfo_children():
            w.destroy()
        self.canvas.yview_moveto(0)

        pad = 28

        # ── TAG badge ─────────────────────────
        tag_row = tk.Frame(self.inner, bg=C["bg_dark"])
        tag_row.pack(anchor="w", padx=pad, pady=(24, 4))

        tag_bg = topic["tag_color"]
        tag_lbl = tk.Label(tag_row, text=f"  {topic['tag']}  ",
                            font=self.font_tag,
                            bg=tag_bg, fg=C["white"],
                            padx=6, pady=3)
        tag_lbl.pack(side="left")

        # Topic count indicator
        cats = CURRICULUM[cat]
        tk.Label(tag_row,
                 text=f"  {index+1} / {len(cats)}",
                 font=self.font_small, bg=C["bg_dark"], fg=C["muted"]
                 ).pack(side="left", padx=8)

        # ── TITLE ─────────────────────────────
        tk.Label(self.inner, text=topic["title"],
                 font=("Segoe UI", 18, "bold"),
                 bg=C["bg_dark"], fg=C["white"],
                 wraplength=800, justify="left"
                 ).pack(anchor="w", padx=pad, pady=(4, 16))

        # ── DIVIDER ───────────────────────────
        tk.Frame(self.inner, bg=C["accent"], height=2).pack(
            fill="x", padx=pad, pady=(0, 16))

        # ── CONTENT CARD ──────────────────────
        content_card = tk.Frame(self.inner, bg=C["bg_card"],
                                bd=0, relief="flat")
        content_card.pack(fill="x", padx=pad, pady=(0, 16))

        tk.Label(content_card,
                 text=" 📖  LESSON CONTENT",
                 font=("Segoe UI", 9, "bold"),
                 bg=C["accent2"], fg=C["white"],
                 anchor="w", padx=12, pady=6
                 ).pack(fill="x")

        tk.Label(content_card,
                 text=topic["content"],
                 font=("Consolas", 10),
                 bg=C["bg_card"], fg=C["off_white"],
                 justify="left", anchor="nw",
                 padx=20, pady=16, wraplength=850
                 ).pack(fill="x", anchor="w")

        # ── CODE CARD ─────────────────────────
        code_card = tk.Frame(self.inner, bg=C["code_bg"],
                             bd=0, relief="flat")
        code_card.pack(fill="x", padx=pad, pady=(0, 16))

        code_header = tk.Frame(code_card, bg="#0D2137")
        code_header.pack(fill="x")

        tk.Label(code_header, text=" 💻  CODE EXAMPLE",
                 font=("Segoe UI", 9, "bold"),
                 bg="#0D2137", fg=C["highlight"],
                 anchor="w", padx=12, pady=6
                 ).pack(side="left", fill="x", expand=True)

        # Copy button
        def copy_code():
            self.root.clipboard_clear()
            self.root.clipboard_append(topic["code"])
            copy_btn.configure(text="✅ Copied!")
            self.root.after(2000, lambda: copy_btn.configure(text="📋 Copy"))

        copy_btn = tk.Button(code_header, text="📋 Copy",
                             font=self.font_tag,
                             bg=C["accent"], fg=C["white"],
                             relief="flat", padx=10, pady=4,
                             cursor="hand2", command=copy_code)
        copy_btn.pack(side="right", padx=8, pady=4)

        code_text = tk.Text(code_card,
                            font=self.font_code,
                            bg=C["code_bg"], fg=C["code_text"],
                            relief="flat", borderwidth=0,
                            padx=20, pady=16,
                            height=self._count_code_lines(topic["code"]),
                            state="normal",
                            wrap="none",
                            insertbackground=C["white"])
        code_text.pack(fill="x")
        code_text.insert("1.0", topic["code"])
        code_text.configure(state="disabled")

        self._syntax_highlight(code_text)

        # Horizontal scroll for code
        h_sb = ttk.Scrollbar(code_card, orient="horizontal",
                             command=code_text.xview)
        h_sb.pack(fill="x")
        code_text.configure(xscrollcommand=h_sb.set)

        # ── NAV BUTTONS ───────────────────────
        nav = tk.Frame(self.inner, bg=C["bg_dark"])
        nav.pack(fill="x", padx=pad, pady=(8, 32))

        if index > 0:
            prev_topic = CURRICULUM[cat][index - 1]["title"]
            tk.Button(nav,
                      text=f"← {prev_topic[:30]}...",
                      font=self.font_body,
                      bg=C["bg_card"], fg=C["off_white"],
                      relief="flat", padx=16, pady=8,
                      cursor="hand2",
                      command=lambda: self._nav_to(index - 1)
                      ).pack(side="left")

        if index < len(CURRICULUM[cat]) - 1:
            next_topic = CURRICULUM[cat][index + 1]["title"]
            tk.Button(nav,
                      text=f"{next_topic[:30]}... →",
                      font=self.font_body,
                      bg=C["accent"], fg=C["white"],
                      relief="flat", padx=16, pady=8,
                      cursor="hand2",
                      command=lambda: self._nav_to(index + 1)
                      ).pack(side="right")

    def _nav_to(self, index):
        self.topic_listbox.selection_clear(0, "end")
        self.topic_listbox.selection_set(index)
        self.topic_listbox.see(index)
        self._show_topic(index)

    def _count_code_lines(self, code: str) -> int:
        lines = code.count("\n") + 1
        return min(max(lines, 8), 40)

    def _syntax_highlight(self, text_widget):
        """Basic syntax highlighting."""
        text_widget.configure(state="normal")

        # Keywords
        keywords = [
            "def ", "class ", "return ", "import ", "from ", "if ",
            "elif ", "else:", "for ", "while ", "try:", "except ",
            "finally:", "with ", "as ", "pass", "break", "continue",
            "lambda ", "yield ", "async ", "await ", "raise ",
            "and ", "or ", "not ", "in ", "is ", "None", "True", "False",
            "global ", "nonlocal ", "del ", "assert ",
        ]

        text_widget.tag_configure("keyword",  foreground="#569CD6")
        text_widget.tag_configure("string",   foreground="#CE9178")
        text_widget.tag_configure("comment",  foreground="#6A9955")
        text_widget.tag_configure("number",   foreground="#B5CEA8")
        text_widget.tag_configure("decorator",foreground="#DCDCAA")
        text_widget.tag_configure("builtin",  foreground="#4EC9B0")

        content = text_widget.get("1.0", "end")
        lines = content.split("\n")

        for line_num, line in enumerate(lines, start=1):
            # Comments
            if "#" in line:
                idx = line.index("#")
                start = f"{line_num}.{idx}"
                end = f"{line_num}.end"
                text_widget.tag_add("comment", start, end)

            # Strings (simplified)
            dq3 = chr(34)*3
            sq3 = chr(39)*3
            dq1 = chr(34)
            sq1 = chr(39)
            for q in [dq3, sq3, dq1, sq1]:
                pos = 0
                while True:
                    start_idx = line.find(q, pos)
                    if start_idx == -1:
                        break
                    end_idx = line.find(q, start_idx + len(q))
                    if end_idx == -1:
                        break
                    s = f"{line_num}.{start_idx}"
                    e = f"{line_num}.{end_idx + len(q)}"
                    text_widget.tag_add("string", s, e)
                    pos = end_idx + len(q)
                    break

            # Keywords
            for kw in keywords:
                pos = 0
                while True:
                    idx = line.find(kw, pos)
                    if idx == -1:
                        break
                    s = f"{line_num}.{idx}"
                    e = f"{line_num}.{idx + len(kw)}"
                    text_widget.tag_add("keyword", s, e)
                    pos = idx + len(kw)

            # Decorators
            stripped = line.lstrip()
            if stripped.startswith("@"):
                col = len(line) - len(stripped)
                end_col = col + len(stripped.split("(")[0].split("\n")[0])
                text_widget.tag_add("decorator",
                                    f"{line_num}.{col}",
                                    f"{line_num}.{end_col}")

        text_widget.configure(state="disabled")

    # ── BOTTOM BAR ────────────────────────────
    def _build_bottombar(self):
        bar = tk.Frame(self.root, bg=C["bg_mid"], height=36)
        bar.pack(fill="x", side="bottom")
        bar.pack_propagate(False)

        dev_text = "Developer: Demiyan Dissanayake  •  📧 dexelsoftwaresolutions@gmail.com  •  🔗 github.com/Dexel-Software-Solutions"
        tk.Label(bar, text=dev_text,
                 font=("Segoe UI", 8),
                 bg=C["bg_mid"], fg=C["muted"]
                 ).pack(side="left", padx=16, pady=8)

        tk.Label(bar, text="© 2026  Dexel Software Solutions",
                 font=("Segoe UI", 8),
                 bg=C["bg_mid"], fg=C["muted"]
                 ).pack(side="right", padx=16)


# ─────────────────────────────────────────────
#  ENTRY POINT
# ─────────────────────────────────────────────
if __name__ == "__main__":
    root = tk.Tk()

    # Style scrollbars
    style = ttk.Style(root)
    style.theme_use("clam")
    style.configure("Vertical.TScrollbar",
                    background=C["bg_card"],
                    troughcolor=C["bg_mid"],
                    bordercolor=C["bg_mid"],
                    arrowcolor=C["muted"],
                    lightcolor=C["bg_card"],
                    darkcolor=C["bg_card"])
    style.configure("Horizontal.TScrollbar",
                    background=C["bg_card"],
                    troughcolor=C["bg_mid"],
                    bordercolor=C["bg_mid"],
                    arrowcolor=C["muted"])

    app = PythonMasterApp(root)
    root.mainloop()
