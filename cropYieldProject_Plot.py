import matplotlib.pyplot as plt

def buildPlot(data, country, crop):
    plX = data.TIME
    plY = data.Value
    ax = plt.subplot()
    ax.scatter(plX, plY, color = 'blue')
    ax.plot(plX, plY, color = 'orange')
    ax.set_title(crop.capitalize() + " Yield in " + country.upper())
    ax.set_xlabel("Crop Year")
    ax.set_ylabel("Amount in Metric Tonnes")
    ax.margins(0.1,0.1)
    plt.show()