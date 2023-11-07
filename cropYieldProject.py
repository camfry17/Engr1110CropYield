from cropYieldProject_Data import readData, getDataForPlot, getMetricDataForPlot
from cropYieldProject_Plot import buildPlot


#Call function to read data
prodData = readData("SOURCE_DATA/crop_production.csv")
ghiData = readData("SOURCE_DATA/global_hunger_index.csv")
underweightData = readData("SOURCE_DATA/children_underweight.csv")
heightWastingData = readData("SOURCE_DATA/children_weight_low_height_wasting.csv")
under5StuntingData = readData("SOURCE_DATA/children_under_5_stunting.csv")

plCrop = "RICE"
plCountry = "ARG"

#Call function to filter plot data
cropPlotData = getMetricDataForPlot(prodData, plCountry, plCrop)
ghiPlotData = getDataForPlot(ghiData, plCountry)
underPlotData = getDataForPlot(underweightData, plCountry)
wastingPlotData = getDataForPlot(heightWastingData, plCountry)
stuntingPlotData = getDataForPlot(under5StuntingData, plCountry)


buildPlot(cropPlotData, ghiPlotData, underPlotData, wastingPlotData, stuntingPlotData, plCountry, plCrop)