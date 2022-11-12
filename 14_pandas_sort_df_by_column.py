#!/usr/bin/env python3

# Python 3.9.5

# 14_pandas_sort_df_by_column

# Dependencies
import pandas as pd
import os

path = '/path'
os.chdir(path)

df = pd.read_csv('file.csv')

value = "column name"

sorting_result = df.sort_values(by=value, ascending=True) # Descending: ascending=False
print(selection)
