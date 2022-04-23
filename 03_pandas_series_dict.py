#!/usr/bin/env python3

# Python 3.9.5

# 03_pandas_series_dict.py

# Dependencies
import pandas as pd
import matplotlib.pyplot as plt

population_2020 = {
'China': 1439323776,
'India': 1380004385,
'United States': 331002651,
'Indonesia': 273523615,
'Pakistan': 220892340
}

population = pd.Series(population_2020)
index = population.index

# Visualization
label = ['Top five population in 2020']
population.plot.bar()
plt.xticks(rotation=0)
plt.legend(label, loc='upper right')
plt.show()
