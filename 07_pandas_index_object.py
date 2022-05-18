#!/usr/bin/env python3

# Python 3.9.5

# 07_pandas_index_object.py

# Dependency
import pandas as pd

# Data
index = pd.Index([1, 2, 3, 4, 5, 6, 7])
index

# [start:stop:step]
index[1]        # Get the second element
index[::2]      # Get every second element

indexA = pd.Index([1, 2, 3, 5, 8])
indexB = pd.Index([2, 3, 5, 6, 10])

indexA & indexB # Intersection

indexA | indexB # Union

indexA ^ indexB # Symmetric Difference
