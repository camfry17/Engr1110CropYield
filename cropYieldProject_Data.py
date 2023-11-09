import pandas as pd
import numpy as np

#Read data from file into variable
def readData(fileName):
    dataIn = pd.read_csv(fileName, header = [0], index_col = [0])
    dataIn.index.name = None

    return dataIn


def getMetricDataForPlot(dataIn, country, crop):
    dataThndTonne = dataIn[(dataIn['Code'] == country) & (dataIn['Subject'] == crop) & (dataIn['Measure'] == 'THND_TONNE')]

    return dataThndTonne

def getHungerDataForPlot(dataIn, country):
    hungerData = dataIn[(dataIn['Code'] == country)]

    return hungerData


#NOT WORKING
#def getWorldHungerDataForPlot(dataIn):
    yearsList = dataIn.Year.unique()
    columnsList = list(dataIn.columns)
    arr = [[0] * 4] * len(yearsList)
    rows = 0
    i = 0
    
    for year in yearsList:
        hungerData = dataIn[(dataIn['Year'] == year)]
        sumData = hungerData[columnsList[2]].sum()
        maxData = hungerData[columnsList[2]].max()
        minData = hungerData[columnsList[2]].min()
        rows = len(dataIn[(dataIn['Year'] == year)])

        arr[0][i] = year
        arr[1][i] = sumData
        arr[2][i] = maxData
        arr[3][i] = minData

        i+=1

    print(yearsList)

