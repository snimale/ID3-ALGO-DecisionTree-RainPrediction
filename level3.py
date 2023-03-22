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

TLHHDF = df[df['Temp'] == 'l']  # temp low humidity high
TLHHDF = TLHHDF[TLHHDF['Humidity'] == 'h']

willRain = len([index for index, row in TLHHDF.iterrows() if row['Rain'] == 'y'])
willNotRain = len([index for index, row in TLHHDF.iterrows() if row['Rain'] == 'n'])
totalEntropy = entropy(willRain, willNotRain)

willRain = len([index for index, row in TLHHDF[TLHHDF['Pressure'] == 'l'].iterrows() if row['Rain'] == 'y'])
willNotRain = len([index for index, row in TLHHDF[TLHHDF['Pressure'] == 'l'].iterrows() if row['Rain'] == 'n'])
lowPressureEntropy = entropy(willRain, willNotRain)

willRain = len([index for index, row in TLHHDF[TLHHDF['Pressure'] == 'm'].iterrows() if row['Rain'] == 'y'])
willNotRain = len([index for index, row in TLHHDF[TLHHDF['Pressure'] == 'm'].iterrows() if row['Rain'] == 'n'])
moderatePressureEntropy = entropy(willRain, willNotRain)

willRain = len([index for index, row in TLHHDF[TLHHDF['Pressure'] == 'h'].iterrows() if row['Rain'] == 'y'])
willNotRain = len([index for index, row in TLHHDF[TLHHDF['Pressure'] == 'h'].iterrows() if row['Rain'] == 'n'])
highPressureEntropy = entropy(willRain, willNotRain)

gainPressure = totalEntropy - ((len(TLHHDF[TLHHDF['Pressure'] == 'l']) / len(TLHHDF)) * lowPressureEntropy +
                               (len(TLHHDF[TLHHDF['Pressure'] == 'm']) / len(TLHHDF)) * moderatePressureEntropy +
                               (len(TLHHDF[TLHHDF['Pressure'] == 'h']) / len(TLHHDF)) * highPressureEntropy)
gains['Pressure'] = gainPressure

willRain = len([index for index, row in TLHHDF[TLHHDF['Wind'] == 'l'].iterrows() if row['Rain'] == 'y'])
willNotRain = len([index for index, row in TLHHDF[TLHHDF['Wind'] == 'l'].iterrows() if row['Rain'] == 'n'])
lowWindEntropy = entropy(willRain, willNotRain)

willRain = len([index for index, row in TLHHDF[TLHHDF['Wind'] == 'h'].iterrows() if row['Rain'] == 'y'])
willNotRain = len([index for index, row in TLHHDF[TLHHDF['Wind'] == 'h'].iterrows() if row['Rain'] == 'n'])
highWindEntropy = entropy(willRain, willNotRain)

gainWind = totalEntropy - ((len(TLHHDF[TLHHDF['Wind'] == 'l']) / len(TLHHDF)) * lowWindEntropy +
                           (len(TLHHDF[TLHHDF['Wind'] == 'h']) / len(TLHHDF)) * highWindEntropy)
gains['Wind'] = gainWind

gains.clear()
HTLPDF = df[df['Temp'] == 'h']
HTLPDF = HTLPDF[HTLPDF['Pressure'] == 'l']

willRain = len([index for index, row in HTLPDF.iterrows() if row['Rain'] == 'y'])
willNotRain = len([index for index, row in HTLPDF.iterrows() if row['Rain'] == 'n'])
totalEntropy = entropy(willRain, willNotRain)

willRain = len([index for index, row in HTLPDF[HTLPDF['Humidity'] == 'vl'].iterrows() if row['Rain'] == 'y'])
willNotRain = len([index for index, row in HTLPDF[HTLPDF['Humidity'] == 'vl'].iterrows() if row['Rain'] == 'n'])
veryLowHumidityEntropy = entropy(willRain, willNotRain)

willRain = len([index for index, row in HTLPDF[HTLPDF['Humidity'] == 'l'].iterrows() if row['Rain'] == 'y'])
willNotRain = len([index for index, row in HTLPDF[HTLPDF['Humidity'] == 'l'].iterrows() if row['Rain'] == 'n'])
lowHumidityEntropy = entropy(willRain, willNotRain)

willRain = len([index for index, row in HTLPDF[HTLPDF['Humidity'] == 'm'].iterrows() if row['Rain'] == 'y'])
willNotRain = len([index for index, row in HTLPDF[HTLPDF['Humidity'] == 'm'].iterrows() if row['Rain'] == 'n'])
moderateHumidityEntropy = entropy(willRain, willNotRain)

willRain = len([index for index, row in HTLPDF[HTLPDF['Humidity'] == 'h'].iterrows() if row['Rain'] == 'y'])
willNotRain = len([index for index, row in HTLPDF[HTLPDF['Humidity'] == 'h'].iterrows() if row['Rain'] == 'n'])
highHumidityEntropy = entropy(willRain, willNotRain)

