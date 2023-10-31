from cropYieldProject_DataFunctions import readData, getDataForPlot
from cropYieldProject_Plot import buildPlot

#Call function to read data
prodData = readData("SOURCE_DATA/crop_production.csv")
ghiData = readData("SOURCE_DATA/global_hunger_index.csv")
underweightData = readData("SOURCE_DATA/children_underweight.csv")
heightWastingData = readData("SOURCE_DATA/children_weight_low_height_wasting.csv")
under5StuntingData = readData("SOURCE_DATA/children_under_5_stunting.csv")

plCrop = "RICE"
plCountry = "KOR"

plotData = getDataForPlot(prodData, plCountry, plCrop)

buildPlot(plotData, plCountry, plCrop)