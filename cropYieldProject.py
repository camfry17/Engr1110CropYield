from cropYieldProject_Data import readData, getHungerDataForPlot, getMetricDataForPlot, getWorldHungerDataForPlot
from cropYieldProject_Plot import buildPlot
from tkinter import ttk
from tkinter import *
import platform

def doThings(country, crop, shouldExcel, shouldPhoto):
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
    buildPlot(outputData, country, crop, shouldPhoto)

#Enable DPI Awareness (only applies to windows systems)
if (platform.system() == 'Windows'):
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
    windll.user32.SetProcessDPIAware()

#Initialize GUI
root = Tk()
root.geometry("500x250+400+300")
root.title("ENGR 1110")

#Define variables connected to GUI widgets
ctSel = StringVar()
cpSel = StringVar()
exSel = IntVar()
opSel = IntVar()

#Build title label
titleLabel = ttk.Label(master = root, justify = 'center', text = 'Select a crop and enter a country.\nLeave country blank for world average.')
titleLabel.place(relx = 0.5, rely = 0, y = 5, anchor = 'n')

#Build Combobox for crop selection
cropPickerLabel = ttk.Label(master = root, justify = 'center', text = 'Crop Type')
cropPickerLabel.place(relx = 0.32, rely = 0.22, anchor = 'n')

cropPicker = ttk.Combobox(master = root, textvariable = cpSel)
cropPicker['values'] = ('All', 'Rice', 'Maize', 'Soybean', 'Wheat')
cropPicker.place(relx = 0.60, rely = 0.22, width = 125, anchor = 'n')
cropPicker.current(0)

#Build entry box for country
countryEntryLabel = ttk.Label(master = root, text = 'Country')
countryEntryLabel.place(relx = 0.32, rely = 0.38, anchor = 'n')

countryEntry = ttk.Entry(master = root, textvariable = ctSel, justify = 'center')
countryEntry.place(relx = 0.60, rely = 0.38, width = 125, anchor = 'n')

#Build checkbox to toggle excel export
shouldExcel = ttk.Checkbutton(master = root, variable = exSel, style = 'primary.TCheckbutton', text = 'Export excel file')
shouldExcel.place(relx = 0.67, rely = 0.54, anchor = 'n')

shouldPhoto = ttk.Checkbutton(master = root, variable = opSel, style = 'primary.TCheckbutton', text = 'Export output photo')
shouldPhoto.place(relx = 0.34, rely = 0.54, anchor = 'n')

#Build button to call program
actButton = ttk.Button(master = root, style = 'primary.TButton', text = 'Run', command = lambda: doThings(ctSel.get().upper(), cpSel.get().upper(), exSel.get(), opSel.get()))
actButton.place(relx = 0.35, rely = 0.69, anchor = 'n')

#Build button to kill program
killButton = ttk.Button(master = root, style = 'danger.TButton', text = 'Quit', command = lambda: root.quit())
killButton.place(relx = 0.65, rely = 0.69, anchor = 'n')

#Run GUI
root.mainloop()