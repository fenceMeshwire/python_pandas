#!/usr/bin/env python3

# Python 3.9.5

# 09_pandas_index_preservation.py

data = np.random.RandomState(31)
pd_series = pd.Series(data.randint(0, 10, 4))
print(pd_series)

# Indices for columns:
data_frame = pd.DataFrame(data.randint(0, 10, (3, 4)), 
    columns=['A', 'B', 'C', 'D'])

print(data_frame)

# Indices for rows and columns:
data_frame = pd.DataFrame(data.randint(0, 10, (3, 4)), 
    columns=['A', 'B', 'C', 'D'], index=['X', 'Y', 'Z'])

print(data_frame)
