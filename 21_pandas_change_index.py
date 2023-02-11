#!/usr/bin/env python3

# Python 3.9.5

# 21_pandas_change_index.py

# Dependencies
import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

df = yf.download('SPY', start='2007-01-01', end='2011-12-31')
df.head() # Visualize data: Date is too long for the task at hand
df.index  # Show the index

new_index = [] # Create a new index
date = ""      # Create an empty date variable (type string)

for index in df.index:
    date = index
    date = str(date)
    date = date[0:10]
    new_index.append(date)  # Add value to the new index
    
df.index = new_index        # Exchange old index for new index
df.index                    # Show the new index
