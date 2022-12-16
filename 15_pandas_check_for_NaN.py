#!/usr/bin/env python3

# Python 3.9.5

# 15_pandas_check_for_NaN.py

# Dependencies
import pandas as pd
import os, platform
from pathlib import Path

if os.name == 'nt' or platform.system() == 'Windows':
    path = 'C:\\...'
    os.chdir(path)
if os.name == 'posix' or platform.system() == 'Darwin':
    path = '/Users/...'
    os.chdir(path)

print('Path changed to:', Path.cwd())

df = pd.read_csv('file.csv')
df.head() # Check the first five rows
df.info() # Check the DataFrame information

# Check for missing data.
df.isnull().values.any() # Returns True if data is missing, or NaN.

# Identify the number of missing data elements:
for col_name in df.columns.values:
    value = df[col_name].isna().sum()
    if value > 0:
        print(col_name, value)
