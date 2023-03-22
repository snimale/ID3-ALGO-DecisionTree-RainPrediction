# assuming temperature to be the first root node:

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

# first for temp = l
lowTempDF = df[df['Temp'] == 'l']
willRain = len([index for index, row in lowTempDF.iterrows() if row['Rain'] == 'y'])
willNotRain = len([index for index, row in lowTempDF.iterrows() if row['Rain'] == 'n'])
totalEntropy = entropy(willRain, willNotRain)

# humidity gain with respect to low temperature DF:
willRain = len([index for index, row in lowTempDF[lowTempDF['Humidity'] == 'vl'].iterrows() if row['Rain'] == 'y'])
willNotRain = len([index for index, row in lowTempDF[lowTempDF['Humidity'] == 'vl'].iterrows() if row['Rain'] == 'n'])
vlHumidityEntropy = entropy(willRain, willNotRain)

willRain = len([index for index, row in lowTempDF[lowTempDF['Humidity'] == 'l'].iterrows() if row['Rain'] == 'y'])
willNotRain = len([index for index, row in lowTempDF[lowTempDF['Humidity'] == 'l'].iterrows() if row['Rain'] == 'n'])
lHumidityEntropy = entropy(willRain, willNotRain)

willRain = len([index for index, row in lowTempDF[lowTempDF['Humidity'] == 'm'].iterrows() if row['Rain'] == 'y'])
willNotRain = len([index for index, row in lowTempDF[lowTempDF['Humidity'] == 'm'].iterrows() if row['Rain'] == 'n'])
mHumidityEntropy = entropy(willRain, willNotRain)

willRain = len([index for index, row in lowTempDF[lowTempDF['Humidity'] == 'h'].iterrows() if row['Rain'] == 'y'])
willNotRain = len([index for index, row in lowTempDF[lowTempDF['Humidity'] == 'h'].iterrows() if row['Rain'] == 'n'])
hHumidityEntropy = entropy(willRain, willNotRain)

gainHumidity = totalEntropy - ((len(lowTempDF[lowTempDF['Humidity'] == 'vl']) / len(lowTempDF)) * vlHumidityEntropy +
                               (len(lowTempDF[lowTempDF['Humidity'] == 'l']) / len(lowTempDF)) * lHumidityEntropy +
                               (len(lowTempDF[lowTempDF['Humidity'] == 'm']) / len(lowTempDF)) * mHumidityEntropy +
                               (len(lowTempDF[lowTempDF['Humidity'] == 'h']) / len(lowTempDF)) * hHumidityEntropy)
gains['Humidity'] = gainHumidity

# Pressure gain with respect to total data:
willRain = len([index for index, row in lowTempDF[lowTempDF['Pressure'] == 'l'].iterrows() if row['Rain'] == 'y'])
willNotRain = len([index for index, row in lowTempDF[lowTempDF['Pressure'] == 'l'].iterrows() if row['Rain'] == 'n'])
lPressureEntropy = entropy(willRain, willNotRain)

willRain = len([index for index, row in lowTempDF[lowTempDF['Pressure'] == 'm'].iterrows() if row['Rain'] == 'y'])
willNotRain = len([index for index, row in lowTempDF[lowTempDF['Pressure'] == 'm'].iterrows() if row['Rain'] == 'n'])
mPressureEntropy = entropy(willRain, willNotRain)

willRain = len([index for index, row in lowTempDF[lowTempDF['Pressure'] == 'h'].iterrows() if row['Rain'] == 'y'])
willNotRain = len([index for index, row in lowTempDF[lowTempDF['Pressure'] == 'h'].iterrows() if row['Rain'] == 'n'])
hPressureEntropy = entropy(willRain, willNotRain)

gainPressure = totalEntropy - ((len(lowTempDF[lowTempDF['Pressure'] == 'l']) / len(lowTempDF)) * lPressureEntropy +
                               (len(lowTempDF[lowTempDF['Pressure'] == 'm']) / len(lowTempDF)) * mPressureEntropy +
                               (len(lowTempDF[lowTempDF['Pressure'] == 'h']) / len(lowTempDF)) * hPressureEntropy)
