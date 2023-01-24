#!/usr/bin/env python3

# Python 3.9.5

# 18_pandas_write_output_file.py

# Dependencies
import pandas as pd
import numpy as np
import os, platform
from pathlib import Path
import random

if os.name == 'nt' or platform.system() == 'Windows':
    path = 'C:\\Users\\...'
    os.chdir(path)
if os.name == 'posix' or platform.system() == 'Darwin':
    path = '/Users/...'
    os.chdir(path)

print('Path changed to:', Path.cwd())

# Set number of visible rows (3: first, ..., last):
pd.options.display.max_rows = 3

# Define filename:
filename = 'output.csv'

# Generate random data:
rows = 10000
cols = ['start', 'end']
df = pd.DataFrame(np.random.randn(rows, 2), columns=cols)

# Generate random letters
LETTERS = [chr(l) for l in range(65, 91)] # Obtain uppercase letters from ASCII
letter_col = [str(LETTERS[random.randint(0, 25)]) + str(LETTERS[random.randint(0, 25)]) for _ in range(rows)] # Randomize two-letter output
# Add letters to existing DataFrame object:
df['feature'] = letter_col
# Check result:
print(df)

# Rearange columns (optional, if necessary)
cols = df.columns.tolist()
cols = cols[-1:] + cols[:-1]
df = df[cols]
# Check result:
print(df)

# Write DataFrame to csv:
df.to_csv(filename)
