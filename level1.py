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

willRain = len([index for index, row in df.iterrows() if row['Rain'] == 'y'])
willNotRain = len([index for index, row in df.iterrows() if row['Rain'] == 'n'])
totalEntropy = entropy(willRain, willNotRain)

# humidity gain with respect to total data:
willRain = len([index for index, row in df[df['Humidity'] == 'vl'].iterrows() if row['Rain'] == 'y'])
willNotRain = len([index for index, row in df[df['Humidity'] == 'vl'].iterrows() if row['Rain'] == 'n'])
vlHumidityEntropy = entropy(willRain, willNotRain)

willRain = len([index for index, row in df[df['Humidity'] == 'l'].iterrows() if row['Rain'] == 'y'])
willNotRain = len([index for index, row in df[df['Humidity'] == 'l'].iterrows() if row['Rain'] == 'n'])
lHumidityEntropy = entropy(willRain, willNotRain)

willRain = len([index for index, row in df[df['Humidity'] == 'm'].iterrows() if row['Rain'] == 'y'])
willNotRain = len([index for index, row in df[df['Humidity'] == 'm'].iterrows() if row['Rain'] == 'n'])
mHumidityEntropy = entropy(willRain, willNotRain)

willRain = len([index for index, row in df[df['Humidity'] == 'h'].iterrows() if row['Rain'] == 'y'])
willNotRain = len([index for index, row in df[df['Humidity'] == 'h'].iterrows() if row['Rain'] == 'n'])
hHumidityEntropy = entropy(willRain, willNotRain)

gainHumidity = totalEntropy - ((len(df[df['Humidity'] == 'vl']) / len(df)) * vlHumidityEntropy +
                               (len(df[df['Humidity'] == 'l']) / len(df)) * lHumidityEntropy +
                               (len(df[df['Humidity'] == 'm']) / len(df)) * mHumidityEntropy +
                               (len(df[df['Humidity'] == 'h']) / len(df)) * hHumidityEntropy)
gains['Humidity'] = gainHumidity

# Temp gain with respect to total data:
willRain = len([index for index, row in df[df['Temp'] == 'l'].iterrows() if row['Rain'] == 'y'])
willNotRain = len([index for index, row in df[df['Temp'] == 'l'].iterrows() if row['Rain'] == 'n'])
lTempEntropy = entropy(willRain, willNotRain)

willRain = len([index for index, row in df[df['Temp'] == 'm'].iterrows() if row['Rain'] == 'y'])
willNotRain = len([index for index, row in df[df['Temp'] == 'm'].iterrows() if row['Rain'] == 'n'])
mTempEntropy = entropy(willRain, willNotRain)

willRain = len([index for index, row in df[df['Temp'] == 'h'].iterrows() if row['Rain'] == 'y'])
willNotRain = len([index for index, row in df[df['Temp'] == 'h'].iterrows() if row['Rain'] == 'n'])
hTempEntropy = entropy(willRain, willNotRain)

gainTemp = totalEntropy - ((len(df[df['Temp'] == 'l']) / len(df)) * lTempEntropy +
                           (len(df[df['Temp'] == 'm']) / len(df)) * mTempEntropy +
                           (len(df[df['Temp'] == 'h']) / len(df)) * hTempEntropy)
gains['Temp'] = gainTemp

# Pressure gain with respect to total data:
willRain = len([index for index, row in df[df['Pressure'] == 'l'].iterrows() if row['Rain'] == 'y'])
willNotRain = len([index for index, row in df[df['Pressure'] == 'l'].iterrows() if row['Rain'] == 'n'])
lPressureEntropy = entropy(willRain, willNotRain)

willRain = len([index for index, row in df[df['Pressure'] == 'm'].iterrows() if row['Rain'] == 'y'])
willNotRain = len([index for index, row in df[df['Pressure'] == 'm'].iterrows() if row['Rain'] == 'n'])
mPressureEntropy = entropy(willRain, willNotRain)

willRain = len([index for index, row in df[df['Pressure'] == 'h'].iterrows() if row['Rain'] == 'y'])
willNotRain = len([index for index, row in df[df['Pressure'] == 'h'].iterrows() if row['Rain'] == 'n'])
hPressureEntropy = entropy(willRain, willNotRain)

gainPressure = totalEntropy - ((len(df[df['Pressure'] == 'l']) / len(df)) * lPressureEntropy +
                               (len(df[df['Pressure'] == 'm']) / len(df)) * mPressureEntropy +
                               (len(df[df['Pressure'] == 'h']) / len(df)) * hPressureEntropy)
gains['Pressure'] = gainPressure

# Wind gain with respect to total data
willRain = len([index for index, row in df[df['Wind'] == 'l'].iterrows() if row['Rain'] == 'y'])
willNotRain = len([index for index, row in df[df['Wind'] == 'l'].iterrows() if row['Rain'] == 'n'])
lWindEntropy = entropy(willRain, willNotRain)

willRain = len([index for index, row in df[df['Wind'] == 'h'].iterrows() if row['Rain'] == 'y'])
willNotRain = len([index for index, row in df[df['Wind'] == 'h'].iterrows() if row['Rain'] == 'n'])
hWindEntropy = entropy(willRain, willNotRain)

gainWind = totalEntropy - ((len(df[df['Wind'] == 'l']) / len(df)) * lWindEntropy +
                           (len(df[df['Wind'] == 'h']) / len(df)) * hWindEntropy)
gains['Wind'] = gainWind

maxGainsAttribute = '-'
for key in gains.keys():
    if gains[key] == max(gains.values()):
        maxGainsAttribute = key
print(maxGainsAttribute)

