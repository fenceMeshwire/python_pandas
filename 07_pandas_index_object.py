#!/usr/bin/env python3

# Python 3.9.5

# 07_pandas_index_object.py

# Dependency
import pandas as pd

# Data
index = pd.Index([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print(index)

# [start:stop:step]
print(index[1])        # Get the second element
print(index[::3])      # Get every third element

indexA = pd.Index([1, 2, 3, 5, 8, 15, 29])
indexB = pd.Index([2, 3, 5, 6, 10, 17, 30])

indexA.__and__(indexB) # Intersection

indexA.__or__(indexB)  # Union

indexA.__xor__(indexB) # Symmetric Difference
