#!/usr/bin/env python3

# Python 3.9.5

# 02_pandas_series_index.py

# Dependencies
import pandas as pd
import matplotlib.pyplot as plt

data = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
data

data = pd.Series([1, 2, 3, 4], index=[2, 3, 5, 7])
data

data.plot()
plt.show()
