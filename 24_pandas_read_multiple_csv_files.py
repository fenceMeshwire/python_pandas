#!/usr/bin/env/python3

# Python 3.9.5

# 24_pandas_read_multiple_csv_files.py
import os
from pathlib import Path
import pandas as pd
import glob

path = "/Users/user/home/..."
os.chdir(path)
Path.cwd()

files = glob.glob(path + '\*.csv')

dataframes = []
for file in files:
    try:
        dataframes.append(pd.read_csv(file))
    except pd.errors.ParserError as err:
        print("Error on file:", file)
        print("Error message:", err)

# Concatenate all data into one DataFrame
data = pd.concat(dataframes, ignore_index=True)
print(data)
