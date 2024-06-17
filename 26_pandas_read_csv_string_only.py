#!/usr/bin/env python3

# Python 3.11

# 26_pandas_read_csv_string_only.py

# Dependencies
import pandas as pd
import os

path = "/Users/user/..."
os.chdir(path)

data = pd.read_csv('data.csv', dtype='str')
data.head()
