# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 07:12:22 2024

@author: Vinoj
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(r'C:\Users\Vinoj\OneDrive\Desktop\Ashoka_PEDP\IDCA Technical Round\IDCA Technical Round\dataset\climate_health_anonymized_dataset.csv')

columns = df.select_dtypes(include='number').columns
for col in columns:
    plt.figure(figsize=(8, 6))
    sns.histplot(df[col], kde=True)
    plt.title(col)
    plt.show()

correlation_matrix = df.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix')
plt.show()
