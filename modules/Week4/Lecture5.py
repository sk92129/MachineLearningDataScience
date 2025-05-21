import pandas as pd
import csv
import numpy as np

babyNames=pd.read_csv("babyNames.csv")

#print(babyNames.head())

def ammd(series):
    # print("running ammd")
    return max(series) - min(series)


babyNamesPivotUnisexContrast = babyNames.pivot_table(index = ['Name'], columns=[], values=['Count'], aggfunc=ammd)

print(babyNamesPivotUnisexContrast.head(10))