gainHumidity = totalEntropy - ((len(HTLPDF[HTLPDF['Humidity'] == 'vl']) / len(HTLPDF)) * veryLowHumidityEntropy +
                               (len(HTLPDF[HTLPDF['Humidity'] == 'l']) / len(HTLPDF)) * lowHumidityEntropy +
                               (len(HTLPDF[HTLPDF['Humidity'] == 'm']) / len(HTLPDF)) * moderateHumidityEntropy +
                               (len(HTLPDF[HTLPDF['Humidity'] == 'h']) / len(HTLPDF)) * highHumidityEntropy)
gains['Humidity'] = gainHumidity

willRain = len([index for index, row in HTLPDF[HTLPDF['Wind'] == 'l'].iterrows() if row['Rain'] == 'y'])
willNotRain = len([index for index, row in HTLPDF[HTLPDF['Wind'] == 'l'].iterrows() if row['Rain'] == 'n'])
lowWindEntropy = entropy(willRain, willNotRain)

willRain = len([index for index, row in HTLPDF[HTLPDF['Wind'] == 'h'].iterrows() if row['Rain'] == 'y'])
willNotRain = len([index for index, row in HTLPDF[HTLPDF['Wind'] == 'h'].iterrows() if row['Rain'] == 'n'])
highWindEntropy = entropy(willRain, willNotRain)

gainWind = totalEntropy - ((len(HTLPDF[HTLPDF['Wind'] == 'l']) / len(HTLPDF)) * lowWindEntropy +
                           (len(HTLPDF[HTLPDF['Wind'] == 'h']) / len(HTLPDF)) * highWindEntropy)
gains['Wind'] = gainWind
gains.clear()

TMHLDF = df[df['Temp'] == 'm']
TMHLDF = TMHLDF[TMHLDF['Humidity'] == 'l']

willRain = len([index for index, row in TMHLDF.iterrows() if row['Rain'] == 'y'])
willNotRain = len([index for index, row in TMHLDF.iterrows() if row['Rain'] == 'n'])
totalEntropy = entropy(willRain, willNotRain)
print(TMHLDF)

willRain = len([index for index, row in TMHLDF[TMHLDF['Wind'] == 'l'].iterrows() if row['Rain'] == 'y'])
willNotRain = len([index for index, row in TMHLDF[TMHLDF['Wind'] == 'l'].iterrows() if row['Rain'] == 'n'])
lowWindEntropy = entropy(willRain, willNotRain)

willRain = len([index for index, row in TMHLDF[TMHLDF['Wind'] == 'h'].iterrows() if row['Rain'] == 'y'])
willNotRain = len([index for index, row in TMHLDF[TMHLDF['Wind'] == 'h'].iterrows() if row['Rain'] == 'n'])
highWindEntropy = entropy(willRain, willNotRain)

gainWind = totalEntropy - ((len(TMHLDF[TMHLDF['Wind'] == 'l']) / len(TMHLDF)) * lowWindEntropy +
                           (len(TMHLDF[TMHLDF['Wind'] == 'h']) / len(TMHLDF)) * highWindEntropy)
gains['Wind'] = gainWind

willRain = len([index for index, row in TMHLDF[TMHLDF['Pressure'] == 'l'].iterrows() if row['Rain'] == 'y'])
willNotRain = len([index for index, row in TMHLDF[TMHLDF['Pressure'] == 'l'].iterrows() if row['Rain'] == 'n'])
lowPressureEntropy = entropy(willRain, willNotRain)

willRain = len([index for index, row in TMHLDF[TMHLDF['Pressure'] == 'm'].iterrows() if row['Rain'] == 'y'])
willNotRain = len([index for index, row in TMHLDF[TMHLDF['Pressure'] == 'm'].iterrows() if row['Rain'] == 'n'])
moderatePressureEntropy = entropy(willRain, willNotRain)

willRain = len([index for index, row in TMHLDF[TMHLDF['Pressure'] == 'h'].iterrows() if row['Rain'] == 'y'])
willNotRain = len([index for index, row in TMHLDF[TMHLDF['Pressure'] == 'h'].iterrows() if row['Rain'] == 'n'])
highPressureEntropy = entropy(willRain, willNotRain)

gainPressure = totalEntropy - (len(TMHLDF[TMHLDF['Pressure'] == 'l']) / len(TMHLDF) * lowPressureEntropy +
                               len(TMHLDF[TMHLDF['Pressure'] == 'm']) / len(TMHLDF) * moderatePressureEntropy +
                               len(TMHLDF[TMHLDF['Pressure'] == 'h']) / len(TMHLDF) * highPressureEntropy)

gains['Pressure'] = gainPressure
gains.clear()
