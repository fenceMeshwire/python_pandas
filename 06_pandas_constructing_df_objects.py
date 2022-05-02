#!/usr/bin/env python3

# Python 3.9.5

# 06_pandas_constructing_df_objects.py

# Dependencies
import pandas as pd
import matplotlib.pyplot as plt

# Constructing a dataframe objects
# Data
area_dict = {'Berlin': 891, 'Hamburg': 755, 'Munich': 310, 'Cologne': 405, 'Frankfurt': 248}
population_dict = {'Berlin': 3664088, 'Hamburg': 1852478, 'Munich': 1488202, 'Cologne': 1083498, 'Frankfurt': 764104}
area = pd.Series(area_dict)
population = pd.Series(population_dict)

# Create a DataFrame object - from one Series object
fig = pd.DataFrame(population, columns=['population'])

# Plot and visualize DataFrame (optional)
fig.plot() 
plt.show()

# Create a DataFrame object - from multiple Series objects
pd.DataFrame({'population': population, 'area': area})
