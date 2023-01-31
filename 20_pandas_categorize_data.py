#!/usr/bin/env python3

# Python 3.9.5

# 20_pandas_categorize_data.py

# Dependencies
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

sample = [np.random.randint(1, 200) for i in range(100)]
limits = [25, 90, 115, 148, 170]

intervals = pd.cut(sample, limits)

result = pd.value_counts(intervals)
result.plot.bar()

plt.xticks(rotation=0)
plt.show()
