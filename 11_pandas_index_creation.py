#!/usr/bin/env python3

# Python 3.9.5

# 11_pandas_index_creation.py

# Result: DataFrame with index name and column named 'values' 
# 
#          values
# symbols
# (            40
# <            60
# R            82
# ¦           166
# ¥           165
# ¤           164

# Dependency
import pandas as pd

# Data
symbols = []
numbers = [40, 60, 82, 166, 165, 164]
symbols_list = [chr(number) for number in numbers]

# Arrange the symbols as index and numbers as values in a DataFrame:
data = pd.DataFrame(numbers, index=symbols_list, columns=['values'])
data.index.names = ['symbols']
print(data)
