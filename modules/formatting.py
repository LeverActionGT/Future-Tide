import pandas as pd


df = pd.read_csv('brestElevation.csv', delimiter=';')
print(df.head())
df.to_csv('BBrestElevation.csv')
