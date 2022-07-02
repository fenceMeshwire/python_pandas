#!/usr/bin/env python3

# Python 3.9.5

# 08_pandas_df_data_selection.py

# Dependencies
import pandas as pd

density = pd.Series({'Gold': 19.32, 'Silver': 10.49, 'Platinum': 21.45, 'Palladium': 11.99})
earth_abundance = pd.Series({'Gold': 0.004, 'Silver': 0.079, 'Platinum': 0.005, 'Palladium': 0.011})

res_data = pd.DataFrame({'density':density, 'abundance':earth_abundance})

res_data['density']   # Shows column density
res_data['abundance'] # Shows column abundance (abundance in earth's crust)

res_data.loc[res_data.density > 19, ['density']] # Shows specific values and
