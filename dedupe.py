import pandas as pd
import sys

df = pd.read_csv("/tmp/switch_ed.csv", 'wb', header=None, na_values=[" "], usecols=[0]) #imports appropriate csv to dataframe

df = df.drop_duplicates()

df[0] = df[0].map(lambda x: x.encode('unicode-escape').decode('utf-8'))  # this is amazing. Solves ascii encoding problem!


with open('/Users/davkenda1/Desktop/switch_ed.csv', 'w') as f:
    df.to_csv(f, header=None, encoding='utf-8', index=False)
