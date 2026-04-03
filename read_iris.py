#!/bin/usr python3

import pandas as pd

df = pd.read_csv('iris.csv')
print(df.head())

#Take a peak at the columns!
print("Columns:", df.columns)
print(df.describe())

# Visualization: scatter plot of first two numeric columns
plt.scatter(df[df.columns[0]], df[df.columns[1]])
plt.xlabel(df.columns[0])
plt.ylabel(df.columns[1])
plt.title("Scatter plot of first two iris columns")
plt.show()
