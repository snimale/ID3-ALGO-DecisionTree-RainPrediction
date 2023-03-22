
import math
import numpy as np
import pandas as pd
import matplotlib


def entropy(willHappen, willNotHappen):
    if willHappen == willNotHappen:
        return 1
    elif willHappen == 0 or willNotHappen == 0:
        return 0
    else:
        total = willHappen + willNotHappen
        entro = -(willHappen / total) * math.log2(willHappen / total) - (willNotHappen / total) * math.log2(
            willNotHappen / total)
        return entro


willRain = 0
willNotRain = 0
gains = dict()
df = pd.read_excel("newData.xlsx", usecols='D, E, F, G, H')

# remove NaN rows - clean data
for index, row in df.iterrows():
    if pd.isnull(row['Rain']):
        df = df.drop(index)

df = df[df['Temp'] == 'm']
df = df[df['Wind'] == 'l']
df = df[df['Humidity'] == 'l']
df = df[df['Pressure'] == 'h']
print(len(df[df['Rain'] == 'n']))




