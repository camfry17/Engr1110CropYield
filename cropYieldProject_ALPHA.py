import pandas as pd
import matplotlib.pyplot as plt

#Function to read data from csv into program
def readData():
    dataIn = pd.read_csv("SOURCE_DATA/crop_production.csv", header = [0], index_col = [0])
    dataIn.index.name = None

    return dataIn

#Function to read, filter, and return data by country code and crop
def getDataForPlot(data, country, crop):
    dataThndTonne = data[(data['Code'] == country) & (data['Subject'] == crop) & (data['Measure'] == 'THND_TONNE')]

    return dataThndTonne

#Call function to read data
dataIn = readData()

plCrop = "RICE"
plCountry = "AUS"

plotData = getDataForPlot(dataIn, plCountry, plCrop)


#Build visualizations and show plot
plX = plotData.Year
plY = plotData.Value
ax = plt.subplot()
ax.scatter(plX, plY, color = 'blue')
ax.plot(plX, plY, color = 'orange')
ax.set_title(plCrop.capitalize() + " Yield in " + plCountry.upper())
ax.set_xlabel("Crop Year")
ax.set_ylabel("Amount in Metric Tonnes")
ax.margins(0.1,0.1)
plt.show()
