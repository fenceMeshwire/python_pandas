#!/usr/bin/env python3

# Python 3.9.5

# 01_pandas_series.py

# Dependency
import pandas as pd

# Data
data = pd.Series([1, 2, 3, 4, 5])

# Operations
data          # returns the indexed object dtype: int64
data.values   # array([1, 2, 3, 4, 5], dtype=int64)
data.index    # RangeIndex(start=0, stop=5, step=1
