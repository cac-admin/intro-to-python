# Python basics

Now that you have familiarized yourself with the environment, let's start coding!

**How to use this notebook**
- Run a cell with **Shift+Enter** (runs and moves to the next cell) or **Ctrl+Enter** (runs and stays).
- Edit any code cell and re-run it to experiment.
- Cells run top to bottom — later cells may use variables from earlier ones.
- Exercises are marked **Try it yourself!** — use the code cell below each one.


```python
print("Hello! Ready to code in Python.")
```

## 1. Data types

In Python, we have different data types. Here are some of them:


```python
# String - text
print("This is a string")

# Integer, float - numbers
print(88)
print(86.5)

# Boolean - logic
print(True)
print(False)
```

**Try it yourself!**
- Use `type()` to get the type of an object. Try `type('hello')`.
- Is there a difference between `'hello'` and `"hello"`?
- Does `'Hello"'` work?


```python

```

## 2. Variables

We can store any of the previous types in a variable. This allows us to modify it and use it throughout our code.


```python
var1 = 100
var2 = 5
var3 = var1 + var2
var3
```

**Try it yourself!**
- If you redefine `var2` after defining `var3`, will `var3` change?
- If `var1 = 20` and `var2 = "hey"`, will `var1 - var2` work?
- Does `var1 = var2 = 50` work? What is the value of each variable?
- Does `var1, var2 = 100, 50` work? What is the value of each variable?
- Does `var1 = 100, 50` work? Does `var1, var2 = 50` work? (More on this later when we talk about tuples!)


```python

```

## 3. Print

In a notebook, the **last expression** in a cell is displayed automatically. When you run code from a `.py` file, you must explicitly print results instead.

Use `print()` when you want to show multiple values or output from inside a function.


```python
print(var3)

# printing multiple elements
print("Var 1:", var1)
```

`print` is a function. To call it, use parentheses after the name and pass whatever you want displayed inside them.

**Try it yourself!**
- When printing multiple objects, how does `print` separate them by default? Try `print("hello", "world", sep="-->")`
- There is another optional argument: try `print("hello", "world", sep="-->", end="*THE END*")`. What changed?


```python

```

## 4. Lists

A list is a container that holds many objects. Create one with square brackets around comma-separated values.


```python
list1 = [1, 2, "a", "b", True, False]
```

To access objects, use their **index** (starting at 0). Functions use parentheses; indexing uses square brackets.


```python
# get the item with index 2 (in Python we count from 0)
print(list1[2])

# get a range of values [from:to]
print(list1[2:5])

# a range with a step different to 1 [from:to:step]
print(list1[2:5:2])
```

**Try it yourself!**
- What happens when you try `list1[:]`? What do you think the index of the 'from' is assigned to? What about 'to'?
- Can lists contain other lists? Try `list1 = [1, ['a', 'b'], 3]`. How would you access an object inside the inner list? Try `list1[1][0]`.


```python

```

## 5. Dictionaries

Lists use numeric indexes that can shift when you modify them. A **dictionary** maps unique **keys** to values using curly braces.


```python
dict1 = {
    "name": "Mike",  # 'key': value
    "age": 27,
}
dict1
```

Access values with square brackets, using the key instead of an index.


```python
print(dict1["name"])
print(dict1["age"])
```

**Try it yourself!**
- Can you store a list within a dictionary? Try `dict1 = {"list1": [1, 2, 3]}`. How do you access an object inside the list? Try `dict1["list1"][1]`.
- Can you store dictionaries inside lists?
- So far we used strings as keys. Can we use integers? Try `dict1 = {0: "hey"}`. What about booleans?


```python

```

## 6. Functions

We briefly mentioned functions with `print`. Now we will create our own.

A function summarizes steps in a compact form. Define one with `def`, a name, parentheses, a colon, and indented code inside.


```python
def say_hello():
    print("Hello!")

say_hello()
```

Use `return` to send a value back instead of only printing it.


```python
def get_a_1():
    return 1

var1 = get_a_1()
var1
```

**Arguments** let a function accept different inputs each time.


```python
def sum_vars(a, b):
    result = a + b
    return result

print(sum_vars(5, 10))

# alternative syntax - explicit parameter names
print(sum_vars(a=5, b=10))
```

Variables defined inside a function are **local** — they cannot be accessed outside it.


```python
def func():
    result = "I belong inside the function"
    return result

func()
# print(result)  # Uncomment to see the NameError
```

**Global** variables (defined outside functions) can be read inside a function.


```python
outside = "I'm a global variable"

def func():
    print(outside)

func()
```

**Optional arguments** have default values so you do not have to pass them every time.


```python
def sum_vars(a, b=10):
    result = a + b
    return result

sum_vars(5)
```

**Try it yourself!**
- Create a function with arguments and a return value:
  ```python
  def add_excitement(word, excl="!!!"):
      return word + excl
  ```
- What happens if you return more than one value? Try `return result, word, excl`.
- Can you reassign a global variable inside a function? Try defining `result = "Answer"`, then a function that sets `result = "Answer has changed"` inside it. What does `print(result)` show after calling the function?


```python

```

## 7. Classes

Sometimes variables and functions alone are not enough. Imagine building a phonebook — you need storage and operations together.


