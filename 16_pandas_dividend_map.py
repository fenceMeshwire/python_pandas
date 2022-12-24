#!/usr/bin/env python3

# Python 3.9.5

# 16_pandas_dividend_map.py

# Practical example: Visualize some dividend payments in one year (DATA FOR DEMONSTRATION ONLY).

# Dependency
import pandas as pd

PAYMENT = {
            (1, 0): 0.94, (4, 0): 0.94, (7, 0): 0.94, (10, 0): 0.94,
            (2, 1): 0.27, (5, 1): 0.27, (8, 1): 0.27, (11, 1): 0.27,
            (3, 2): 0.35, (6, 2): 0.35, (9, 2): 0.35, (12, 2): 0.35,
            (3, 3): 0.36, (6, 3): 0.36, (9, 3): 0.36, (12, 3): 0.36,
            (2, 4): 0.51, (5, 4): 0.51, (8, 4): 0.51, (11, 4): 0.51,
          }

IDX = {0:"MO", 1:"T", 2:"GOGL", 3:"ULVR", 4:"C"}

cols = [i for i in range(1, 13)]
rows = [i for i in range(len(IDX))]

df = pd.DataFrame(columns=cols)

def draw_result(col, row):
    try:
        key = (col, row)
        div = PAYMENT[key]
    except KeyError:
        div = "."
    return div

for row in rows:
    values = [draw_result(col, row) for col in cols] # Get values per line
    df.loc[row] = values # Append values for each line to the DataFrame

df = df.rename(index=IDX)
print(df)
