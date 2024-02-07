#!/usr/bin/env python3

# Python 3.9.5

# 25_pandas_concat_values_related_to_keys.py

import os
import pandas as pd

path = r'C:\Users\...\'
os.chdir(path)

df = pd.read_csv('input.csv')
df.head() # Check input

df_concat = df.groupby(['keys'])['values'].apply(lambda x: ','.join(x)).reset_index()
df_concat.head() # Check concatenated values

df_concat.to_csv('output.csv', sep=',', encoding='utf-8', index=False)
