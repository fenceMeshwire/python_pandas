#!/usr/bin/env python3

# Python 3.9.5

# 10_pandas_df_align_index.py

# Dependency
import pandas as pd
import numpy as np

data = np.random.RandomState(15)      # Generate a seed of same results.
matrix_A = pd.DataFrame(data.randint(0, 50, (2, 2)), columns=['n1', 'n2'], index=['m1', 'm2'])
print(matrix_A)

matrix_B = pd.DataFrame(data.randint(0, 30, (3, 3)), columns=['n1', 'n2', 'n3'], index=['m1', 'm2', 'm3'])
print(matrix_B)

mean_value = matrix_A.stack().mean()

matrix_C = matrix_A.add(matrix_B, fill_value=mean_value)
print(matrix_C)

matrix_D = matrix_B.add(matrix_A, fill_value=mean_value)
print(matrix_D)

print(matrix_C == matrix_D) # Returns True

# Instead of "add" other operations are also possible:
# sub, mul, div, mod, floordiv, pow
