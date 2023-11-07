import pandas as pd

#Read data from file into variable
def readData(fileName):
    dataIn = pd.read_csv(fileName, header = [0], index_col = [0])
    dataIn.index.name = None

    return dataIn


def getMetricDataForPlot(prodData, country, crop):
    dataThndTonne = prodData[(prodData['Code'] == country) & (prodData['Subject'] == crop) & (prodData['Measure'] == 'THND_TONNE')]

    return dataThndTonne

def getDataForPlot(dataIn, country):
    hungerData = dataIn[(dataIn['Code'] == country)]

    return hungerData