```python
phonebook = []

def add_contact(full_name, phone_number):
    phonebook.append({"name": full_name, "number": phone_number})

add_contact("Mom", 89776923)
print(phonebook)
```

For many phonebooks, a **class** acts as a template you instantiate each time you need one.


```python
class PhoneBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, full_name, phone_number):
        self.contacts.append({"name": full_name, "number": phone_number})

personal = PhoneBook()
personal.add_contact("Mom", 89776923)
personal.contacts
```

**Try it yourself!**
- Create several phonebooks.
- Store them in a dictionary: `pb = {"personal": PhoneBook(), "business": PhoneBook()}`
- What happens when you `print(personal)`? Add a `__str__` method that returns `"I'm a phonebook!"` to customize the display.


```python

```

## 8. Lists, tuples, and dictionary methods

Integers, strings, lists, and dicts are all classes with built-in **methods**. Here are common list methods:


```python
l = [1, 2, 3, 4, 5]

l.append(6)              # add one element at the end
l.extend([7, 8, 9, 10])  # add many elements
l.pop(5)                 # remove and return an element
l.insert(5, 6)           # insert at a specific index
l[0] = 100               # replace an element
l
```

Run `help(list)` to see all list methods.


```python
help(list)
```

**Tuples** are like lists but immutable. Returning multiple values from a function creates a tuple you can unpack:


```python
def divide(a, b):
    quotient = a // b   # floor division
    remainder = a % b   # modulo
    return quotient, remainder

quot, rem = divide(10, 3)
print(quot, rem)
```

Common dictionary methods:


```python
d = {"key": "value", "name": "Fernando"}

print(list(d.keys()))
print(list(d.values()))
print(list(d.items()))

d.pop("key")
d["new_key"] = "new value"
d
```

**Try it yourself!**
- Practice the list and dictionary methods above.
- Strings also have methods, but they return new strings instead of modifying in place. Try:
  ```python
  var1 = "hey there friend"
  var1 = var1.split(" ")
  print(var1)
  ```


```python

```

## 9. Logic

Decisions depend on whether something is `True` or `False`.


```python
print(1 == 1)
print(1 == "1")
print(10 > 5)
print(50 <= 4)
print([1, 2, 3] == [1, 2, 3])
print([1, 2, 3] == [3, 2, 1])
print(0 < 5 < 10)
print(not True)
print(True and True)
print((True and True) or (False or False))
```

Use `if`, `elif`, and `else` to act on conditions:


```python
# simple if
if 10 < 100:
    print("True!")

# if-else
if 20 < 10:
    print("True!")
else:
    print("False!")

# if-elif-else
i = 0
if i > 0:
    print("Positive!")
elif i < 0:
    print("Negative!")
else:
    print("It's zero!")
```

**Try it yourself!** Create if-elif-else statements and try different conditions.


```python

```

## 10. Loops

To print every item in a list, indexing each position manually is tedious:


```python
letters = ["a", "b", "c", "d"]
print(letters[0])
print(letters[1])
print(letters[2])
print(letters[3])
```

### 10.1 For-loops

A **for** loop iterates over an iterable.


```python
for i in [0, 1, 2, 3]:
    print(letters[i])
```

`range()` generates a sequence of numbers:


```python
print(list(range(4)))
print(list(range(5, 10)))
print(list(range(10, 101, 10)))
```


```python
for i in range(4):
    print(letters[i])
```

Use `len()` so the loop adapts to any list length:


```python
for i in range(len(letters)):
    print(letters[i])
```

You can iterate directly over values:


```python
for letter in letters:
    print(letter)
```

`enumerate()` gives both index and value:


```python
print(list(enumerate(letters)))

for i, letter in enumerate(letters):
    print(i, letter)
```

**Try it yourself!**
- Create a list of objects, iterate over them, and print them.
- Can we iterate over a tuple? Try `for obj in (1, 2, 3, 4):`


```python

```

### 10.2 While-loops

Use a **while** loop when you do not know how many iterations you need.


```python
# Careful - this runs forever! Uncomment to try:
# while True:
#     print("Still running...")
```


```python
num = 0
while num < 1000:
    num += 1  # same as num = num + 1
num
```

**Try it yourself!** Create a while loop that stops before running forever.


```python

```

### 10.3 Break and continue

`break` exits a loop early; `continue` skips to the next iteration.


```python
for i in range(10):
    if i == 5:
        break
print("Loop exited at iteration", i)
```


```python
for i in range(10):
    if i == 5:
        continue
    print(i)
```

**Try it yourself!**
Create a list of integers with a string in the middle. Iterate and print only the integers, skipping strings with `continue`. Hints: use `type()` and compare to `str`.


```python

```

## 11. More functions

### 11.1 Lambda functions

Turn a multi-line function into a one-liner:


```python
def f(x):
    return (x ** x) / x

print(f(4))

f = lambda x: (x ** x) / x
print(f(4))
```

### 11.2 Map

Apply a transformation to every item in a list.


```python
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```


```python
# with a loop
l_squared = []
for num in l:
    l_squared.append(num ** 2)
print(l_squared)
```


```python
# with map
l_squared = map(lambda x: x ** 2, l)
print(list(l_squared))
```

Other useful functions: `filter` and `sorted` work similarly to `map`.

**Try it yourself!** Use `map` to multiply all integers in a list by 100.


```python

```
