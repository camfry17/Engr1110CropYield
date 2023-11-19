from cropYieldProject_Data import readData, getHungerDataForPlot, getMetricDataForPlot, getWorldHungerDataForPlot
from cropYieldProject_Plot import buildPlot
from ctypes import windll
from tkinter import ttk
from tkinter import *

def doThings(country, crop, shouldExcel):
    #Call function to read data
    prodData = readData("SOURCE_DATA/crop_production.csv")
    ghiData = readData("SOURCE_DATA/global_hunger_index.csv")
    underweightData = readData("SOURCE_DATA/children_underweight.csv")
    heightWastingData = readData("SOURCE_DATA/children_weight_low_height_wasting.csv")
    under5StuntingData = readData("SOURCE_DATA/children_under_5_stunting.csv")

    #Call function to filter plot data with country parameter
    cropPlotData = getMetricDataForPlot(prodData, country, crop)
    ghiPlotData = getHungerDataForPlot(ghiData, country)
    underPlotData = getHungerDataForPlot(underweightData, country)
    wastingPlotData = getHungerDataForPlot(heightWastingData, country)
    stuntingPlotData = getHungerDataForPlot(under5StuntingData, country)

    #Combines dataframes from each dataset and returns based on specified inputs
    outputData = getWorldHungerDataForPlot(cropPlotData, ghiPlotData, underPlotData, wastingPlotData, stuntingPlotData, shouldExcel)

    #Passes all datasets to build plot and show data on the plot
    buildPlot(outputData, country, crop)

#Enable DPI Awareness for high DPI screens
windll.shcore.SetProcessDpiAwareness(1)
windll.user32.SetProcessDPIAware()

#Initialize GUI
root = Tk()
root.geometry("500x400+400+300")
root.title("ENGR 1110")

#Define widget styles ---FIX LATER---
#style = ttk.Style()

#Define variables connected to GUI widgets
ctSel = StringVar()
cpSel = StringVar()
exSel = IntVar()

#Build title label
titleLabel = ttk.Label(master = root, justify = 'center', text = 'Select a crop and enter a country\nEnter \'all\' in textbox for world average')
titleLabel.place(relx = 0.5, rely = 0, y = 5, anchor = 'n')

#Build Combobox for crop selection
cropPicker = ttk.Combobox(master = root, textvariable = cpSel)
cropPicker['values'] = ('All', 'Rice', 'Maize', 'Soybean', 'Wheat')
cropPicker.place(relx = 0.5, rely = 0.15, width = 125, anchor = 'n')
cropPicker.current(0)

#Build entry box for country
countryEntry = ttk.Entry(master = root, textvariable = ctSel, justify = 'center')
countryEntry.place(relx = 0.5, rely = 0.25, width = 75, anchor = 'n')

#Build checkbox to toggle excel export
shouldExport = ttk.Checkbutton(master = root, variable = exSel, style = 'primary.TCheckbutton', text = 'Export excel file')
shouldExport.place(relx = 0.5, rely = 0.33, anchor = 'n')

#Build button to call program
actButton = ttk.Button(master = root, style = 'primary.TButton', text = 'Run', command = lambda: doThings(ctSel.get().upper(), cpSel.get().upper(), exSel.get()))
actButton.place(relx = 0.5, rely = 0.45, anchor = 'center')

#Build button to kill program
killButton = ttk.Button(master = root, style = 'danger.TButton', text = 'Quit', command = lambda: root.quit())
killButton.place(relx = 0.5, rely = 0.55, anchor = 'center')

#Run GUI
root.mainloop()