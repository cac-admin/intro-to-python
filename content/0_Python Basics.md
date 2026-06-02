# Python basics
Now that you familiarized yourself with the environment, let's start coding!

## 1. Data types

In Python, we have different data types. Here are some of them

```python
# String - text
"This is a string"

# Integer, float - numbers
88
86.5

# Boolean - logic
True
False
```

> Try it yourself!
> - Use `type()` to get the type of an object. Try `type('hello')`.
> - Is there a difference between `'hello'` and `"hello"`?
> - Does `'Hello"` work?

## 2. Variables

We can store any of the previous types in a variable. This allows us to modify it and use it throughout our script

```python
var1 = 100
var2 = 5
var3 = var1 + var2
```

> Try it yourself!
> - If you redefine `var2` after defining `var3`, will `var3` change?
> - If `var1 = 20` and `var2 = "hey"`, will `var1 - var2` work?
> - Does `var1 = var2 = 50` work? What is the value of each variable?
> - Does `var1, var2 = 100, 50` work? What is the value of each variable?
> - Does `var1 = 100, 50` work? Does `var1, var2 = 50` work? (More on this later when we talk about tuples!)

## 3. Print

So far, the console has allowed us to see the output of every line that we run, this will not be the case when we switch to running code from a file. In that case, we must explicitly "print" the result.

```python
print(var3)

# printing mutiple elements
print("Var 1:", var1)
```

`print` is a function (more about that in a moment), to execute a function we use parenthesis after the function name. If the function requires it, we must also pass 'arguments' to it inside the parenthesis. In this case, whatever we put inside the parenthesis will be printed.

> Try it yourself!
> - When printing multiple objects, how does the `print` function separate them by default? We can change that by passing an optional argument (essentially a setting), try `print("hello", "world", sep="-->")`
> - There is another optional argument, try `print("hello", "world", sep="-->", end="*THE END*")`. What changed?

## 4. Lists

A list is a container. It can hold many objects. To create a list, we use square brakets around comma-separated objects.

```python
list1 = [1,2,"a",'b',True,False]
```

In order to access the objects, we use their index, which is a number that corresponds to the location of the object in the list. The index starts from 0.

We saw that functions (like `print`) use parenthesis at the end to be executed, to index objects we use square brakets.

```python
# get the item with index 2 (in python we count from 0)
list1[2]

# get a range of values [from:to]
list1[2:5]

# a range with a step different to 1 [from:to:step]
list1[2:5:2]
```

> Try it yourself!
> - What happens when you try `list1[:]`? What do you think the index of the 'from' is assigned to? What do you think the index of the 'to' is assigned to?
> - Can lists contain other lists? Try `list1 = [1,['a','b'],3]`. How would you access an object inside the list inside the list? Try `list1[1][0]`.

## 5. Dictionaries

Soon you will learn that we can modify lists. Doing so can change the indexes of objects and make it confusing to access the object we are interested in. What if we gave each object a unique 'ID' which doesn't change? That can be done with a dictionary.

A dictionary is similar to a list, but instead of using an index, we use a key. To distinguish a dictionary from a list, we use curly brakets. Additionally, when we created lists, the indexes were assigned implicitly from the order of the objects, now we must be explicit.

```python
dict1 = {
  'name': 'Mike', # 'key':value
  'age': 27,
}
```

Similar to lists, we access the values using square brakets. But this time we place the key inside.

```python
dict1['name']

dict1["age"]
```

> Try it yourself!
> - Can you store a list within a dictionary? Try `dict1 = {'list1':[1,2,3]}`. How do you access an object inside the list? Try `dict1['list1'][1]`.
> - Can you store dictionaries inside lists?
> - So far, we used strings as our keys. Can we use integers? Try `dict1 = {0:'hey'}`. What about using a boolean?

## 6. Functions

We breafly mentioned functions when we talked about the `print` function and its arguments, now we will not only use them but also create them.

A function is typically used to summarize a series of steps in a compact form. To define a function, we use `def`, we give our function a name, we add parenthesis, a colon, and we place the code that we want to execute inside it. The code inside the function must be indented (I recommend that you use a tab).

```python
def function_name():
  # do something
```

For example:

```python
def say_hello():
  print("Hello!")
```

Sometimes, we want the function to return something back instead of just printing it to the console. For that we can use `return` at the end of our function!

```python
def get_a_1():
  return 1
```

Now we can save the returned value to a variable.

```python
var1 = get_a_1()
```

