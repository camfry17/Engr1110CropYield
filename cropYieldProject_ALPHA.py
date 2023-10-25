import pandas as pd
import matplotlib.pyplot as plt

#Function to read data from csv into program
def readData():
    dataIn = pd.read_csv("crop_production.csv", header = [0], index_col = [0])
    dataIn.index.name = None

    return dataIn

#Function to read, filter, and return data by country code and crop
def getDataForPlot(data, country, crop):
    dataThndTonne = data[(data['LOCATION'] == country) & (data['SUBJECT'] == crop) & (data['MEASURE'] == 'THND_TONNE')]

    return dataThndTonne

#Call function to read data
dataIn = readData()

#Get Unique Values for Country Codes and Crops from dataIn
#For later use
countries = dataIn.LOCATION.unique()
crops = dataIn.SUBJECT.unique()
year = dataIn.TIME.unique()

#Get input to filter data by country code and crop type for plot
#Input separated by space; ex. aus rice assigns plotData with data from dataIn filtered by AUS and RICE
filterIn = input().split()
countryCode = filterIn[0]
crop = filterIn[1]
plotData = getDataForPlot(dataIn, countryCode.upper(), crop.upper())

#Build visualizations and show plot
plX = plotData.TIME
plY = plotData.Value
ax = plt.subplot()
ax.scatter(plX, plY, color = 'blue')
ax.plot(plX, plY, color = 'orange')
ax.set_title(crop.capitalize() + " Yield in " + countryCode.upper())
ax.set_xlabel("Crop Year")
ax.set_ylabel("Amount in Metric Tonnes")
ax.margins(0.1,0.1)
plt.show()
