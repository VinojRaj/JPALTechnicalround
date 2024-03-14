# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 08:04:40 2024

@author: Vinoj
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv(r'C:\Users\Vinoj\OneDrive\Desktop\Ashoka_PEDP\IDCA Technical Round\IDCA Technical Round\dataset\climate_health_anonymized_dataset.csv')

column1 = 'land_surface_temperature_during_night'
column2 = 'ultraviolet_index'

correlation = df[column1].corr(df[column2])

plt.scatter(df[column1], df[column2])
plt.title(f'Correlation between {column1} and {column2}: {correlation:.2f}')
plt.xlabel(column1)
plt.ylabel(column2)
plt.show()

plt.scatter(df[column1], df[column2], label='Data Points')

z = np.polyfit(df[column1], df[column2], 1)
p = np.poly1d(z)
plt.plot(df[column1], p(df[column1]), color='red', label='Correlation Line')

plt.title(f'Correlation between {column1} and {column2}: {correlation:.2f}')
plt.xlabel(column1)
plt.ylabel(column2)
plt.legend()
plt.show()