Sometimes, we need functions to be more flexible and to not do the exact same thing every time. We use arguments for this.

Arguments are placeholders, variables, and we give them values when executing the function. We define these arguments inside the parenthesis.

```python
def sum_vars(a, b):
  result = a + b
  return result

sum_vars(5,10)

# alternative syntax, this time being explicit about the parameters
sum_vars(
  a=5,
  b=10
)
```

It is important to note that the 3 variables inside the function (`result`, `a`, and `b`) were defined inside the function. This means that those variables belong to the function and can't be accessed outside of the function.

```python
def func():
  result = "I belong inside the function"

func()

print(result)
```

The variables outside of functions, global variables, can be accessed inside a function.

```python
outside = "I'm a global variable"

def func():
  print(outside)

func()
```

Finally, it can get annoying to provide every single argument every time. We can use defaults for arguments which are not required, we call these *optional arguments*.

```python
def sum_vars(a, b=10):
  result = a + b
  return result

sum_vars(5)
```

> Try it yourself!
> - Create a function using arguments and return. You can try:
> ```python
> def add_excitement(word, excl="!!!"):
>   result = word + excl
>   return result
> ```
> - What happens if you try to return more than 1 value? Try replacing `return result` with `return result, word, excl`.
> - Can you reassign a global variable inside a function? Try:
> ```python
> result = "Answer"
>
> def func():
>   result = "Answer has changed"
>
> func()
>
> print(result)
> ```

## 7. Classes

In some situations, variables and functions are not enough. Let's say we want to create a phonebook. We need a place to store all the contacts (a list) and ways to add, modify and delete contacts (functions).

```python
phonebook = []

def add_contact(full_name, phone_number):
  phonebook.append(
    {
      'name': full_name,
      'number': phone_number
    }
  )

add_contact("Mom", 89776923)
print(phonebook)
```

This is simple for a single phonebook, but if we want to have many phonebooks we need more variables and functions. Why not creating a 'template' for a phonebook and creating a phonebook from that template every time we need one? That is what a class can help us do.

```python
class PhoneBook:
  def __init__(self): # Special method which is executed only once
    self.contacts = []
  
  def add_contact(self, full_name, phone_number):
    self.contacts.append(
      {
        'name': full_name,
        'number': phone_number
      }
    )

personal = PhoneBook()
personal.add_contact("Mom", 89776923)
print(personal.contacts)
```

> Try it yourself!
> - Create several phonebooks
> - Try storing several phonebooks in a dictionary
> ```python
> pb = {
>   "personal": PhoneBook(),
>   "business": PhoneBook()
> }
> ```
> - What happens when you print an instance of a phonebook? Does it look something like this: `<__main__.PhoneBook object at 0x7f0cead56c10>`? You can change that. Add the `__str__` special method:
> ```python
> class PhoneBook:
> # ...
>   def __str__(self):
>     return "I'm a phonebook!"
> ```

## 8. List, tuples, and dictionary methods 

Classes are so cool that, without noticing it, we have been working with classes. Integers, strings, dictionaries, lists, etc are classes. Which means that they have methods to modify them and do cool things with them. Here are a couple of methods for lists:

```python
# define the list
l = [1,2,3,4,5]

# add a single element at the very end
l.append(6)

# add many elements at the end
l.extend([7,8,9,10])

# remove (and return) an element
l.pop(5)

# insert an element at a specific location
l.insert(5, 6)

# to replace an object
l[0] = 100
```

You can check out all the methods by running:
```python
help(list)
```

I think this is a good point to introduce tuples. Tuples contain objects that are indexed, just like lists, but tuples can't be modified. For these reason, they only have 2 methods: `count` and `index`. Because they are immutable, we know how many objects will be contained in a tuple. This allows us to unpack those object like this:

```python
def divide(a, b):
  quotient = a // b # '//' is the floor division operator
  remainder = a % b # '%' is the modulo operator
  return quotient, remainder

quot, rem = divide(10,3)

print(quot, rem)
```

And here are a couple of methods for dictionaries:

```python
# define a dictionary
d = {
  "key": "value",
  "name": "Fernando"
}

# get an iterable containing the keys
d.keys()

# get an iterable containing the values
d.values()

# get an iterable containing (key, value) tuples
d.items()

# remove a key
d.pop('key')

# add a key
d['new_key'] = "new value"
```

> Try it yourself!
> - Use the methods above to familiarize yourself with how you can modify lists and dictionaries
> - I mentioned that strings also have methods, but instead of modifying the original string, they return a new string (or a different object depending on the method). You can assign the returned string to a new variable or replace the original one. Try:
> ```python
> var1 = "hey there friend"
> var1 = var1.split(" ")
> print(var1)
> ```

