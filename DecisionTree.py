import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def will_rain(Temp, Pressure, Humidity, Wind):
    if Temp == 'l':
        if Humidity == 'vl':
            return None
        elif Humidity == 'l':
            return None
        elif Humidity == 'm':
            return False
        elif Humidity == 'h':
            if Pressure == 'l':
                return None
            elif Pressure == 'm':
                if Wind == 'l':
                    return False
                elif Wind == 'h':
                    return True
            elif Pressure == 'h':
                return False
    elif Temp == 'm':
        if Humidity == 'vl':
            return False
        elif Humidity == 'l':
            if Wind == 'l':
                if Pressure == 'l':
                    return False
                elif Pressure == 'm':
                    return False
                elif Pressure == 'h':
                    return None
            elif Wind == 'h':
                return False
        elif Humidity == 'm':
            return True
        elif Humidity == 'h':
            return True
    elif Temp == 'h':
        if Pressure == 'l':
            if Humidity == 'vl':
                if Wind == 'l':
                    return False
                elif Wind == 'h':
                    return True
            elif Humidity == 'l':
                return False
            elif Humidity == 'm':
                return None
            elif Humidity == 'h':
                return None
        elif Pressure == 'm':
            return False
        elif Pressure == 'h':
            return None
    return None


df = pd.read_excel("testingData.xlsx", usecols='C, D, E, F, G')
for index, row in df.iterrows():
    if pd.isnull(row['Rain']):
        df = df.drop(index)

correct = 0
nodata = 0
knownData = 0
for index, row in df.iterrows():
    if will_rain(row['Temp'], row['Pressure'], row['Humidity'], row['Wind']) is None:
        nodata += 1
        continue
    else:
        if will_rain(row['Temp'], row['Pressure'], row['Humidity'], row['Wind']) and row['Rain'] == 'y':
            correct += 1
        elif will_rain(row['Temp'], row['Pressure'], row['Humidity'], row['Wind']) is False and row['Rain'] == 'n':
            correct += 1
    knownData += 1

print("\nUnpredictable data :", nodata / len(df) * 100)
print('Predictable data:', 100 - nodata / len(df) * 100)
print('\ncorrect predictions %', correct / knownData * 100)
print('incorrect predictions %', 100 - correct / knownData * 100)

# plt.pie([nodata / len(df) * 100, 100 - nodata / len(df) * 100], labels=["Unpredictable", "Predictable"], explode=[0.2, 0], autopct='%1.2f%%')
plt.pie([correct / knownData * 100, 100 - correct / knownData * 100], labels=["Correct\nPrediction", "Incorrect\nPrediction"], explode=[0, 0],
        autopct='%1.2f%%', colors=['#ccffcc', '#ccccff'])
plt.title("Rain Prediction Using ML")
plt.show()