gains['Pressure'] = gainPressure

# Wind gain with respect to total data
willRain = len([index for index, row in lowTempDF[lowTempDF['Wind'] == 'l'].iterrows() if row['Rain'] == 'y'])
willNotRain = len([index for index, row in lowTempDF[lowTempDF['Wind'] == 'l'].iterrows() if row['Rain'] == 'n'])
lWindEntropy = entropy(willRain, willNotRain)

willRain = len([index for index, row in lowTempDF[lowTempDF['Wind'] == 'h'].iterrows() if row['Rain'] == 'y'])
willNotRain = len([index for index, row in lowTempDF[lowTempDF['Wind'] == 'h'].iterrows() if row['Rain'] == 'n'])
hWindEntropy = entropy(willRain, willNotRain)

gainWind = totalEntropy - ((len(lowTempDF[lowTempDF['Wind'] == 'l']) / len(lowTempDF)) * lWindEntropy +
                           (len(lowTempDF[lowTempDF['Wind'] == 'h']) / len(lowTempDF)) * hWindEntropy)
gains['Wind'] = gainWind

maxGainsAttribute = '-'
for key in gains.keys():
    if gains[key] == max(gains.values()):
        maxGainsAttribute = key
print("low temperature -> ", maxGainsAttribute)
gains.clear()

# second for temp = m
moderateTempDF = df[df['Temp'] == 'm']
willRain = len([index for index, row in moderateTempDF.iterrows() if row['Rain'] == 'y'])
willNotRain = len([index for index, row in moderateTempDF.iterrows() if row['Rain'] == 'n'])
totalEntropy = entropy(willRain, willNotRain)

# humidity gain with respect to moderate temperature DF:
willRain = len([index for index, row in moderateTempDF[moderateTempDF['Humidity'] == 'vl'].iterrows() if row['Rain'] == 'y'])
willNotRain = len([index for index, row in moderateTempDF[moderateTempDF['Humidity'] == 'vl'].iterrows() if row['Rain'] == 'n'])
vlHumidityEntropy = entropy(willRain, willNotRain)

willRain = len([index for index, row in moderateTempDF[moderateTempDF['Humidity'] == 'l'].iterrows() if row['Rain'] == 'y'])
willNotRain = len([index for index, row in moderateTempDF[moderateTempDF['Humidity'] == 'l'].iterrows() if row['Rain'] == 'n'])
lHumidityEntropy = entropy(willRain, willNotRain)

willRain = len([index for index, row in moderateTempDF[moderateTempDF['Humidity'] == 'm'].iterrows() if row['Rain'] == 'y'])
willNotRain = len([index for index, row in moderateTempDF[moderateTempDF['Humidity'] == 'm'].iterrows() if row['Rain'] == 'n'])
mHumidityEntropy = entropy(willRain, willNotRain)

willRain = len([index for index, row in moderateTempDF[moderateTempDF['Humidity'] == 'h'].iterrows() if row['Rain'] == 'y'])
willNotRain = len([index for index, row in moderateTempDF[moderateTempDF['Humidity'] == 'h'].iterrows() if row['Rain'] == 'n'])
hHumidityEntropy = entropy(willRain, willNotRain)

gainHumidity = totalEntropy - ((len(moderateTempDF[moderateTempDF['Humidity'] == 'vl']) / len(moderateTempDF)) * vlHumidityEntropy +
                               (len(moderateTempDF[moderateTempDF['Humidity'] == 'l']) / len(moderateTempDF)) * lHumidityEntropy +
                               (len(moderateTempDF[moderateTempDF['Humidity'] == 'm']) / len(moderateTempDF)) * mHumidityEntropy +
                               (len(moderateTempDF[moderateTempDF['Humidity'] == 'h']) / len(moderateTempDF)) * hHumidityEntropy)
gains['Humidity'] = gainHumidity

