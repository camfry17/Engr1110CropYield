import pandas as pd

def readData(fileName):
    dataIn = pd.read_csv(fileName, header = [0], index_col = [0])
    dataIn.index.name = None

    return dataIn

def getDataForPlot(data, country, crop):
    dataThndTonne = data[(data['LOCATION'] == country) & (data['SUBJECT'] == crop) & (data['MEASURE'] == 'THND_TONNE')]

    return dataThndTonne