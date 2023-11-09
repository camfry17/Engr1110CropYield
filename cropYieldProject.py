from cropYieldProject_Data import readData, getHungerDataForPlot, getMetricDataForPlot, getWorldHungerDataForPlot
from cropYieldProject_Plot import buildPlot


#Call function to read data
prodData = readData("SOURCE_DATA/crop_production.csv")
ghiData = readData("SOURCE_DATA/global_hunger_index.csv")
underweightData = readData("SOURCE_DATA/children_underweight.csv")
heightWastingData = readData("SOURCE_DATA/children_weight_low_height_wasting.csv")
under5StuntingData = readData("SOURCE_DATA/children_under_5_stunting.csv")

plCrop = "RICE"
plCountry = "ARG"

#Call function to filter plot data with country parameter
cropPlotData = getMetricDataForPlot(prodData, plCountry, plCrop)
ghiPlotData = getHungerDataForPlot(ghiData, plCountry)
underPlotData = getHungerDataForPlot(underweightData, plCountry)
wastingPlotData = getHungerDataForPlot(heightWastingData, plCountry)
stuntingPlotData = getHungerDataForPlot(under5StuntingData, plCountry)

#NOT WORKING
#getWorldHungerDataForPlot(ghiData)

buildPlot(cropPlotData, ghiPlotData, underPlotData, wastingPlotData, stuntingPlotData, plCountry, plCrop)