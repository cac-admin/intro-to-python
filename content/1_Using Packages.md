# Using packages

Packages extend the capabilities that Python comes with by default. They simplify complex tasks and make the development process faster.

There are internal and external packages. Internal ones are installed along with python, but we have to import them to be able to use them. External packages are typically installed through pip, Python's package manager. These packages are publicly available on the [PyPI](https://pypi.org/). Replit takes care of installing packages and their dependencies when we run our script, so we don't have to worry about performing `pip install <package-name>` today (which is how we typically install packages).

## 0. Importing packages

[Numpy documentation](https://numpy.org/doc/stable/index.html)

[Pandas documentation](https://pandas.pydata.org/pandas-docs/stable/index.html)

[Matplotlib documentation](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.html#module-matplotlib.pyplot)

[Seaborn documentation](https://seaborn.pydata.org/)


The basic way of importing packages

```python
import numpy
```

But we are lazy, we don't want to type `numpy` every time we want to use one of it's functions. We can give packages an alias

```python
import numpy as np
```

Packages can contain many modules, classes and functions in them. We can specify what we want to import from a package

```python
from numpy import random as nprand

# Or we can use periods to navigate the package's structure
import numpy.random as nprand
```

```python
from matplotlib import pyplot as plt

# Or we can use periods to navigate the package's structure
import matplotlib.pyplot as plt
```

## 1. Working with arrays

We can use Numpy to work with arrays.

```python
import numpy as np

arr1 = np.zeros([8,8], dtype=np.int32)
arr2 = np.zeros([8,8], dtype=np.float32)

print(arr1.dtype)
print(arr2.dtype)
```

Numpy provides all sort of routines to operate on arrays. You can find them [here](https://numpy.org/doc/stable/reference/routines.html).

```python
import numpy as np

arr1 = np.array([[1, 0], [0, 1]])
arr2 = np.array([[4, 1], [2, 2]])

prod = arr1.dot(arr2)

print(prod)
```

And you can save and load arrays

```python
np.save('myarray', arr1)
```

```python
arr2 = np.load('myarray.npy')
```

## 2. Working with tables

It is very common to work with data in the form of tables. We see them in the form of CSVs, Excel spreadsheets, databases, etc.

In Python, we could represent tables in several ways. For example, as a list of lists:

```python
weekly_stock_price = [
  # M, T, W, T, F, S, S
  [32,43,34,36,56,53,54], # week 1
  [33,34,41,42,47,51,54] # week 2
  # ...
]
```

This is not very convenient. Fortunately, external libraries can help us with this task. 

### 2.1 Pandas Dataframe

[Pandas documentation](https://pandas.pydata.org/pandas-docs/stable/index.html)

The Pandas library provides a class, called DataFrame, which not only simplifies working with tables in Python, but it provides some nifty methods.

```python
import pandas as pd

df = pd.DataFrame({
  'mon': [2,4,5,6],
  'tue': [4,2,4,5],
  'wed': [6,3,2,5],
  'thu': [3,5,6,4],
  'fri': [4,6,7,8],
  'sat': [2,4,6,7],
  'sun': [8,5,3,6]
}, index=['w1','w2','w3','w4'])
```

You can get quick information using the `describe` method.

```python
print(df.describe())
```

You can also select by index.

```python
print(df.iloc[2, 1])
print(df.iloc[1:3, :])
```

Or select by column and index name.

```python
print(df.loc['w3', 'wed'])
print(df.loc['w3':'w4', 'fri':'sun'])
```

And we can also use conditionals.

```python
print(df.loc[df['mon']>4, :])
```

## 3. Importing data using Pandas

Using pandas, we can import a variety of data formats to a DataFrame.

```python
df = pd.read_csv('data.csv')
```

This data corresponds to measurements of different iris plants.

![iris measurement](https://miro.medium.com/max/362/1*XN85Vu-SmkJc3TkwgTx5Kw.jpeg)

Using what we have learned, we can analyze the data. Let's identify our classes using `unique`.

```python
df['class'].unique()
```

Now, we can filter the data and use `describe` to get a sense of each class.

```python
classes = df['class'].unique()

for iris in classes:
  class_df = df.loc[ df['class']==iris, : ]
  print(iris)
  print(class_df.describe())
```

## 4. Plotting data

Visualizing data is a useful way of understanding it. This task can be challenging if we try to do it from scratch. Fortunately, there are libraries that make it very simple. One of those libraries is matplotlib.

```python
import matplotlib.pyplot as plt

data = [0,1,2,3,4,7,10,16,15,8,4,7,3,1,0]

plt.plot(data)
plt.show()
```

## 5. Let's put everything together

We learned earlier about pandas. Let's combine it with matplotlib to visualize our iris data.

```python
classes = df['class'].unique()

for iris in classes:
  iris_df = df.loc[df['class']==iris, :]
  x = iris_df['petal_length']
  y = iris_df['petal_width']
  plt.scatter(x, y)

plt.legend(classes)
plt.show()
```

## 6. Taking visualizations a step further

As it has been mentioned earlier, there are packages for everything in Python. In fact, there's one for the exact excercise we're doing. Seaborn is a statistical data visualization package that's meant to be used with pandas DataFrames.

```python
import seaborn as sns
import pandas as pd

df = pd.read_csv('data.csv')

sns.scatterplot(df, x='sepal_length', y='sepal_width', hue='class').figure.savefig('scatterplot.png')
```