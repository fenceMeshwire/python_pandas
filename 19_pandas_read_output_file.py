#!/usr/bin/env python3

# Python 3.9.5

# 19_pandas_read_output_file.py

# Dependencies
import pandas as pd
import os, platform
from pathlib import Path

if os.name == 'nt' or platform.system() == 'Windows':
    path = 'C:\\Users...'
    os.chdir(path)
if os.name == 'posix' or platform.system() == 'Darwin':
    path = '/Users/...'
    os.chdir(path)

print('Path changed to:', Path.cwd())

# Set number of visible rows:
pd.options.display.max_rows = 10

# Import all:
data_import = pd.read_csv('import.csv')
print(data_import)

# Import number of rows:
data_import = pd.read_csv('import.csv',  nrows=10)
print(data_import)

# Make Series from import:
partial_data = pd.read_csv('import.csv', chunksize=100)
obj = pd.Series([])
for data in partial_data:
    obj = obj.add(data['feature'].value_counts(), fill_value=0)

obj = obj.sort_values(ascending=False)
print(obj)
