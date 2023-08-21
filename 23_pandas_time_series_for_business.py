#!/usr/bin/env python3

# Python 3.9.5

# 23_pandas_time_series_for_business.py

# Dependencies
import pandas as pd

pd.period_range('2015-07-03', periods=8, freq='B')  # Returns Business Days
pd.date_range('2023-01-01', periods=12, freq='BM')  # End of Business Month
pd.date_range('2023-01-01', periods=12, freq='BQ')  # End of Business Quarter
pd.date_range('2023-01-01', periods=1, freq='BA')   # End of Business Year
pd.date_range('2023-01-02', periods=8, freq='BH')   # Returns Business Hours
