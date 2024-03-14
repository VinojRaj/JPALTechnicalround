# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 07:25:25 2024

@author: Vinoj
"""
import pandas as pd

df = pd.read_csv(r'C:\Users\Vinoj\OneDrive\Desktop\Ashoka_PEDP\IDCA Technical Round\IDCA Technical Round\dataset\climate_health_anonymized_dataset.csv')

print(df.head()) 
print(df.info())  
print(df.describe())  

summary_stats = df.describe()
summary_stats.to_csv(r'C:\Users\Vinoj\OneDrive\Desktop\Ashoka_PEDP\IDCA Technical Round\IDCA Technical Round\output\summary_statistics.csv')
