import pandas as pd
import matplotlib.pyplot as plt

#Function to read data from csv into program
def readData():
    dataIn = pd.read_csv("crop_production.csv", header = [0], index_col = [0])
    dataIn.index.name = None

    return dataIn

#Function to read, filter, and return data by country code and crop
def dataForPlot(data, country, crop, year):
    dataThndTonne = data.loc[(data['LOCATION'] == country) & (data['SUBJECT'] == crop) & (data['MEASURE'] == 'THND_TONNE') & (data['TIME'] == year)]

    return dataThndTonne

#Call function to read data
dataIn = readData()

#Get Unique Values for Country Codes and Crops from dataIn
countries = dataIn.LOCATION.unique()
crops = dataIn.SUBJECT.unique()
year = dataIn.TIME.unique()

numCountries = len(countries)
yr = min(year)
i = 0
print(yr)

#Loop to plot data for each country and crop on scatter plot
while yr <= max(year):
    totalYield = 0.0
    avgYield = 0.0

    while i < len(countries):
        plotData = dataForPlot(dataIn, countries[i], 'RICE', yr)
        totalYield = totalYield + plotData.Value
        i+=1

    avgYield = totalYield / numCountries
    print(i)
    print(totalYield)
    yr+=1


    #plotX = plotData.TIME
    #plotY = plotData.Value
    #plt.scatter(plotX, plotY, color = 'blue')
    #plt.plot(plotX, plotY, color = 'orange')
#plt.ylim(0,15)
#plt.show()

#df = pd.DataFrame()
#df['Country'] = countries[0::1]

#df.to_excel('output.xlsx', index = False)
