#!/usr/bin/env python3

# Python 3.9.5

# 04_pandas_construct_series.py

# Dependencies
import pandas as pd
import matplotlib.pyplot as plt

data = pd.Series({25:'Product A', 13:'Product B', 36:'Product C'})
index = data.index
values = data.values

label = ['Pandas Series Visualization']
plt.bar(values, index) # Switching: key, value = value, key
plt.legend(label, loc='upper left')
plt.show()
