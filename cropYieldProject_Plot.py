import matplotlib.pyplot as plt
import numpy as np

def buildPlot(worldData, country, crop, shouldPhoto):
    #Initialize plot parameters, figure, and axes
    plt.rcParams['toolbar'] = 'None'
    plt.rcParams['figure.dpi'] = 109
    fig,axs = plt.subplots(2, layout = 'constrained')
    fig.set_figheight(7)
    fig.set_figwidth(10)

    if (crop.lower() == 'all' and country.lower() == 'all'):
        figTitle = ('Crop Yield Average vs. Hunger Index Worldwide')
    elif (crop.lower() == 'all'):
        figTitle = ("Overall Crop Yield vs. Hunger Index in " + country)
    elif (country.lower() == 'all'):
        figTitle = (crop.capitalize() + " Yield vs. Hunger Index Worldwide")
    else:
        figTitle = (crop.capitalize() + " Yield vs. Hunger Index in " + country)

    #Pull data into local variables and ignore datapoints with no values
    cYear = worldData.Year[np.isfinite(worldData.Value)]
    ghYear = worldData.Year[np.isfinite(worldData.Global_Hunger_Index_2021)]
    unYear = worldData.Year[np.isfinite(worldData.Prevalence_of_underweight_weight_for_age_percent_of_children_under_5)]
    wsYear = worldData.Year[np.isfinite(worldData.Prevalence_of_wasting_weight_for_height_percent_of_children_under_5)]
    stYear = worldData.Year[np.isfinite(worldData.Prevalence_of_stunting_height_for_age_percent_of_children_under_5)]
    cVal = worldData.Value[np.isfinite(worldData.Value)]
    ghVal = worldData.Global_Hunger_Index_2021[np.isfinite(worldData.Global_Hunger_Index_2021)]
    unVal = worldData.Prevalence_of_underweight_weight_for_age_percent_of_children_under_5[np.isfinite(worldData.Prevalence_of_underweight_weight_for_age_percent_of_children_under_5)]
    wsVal = worldData.Prevalence_of_wasting_weight_for_height_percent_of_children_under_5[np.isfinite(worldData.Prevalence_of_wasting_weight_for_height_percent_of_children_under_5)]
    stVal = worldData.Prevalence_of_stunting_height_for_age_percent_of_children_under_5[np.isfinite(worldData.Prevalence_of_stunting_height_for_age_percent_of_children_under_5)]

    #Set up plots for crop yield graph
    axs[0].grid(True, color = '#eeeeee')
    axs[0].scatter(cYear, cVal, color = '#6666ff', zorder = 2.5)
    axs[0].plot(cYear, cVal, color = '#6666ff', zorder = 2.5)
    axs[0].set_ylabel("Amount in Metric Tonnes")
    axs[0].margins(0.1, 0.1)

    #Set up plots for global hunger graph
    axs[1].grid(True, color = '#eeeeee')
    axs[1].scatter(ghYear, ghVal, color = '#0033ff', label = 'Hunger Index', zorder = 2.5)
    axs[1].scatter(unYear, unVal, color = '#fca000', label = 'Children underweight', zorder = 2.5)
    axs[1].scatter(wsYear, wsVal, color = '#02d63e', label = 'Wasting weight for height', zorder = 2.5)
    axs[1].scatter(stYear, stVal, color = '#de0404', label = 'Stunting height for age', zorder = 2.5)
    axs[1].plot(ghYear, ghVal, color = '#0033ff', zorder = 2.5)
    axs[1].plot(unYear, unVal, color = '#fca000', zorder = 2.5)
    axs[1].plot(wsYear, wsVal, color = '#02d63e', zorder = 2.5)
    axs[1].plot(stYear, stVal, color = '#de0404', zorder = 2.5)
    axs[1].set_ylabel("Percentage of Population")
    axs[1].margins(0.1, 0.1)

    legend = axs[1].legend(loc = 'best', shadow = False, fontsize = 9, facecolor = '#dddddd', edgecolor = '#dddddd')
    legend.get_frame()

    #Set up Figure Attributes
    fig.suptitle(figTitle)
    fig.supxlabel("Year")
    fig.align_ylabels()
    fig.canvas.manager.set_window_title(figTitle)

    if (shouldPhoto == 1):
        plt.savefig('output.png')

    plt.show()