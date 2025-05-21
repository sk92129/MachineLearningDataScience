import pandas as pd
import csv
import numpy as np

df = pd.DataFrame({
    'Region': ['North', 'North', 'South', 'South'],
    'Category': ['A', 'B', 'A', 'B'],
    'Sales': [100, 200, 150, 250],
    'Profit': [50, 20, 50, 100]
})

# Group by 'Region' and 'Category'
grouped = df.groupby(['Region', 'Category'])

# Calculate the sum of sales for each group
result = grouped['Sales'].sum()

print(result)

def showcount(series):
    result = len(series)
    #print(result)
    return result

df_result = grouped['Sales'].agg([showcount])

print(type(df_result))

print(df_result.columns)
