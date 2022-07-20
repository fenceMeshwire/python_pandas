#!/usr/bin/env python3

# Python 3.9.5

# 12_DataFrame_Scratch_Built.py

# Dependency
import pandas as pd

heading = ["City", "Country Code", "Inhabitants", "Latitude, Longitude"]

df = pd.DataFrame(columns=heading)
df.loc[len(df.index)] = ['Munich', 'DE', 1.472, (48.137154, 11.576124)]
df.loc[len(df.index)] = ['Berlin', 'DE', 3.645, (52.520008, 13.404954)]
df.loc[len(df.index)] = ['Copenhagen', 'DK', 0.602, (55.676098, 12.568337)]

print(df)