# Pressure gain with respect to total data:
willRain = len([index for index, row in moderateTempDF[moderateTempDF['Pressure'] == 'l'].iterrows() if row['Rain'] == 'y'])
willNotRain = len([index for index, row in moderateTempDF[moderateTempDF['Pressure'] == 'l'].iterrows() if row['Rain'] == 'n'])
lPressureEntropy = entropy(willRain, willNotRain)

willRain = len([index for index, row in moderateTempDF[moderateTempDF['Pressure'] == 'm'].iterrows() if row['Rain'] == 'y'])
willNotRain = len([index for index, row in moderateTempDF[moderateTempDF['Pressure'] == 'm'].iterrows() if row['Rain'] == 'n'])
mPressureEntropy = entropy(willRain, willNotRain)

willRain = len([index for index, row in moderateTempDF[moderateTempDF['Pressure'] == 'h'].iterrows() if row['Rain'] == 'y'])
willNotRain = len([index for index, row in moderateTempDF[moderateTempDF['Pressure'] == 'h'].iterrows() if row['Rain'] == 'n'])
hPressureEntropy = entropy(willRain, willNotRain)

gainPressure = totalEntropy - ((len(moderateTempDF[moderateTempDF['Pressure'] == 'l']) / len(moderateTempDF)) * lPressureEntropy +
                               (len(moderateTempDF[moderateTempDF['Pressure'] == 'm']) / len(moderateTempDF)) * mPressureEntropy +
                               (len(moderateTempDF[moderateTempDF['Pressure'] == 'h']) / len(moderateTempDF)) * hPressureEntropy)
gains['Pressure'] = gainPressure

# Wind gain with respect to total data
willRain = len([index for index, row in moderateTempDF[moderateTempDF['Wind'] == 'l'].iterrows() if row['Rain'] == 'y'])
willNotRain = len([index for index, row in moderateTempDF[moderateTempDF['Wind'] == 'l'].iterrows() if row['Rain'] == 'n'])
lWindEntropy = entropy(willRain, willNotRain)

willRain = len([index for index, row in moderateTempDF[moderateTempDF['Wind'] == 'h'].iterrows() if row['Rain'] == 'y'])
willNotRain = len([index for index, row in moderateTempDF[moderateTempDF['Wind'] == 'h'].iterrows() if row['Rain'] == 'n'])
hWindEntropy = entropy(willRain, willNotRain)

gainWind = totalEntropy - ((len(moderateTempDF[moderateTempDF['Wind'] == 'l']) / len(moderateTempDF)) * lWindEntropy +
                           (len(moderateTempDF[moderateTempDF['Wind'] == 'h']) / len(moderateTempDF)) * hWindEntropy)
gains['Wind'] = gainWind

maxGainsAttribute = '-'
for key in gains.keys():
    if gains[key] == max(gains.values()):
        maxGainsAttribute = key
print("moderate temperature -> ", maxGainsAttribute)
gains.clear()

# third for temp = m
highTempDF = df[df['Temp'] == 'h']
willRain = len([index for index, row in highTempDF.iterrows() if row['Rain'] == 'y'])
willNotRain = len([index for index, row in highTempDF.iterrows() if row['Rain'] == 'n'])
totalEntropy = entropy(willRain, willNotRain)

# humidity gain with respect to moderate temperature DF:
willRain = len([index for index, row in highTempDF[highTempDF['Humidity'] == 'vl'].iterrows() if row['Rain'] == 'y'])
willNotRain = len([index for index, row in highTempDF[highTempDF['Humidity'] == 'vl'].iterrows() if row['Rain'] == 'n'])
vlHumidityEntropy = entropy(willRain, willNotRain)

willRain = len([index for index, row in highTempDF[highTempDF['Humidity'] == 'l'].iterrows() if row['Rain'] == 'y'])
willNotRain = len([index for index, row in highTempDF[highTempDF['Humidity'] == 'l'].iterrows() if row['Rain'] == 'n'])
lHumidityEntropy = entropy(willRain, willNotRain)

