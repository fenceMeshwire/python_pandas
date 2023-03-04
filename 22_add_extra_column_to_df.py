#!/usr/bin/env python3

# Python 3.9.5

# 22_add_extra_column_to_df.py

# Dependency
import pandas as pd

# total:    total amount
# tip:      tip for servant
# date:     date of service

columns = pd.Series(['total', 'tip', 'date'])

orders = [
    {'total': 25.98, 'tip': 4.02, 'date': '2023/03/05'},
    {'total': 10.17, 'tip': 0.83, 'date': '2023/03/05'},
    {'total': 15.38, 'tip': 1.62, 'date': '2023/03/06'},
    {'total': 12.99, 'tip': 0.01, 'date': '2023/03/06'},
    {'total': 15.00, 'tip': 0.00, 'date': '2023/03/07'},
    {'total': 38.79, 'tip': 1.21, 'date': '2023/03/07'},
    ]

orders = pd.DataFrame(orders, columns=columns)

# Add extra column for the calculated values
orders['tip_pct'] = orders['tip'] / orders['total']
print(orders)
