#!/usr/bin/env python3

# Python 3.9.5

# 05_pandas_DataFrame.py

# Dependency
import pandas as pd

# Data
area_dict = {'Macau': 30.5, 'Monaco': 2.02, 'Singapore': 719.9, 'Hong Kong': 1106.3, 'Gibraltar': 6.8}
population_dict = {'Macau': 650834, 'Monaco': 37550, 'Singapore': 5612300, 'Hong Kong': 7409800, 'Gibraltar': 33140}

area = pd.Series(area_dict)

population = pd.Series(population_dict)

states =pd.DataFrame({'population': population, 'area': area})

population['Monaco']
population['Macau':'Singapore']

states['area']