willRain = len([index for index, row in highTempDF[highTempDF['Humidity'] == 'm'].iterrows() if row['Rain'] == 'y'])
willNotRain = len([index for index, row in highTempDF[highTempDF['Humidity'] == 'm'].iterrows() if row['Rain'] == 'n'])
mHumidityEntropy = entropy(willRain, willNotRain)

willRain = len([index for index, row in highTempDF[highTempDF['Humidity'] == 'h'].iterrows() if row['Rain'] == 'y'])
willNotRain = len([index for index, row in highTempDF[highTempDF['Humidity'] == 'h'].iterrows() if row['Rain'] == 'n'])
hHumidityEntropy = entropy(willRain, willNotRain)

gainHumidity = totalEntropy - ((len(highTempDF[highTempDF['Humidity'] == 'vl']) / len(highTempDF)) * vlHumidityEntropy +
                               (len(highTempDF[highTempDF['Humidity'] == 'l']) / len(highTempDF)) * lHumidityEntropy +
                               (len(highTempDF[highTempDF['Humidity'] == 'm']) / len(highTempDF)) * mHumidityEntropy +
                               (len(highTempDF[highTempDF['Humidity'] == 'h']) / len(highTempDF)) * hHumidityEntropy)
gains['Humidity'] = gainHumidity

# Pressure gain with respect to total data:
willRain = len([index for index, row in highTempDF[highTempDF['Pressure'] == 'l'].iterrows() if row['Rain'] == 'y'])
willNotRain = len([index for index, row in highTempDF[highTempDF['Pressure'] == 'l'].iterrows() if row['Rain'] == 'n'])
lPressureEntropy = entropy(willRain, willNotRain)

willRain = len([index for index, row in highTempDF[highTempDF['Pressure'] == 'm'].iterrows() if row['Rain'] == 'y'])
willNotRain = len([index for index, row in highTempDF[highTempDF['Pressure'] == 'm'].iterrows() if row['Rain'] == 'n'])
mPressureEntropy = entropy(willRain, willNotRain)

willRain = len([index for index, row in highTempDF[highTempDF['Pressure'] == 'h'].iterrows() if row['Rain'] == 'y'])
willNotRain = len([index for index, row in highTempDF[highTempDF['Pressure'] == 'h'].iterrows() if row['Rain'] == 'n'])
hPressureEntropy = entropy(willRain, willNotRain)

gainPressure = totalEntropy - ((len(highTempDF[highTempDF['Pressure'] == 'l']) / len(highTempDF)) * lPressureEntropy +
                               (len(highTempDF[highTempDF['Pressure'] == 'm']) / len(highTempDF)) * mPressureEntropy +
                               (len(highTempDF[highTempDF['Pressure'] == 'h']) / len(highTempDF)) * hPressureEntropy)
gains['Pressure'] = gainPressure

# Wind gain with respect to total data
willRain = len([index for index, row in highTempDF[highTempDF['Wind'] == 'l'].iterrows() if row['Rain'] == 'y'])
willNotRain = len([index for index, row in highTempDF[highTempDF['Wind'] == 'l'].iterrows() if row['Rain'] == 'n'])
lWindEntropy = entropy(willRain, willNotRain)

willRain = len([index for index, row in highTempDF[highTempDF['Wind'] == 'h'].iterrows() if row['Rain'] == 'y'])
willNotRain = len([index for index, row in highTempDF[highTempDF['Wind'] == 'h'].iterrows() if row['Rain'] == 'n'])
hWindEntropy = entropy(willRain, willNotRain)

gainWind = totalEntropy - ((len(highTempDF[highTempDF['Wind'] == 'l']) / len(highTempDF)) * lWindEntropy +
                           (len(highTempDF[highTempDF['Wind'] == 'h']) / len(highTempDF)) * hWindEntropy)
gains['Wind'] = gainWind

maxGainsAttribute = '-'
for key in gains.keys():
    if gains[key] == max(gains.values()):
        maxGainsAttribute = key
print("high temperature -> ", maxGainsAttribute)
gains.clear()
