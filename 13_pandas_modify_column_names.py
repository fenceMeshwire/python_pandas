#!/usr/bin/env python3

# Python 3.9.5

# 57_pandas_mod_column_labels.py

# Dependencies
import pandas as pd
import os

path = '/path'
os.chdir(path)

df = pd.read_csv('file.csv')

# All columns get the same prefix and suffix
df = df.add_prefix('prefix___')
df = df.add_suffix('___suffix')

print(df)

# Change column names individually:
columns = list(df.columns)
number_of_columns = len(df.columns)

for column in range(number_of_columns):
    columns[column] = columns[column].strip()
    columns[column] = columns[column] + '_' + str(column)

df.columns = columns

print(df)
