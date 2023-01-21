#!/usr/bin/env/python3

# Python 3.9.5

# 17_pandas_create_series_from_scratch.py

# In order to create a Series from scratch, e.g. a list has to be provided first.
# data = [1, 2, 3] -> series = pd.Series(data) -> series.plot.bar() -> plt.show()

# Dependency
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import binom

def generate_distribution(n, p):
    data = []
    for i in range(n+1):
        data.append(binom.pmf(i, n, p))

    distribution = pd.Series(data, index=[n for n in range(n+1)])
    return distribution

def create_bar_chart(distribution, n):
    distribution.plot.bar()
    xlabel = f"k results for {n} trials"
    plt.xlabel(xlabel)
    plt.ylabel('p')
    plt.show()

if __name__ == '__main__':
    n = 20
    p = 0.5
    distribution = generate_distribution(n, p)
    create_bar_chart(distribution, n)