## 9. Logic

Logic is how we make decisions. We make decisions based on whether something is `True` or `False`. Let's start by understanding what is and what isn't true

```python
1 == 1
1 == "1"
10 > 5
50 <= 4
[1,2,3] == [1,2,3]
[1,2,3] == [3,2,1]
0<5<10
True != True
not True
True and True
(True and True) or (False or False)
True and ((True or False) or False)
```

And now we can implement them in `if` statements

```python
# a simple if
if 10 < 100:
  print("True!")

# an if-else
if 20 < 10:
  print("True!")
else:
  print("False!")

# an if-elif-else
i = 0
if i > 0:
  print("Positive!")
elif i < 0:
  print("Negative!")
else:
  print("It's zero!")
```

> Try it yourself!
> Create if-elif-else statements and try different conditions.

## 10. Loops

We already know how to access items in a list. Let's say we want to print every item. We could try:

```python
letters = ["a","b","c","d"]
print(letters[0])
print(letters[1])
print(letters[2])
print(letters[3])
```

Not very efficient. We can do better.

### 10.1 For-loops

A for loop allows us to iterate over an iterable.

```python
for i in [0,1,2,3]:
  print(letters[i])
```

We can still do better. The indexes have been hard-coded, we want them to be dynamic. Check out this function which might help us

```python
print( list(range(4)) )

# we can start at a different integer
print( list(range(5,10)) )

# we can change the step
print( list(range(10,101,10)) )
```

Let's use `range`!

```python
for i in range(4):
  print(letters[i])
```

Much better, but the `4` is still hard-coded. We can use `len` to get the length of our list.

```python
for i in range(len(letters)):
  print(letters[i])
```

This is a very popular for-loop, it allows you to know the index of the elements. But there are other ways of creating a loop.

Check out this elegant for-loop

```python
for letter in letters:
  print(letter)
```

We don't know the index anymore, but that might not be an issue. If we want to have the best of both worlds, we can use `enumerate`

```python
print( list(enumerate(letters)) )
```

`enumerate` provides a list of tuples.  We can unpack the tuples in the following manner:

```python
for i, letter in enumerate(letters):
  print(i, letter)
```

> Try it yourself!
> - Create a list of objets, iterate over them and print them
> - Can we iterate over a tuple? Try `for obj in (1,2,3,4):`

### 10.2 While-loops

When we don't know how many times we want to do something, we may want to use a while loop.

```python
while True:
  print("Still running...")
```

Forever is not great sometimes, let's apply more logic.

```python
num = 0
while num < 1000:
  num += 1 # fancy way of writing 'num = num + 1'
print( num )
```

> Try it yourself!
> - Create a while loop that doesn't run forever!

### 10.3 Break and continue

Sometimes we want to break out of a loop if something happens (e.g. something went wrong!)

```python
for i in range(10):
  if i == 5:
    break
print("Loop exited at iteration", i)
```

Other times we may want to skip the current iteration

```python
for i in range(10):
  if i == 5:
    continue
  print(i)
```

> Try it yourself!
> - Create a list of integers. Add a string somewhere in the middle of the list. Iterate over the objects and print only the integers by skipping strings using `continue`. Hints:
>   - Use `type()` to get the type of an object
>   - Use `str` in the comparison

## 11. More functions

What we have learned so far can take us far, but there are some useful functions that are worth talking about.

### 11.1 Lambda functions

They allow us to simplify a function like:

```python
def f(x):
  y = (x**x)/x
  return y

print( f(4) )
```

And make it a one-line elegant function.

```python
f = lambda x: (x**x)/x

print( f(4) )
```

### 11.2 Map

Let's say we have the following list:

```python
l = [1,2,3,4,5,6,7,8,9,10]
```

And our goal is to apply a certain tranformation to all items in that list, like squaring them! We can do this with a loop.

```python
l_squared = []
for num in l:
    l_squared.append(num**2)
print(l_squared)
```

Or we can use map!

```python
def transf(x):
  return x**2

l_squared = map(transf, l)

print(list(l_squared))
```

And now let's make it more elegant with a lambda function!

```python
l_squared = map(lambda x: x**2, l)

print(list(l_squared))
```

> Other useful functions are `filter` and `sorted`. They work similar to `map`.

> Try it yourself!
> - Use map to multiply all integers in a list by 100.