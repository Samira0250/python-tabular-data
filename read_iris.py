#!/bin/usr python3

import pandas as pd

df = pd.read_csv('iris.csv')
print(df.head())

#Take a peak at the columns!
print("Columns:", df.columns)
print(df.describe())

