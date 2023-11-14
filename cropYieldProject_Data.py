import pandas as pd
import numpy as np

#Read data from file into variable
def readData(fileName):
    dataIn = pd.read_csv(fileName, header = [0], index_col = [0])
    dataIn.index.name = None

    return dataIn

def getMetricDataForPlot(dataIn, country, crop):
    if (country.lower() == 'all'):
        if (crop.lower() == 'all'):
            dataThndTonne = dataIn[(dataIn['Measure'] == 'THND_TONNE')]
        else:
            dataThndTonne = dataIn[(dataIn['Subject'] == crop) & (dataIn['Measure'] == 'THND_TONNE')]
    else:
        if (crop.lower() == 'all'):
            dataThndTonne = dataIn[(dataIn['Code'] == country) & (dataIn['Measure'] == 'THND_TONNE')]
        else:
            dataThndTonne = dataIn[(dataIn['Code'] == country) & (dataIn['Subject'] == crop) & (dataIn['Measure'] == 'THND_TONNE')]
    return dataThndTonne

def getHungerDataForPlot(dataIn, country):
    if (country.lower() == 'all'):
        hungerData = dataIn
    else:
        hungerData = dataIn[(dataIn['Code'] == country)]
    return hungerData


#Concats passed dataframes into a single dataframe, then groups data by year and calculates averages of data by year
def getWorldHungerDataForPlot(cp, gh, uw, hw, st):
    frame = [cp, gh, uw, hw, st]

    results = pd.concat(frame)

    resultsAvg = results.groupby(['Year'])
    resultsOut = resultsAvg[['Value','Global_Hunger_Index_2021','Prevalence_of_underweight_weight_for_age_percent_of_children_under_5','Prevalence_of_wasting_weight_for_height_percent_of_children_under_5','Prevalence_of_stunting_height_for_age_percent_of_children_under_5']].mean()
    
    #Fixes Formatting and indexing issues
    resultsOut.index.name = None
    resultsOut.insert(loc = 0, column = 'Year', value = resultsOut.index)

    resultsOut.to_excel('output.xlsx')
    return resultsOut