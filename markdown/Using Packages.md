# Using packages

Packages extend the capabilities that Python comes with by default. They simplify complex tasks and make development faster.

**How to use this notebook**
- Run a cell with **Shift+Enter** (runs and moves to the next cell) or **Ctrl+Enter** (runs and stays).
- Cells run top to bottom - later cells may use variables from earlier ones.
- Plots appear inline below the cell that creates them.

There are **internal** packages (installed with Python, but still imported before use) and **external** packages (installed separately). External packages are published on [PyPI](https://pypi.org/). In this workshop, dependencies are listed in `pyproject.toml` and installed with `uv sync`.


```python
print("Ready to explore Python packages.")
```

## 0. Importing packages

Useful documentation:
- [NumPy](https://numpy.org/doc/stable/index.html)
- [Pandas](https://pandas.pydata.org/pandas-docs/stable/index.html)
- [Matplotlib](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.html#module-matplotlib.pyplot)
- [Seaborn](https://seaborn.pydata.org/)

The basic way to import a package:


```python
import numpy
```

We often give packages a shorter **alias** so we do not have to type the full name every time:


```python
import numpy as np
```

Packages contain modules, classes, and functions. You can import only what you need:


```python
from numpy import random as nprand

# Or navigate the package structure with dots
import numpy.random as nprand
```


```python
from matplotlib import pyplot as plt

# Or
import matplotlib.pyplot as plt
```

## 1. Working with arrays

NumPy is the standard library for numerical arrays.


```python
import numpy as np

arr1 = np.zeros([8, 8], dtype=np.int32)
arr2 = np.zeros([8, 8], dtype=np.float32)

print(arr1.dtype)
print(arr2.dtype)
```

NumPy provides routines for creating, transforming, and combining arrays. See the [full reference](https://numpy.org/doc/stable/reference/routines.html).


```python
arr1 = np.array([[1, 0], [0, 1]])
arr2 = np.array([[4, 1], [2, 2]])

prod = arr1.dot(arr2)
print(prod)
```

Arrays can be saved to disk and loaded back:


```python
np.save('myarray', arr1)
```


```python
loaded = np.load('myarray.npy')
print(loaded)
```

## 2. Working with tables

Tabular data shows up as CSVs, spreadsheets, databases, and more. A plain list of lists works, but it is awkward:


```python
weekly_stock_price = [
    # M, T, W, T, F, S, S
    [32, 43, 34, 36, 56, 53, 54],  # week 1
    [33, 34, 41, 42, 47, 51, 54],  # week 2
    # ...
]
```

### 2.1 Pandas DataFrame

[Pandas](https://pandas.pydata.org/pandas-docs/stable/index.html) provides the `DataFrame` class -  a table-like structure with powerful methods for selection and analysis.


```python
import pandas as pd

df = pd.DataFrame(
    {
        "mon": [2, 4, 5, 6],
        "tue": [4, 2, 4, 5],
        "wed": [6, 3, 2, 5],
        "thu": [3, 5, 6, 4],
        "fri": [4, 6, 7, 8],
        "sat": [2, 4, 6, 7],
        "sun": [8, 5, 3, 6],
    },
    index=["w1", "w2", "w3", "w4"],
)
df
```

Get quick summary statistics with `describe`:


```python
df.describe()
```

Select by **integer position** with `iloc`:


```python
print(df.iloc[2, 1])
df.iloc[1:3, :]
```

Select by **row/column labels** with `loc`:


```python
print(df.loc["w3", "wed"])
df.loc["w3":"w4", "fri":"sun"]
```

Filter rows with a condition:


```python
df.loc[df["mon"] > 4, :]
```

## 3. Importing data using Pandas

Pandas can read many file formats into a DataFrame. We can download a dataset from kaggle and open it with Pandas.


```python
import kagglehub
import os

data = kagglehub.dataset_download("uciml/iris")
print("Data downloaded to", data)

df = pd.read_csv(os.path.join(data,"Iris.csv"), index_col="Id")
df.head()
```

The Iris dataset includes iris species with sepal and petal measurements. You can learn more about it at [kaggle](https://www.kaggle.com/datasets/uciml/iris/data).

![iris measurement](https://miro.medium.com/max/362/1*XN85Vu-SmkJc3TkwgTx5Kw.jpeg)

Let's find the distinct iris species:


```python
df["Species"].unique()
```

Filter by species and describe them:


```python
classes = df["Species"].unique()

for iris in classes:
    class_df = df.loc[df["Species"] == iris, :]
    print(iris)
    print(class_df.describe())
    print()
```

## 4. Plotting data

Visualizing data helps you understand it. Matplotlib makes plotting straightforward -  in a notebook, figures appear inline below the cell.


```python
import matplotlib.pyplot as plt

data = [0, 1, 2, 3, 4, 7, 10, 16, 15, 8, 4, 7, 3, 1, 0]

plt.plot(data)
```

## 5. Let's put everything together

Combine Pandas and Matplotlib to visualize the iris dataset:


```python
classes = df["Species"].unique()

for iris in classes:
    iris_df = df.loc[df["Species"] == iris, :]
    x = iris_df["SepalLengthCm"]
    y = iris_df["SepalWidthCm"]
    plt.scatter(x, y, label=iris)

plt.legend()
plt.xlabel("SepalLengthCm")
plt.ylabel("SepalWidthCm")
```

## 6. Taking visualizations a step further

[Seaborn](https://seaborn.pydata.org/) builds on Matplotlib and integrates well with Pandas DataFrames. We can create the plot above with a single function call:


```python
import seaborn as sns

sns.scatterplot(data=df, x="PetalLengthCm", y="PetalWidthCm", hue="Species")
```
