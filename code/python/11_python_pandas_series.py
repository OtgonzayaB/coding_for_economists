# Introduction to pandas and numpy
# Pandas is a python library for data manipulation
import pandas as pd
import numpy as np

# Let's look at pd.Series
# A series is a one-dimensional array- like objects

# Let's define our first pd.Series
ps = pd.Series(['a', 1, 2, np.pi])
print(ps)

# Which data type does our pd.Series have?
print(type(ps))

# We can access the values
print(ps.values)

# Access elements of pd.Series by indexing
print(ps[0:2])

# Define custom index
series_1 = pd.Series(
  data = ["Ramen",
         "Apple",
         "Pizza"],
  index = ["Japan",
           "USA",
           "Italy"]
)

# Advanced indexing of pd.Series
# using . loc[]
print(series_1.loc["Japan"])

# Accessing more than one index
print(series_1.loc[["Japan", "USA"]])

# using .iloc[]
series_1.iloc[0]

# Access elements from a range of indexes
print(series_1.loc["Japan": "Italy"])





