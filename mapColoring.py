import plotly.express as px
import numpy as matrix

countries = ["Argentina", "Bolivia", "Brazil", "Chile", "Colombia", "Ecuador", "Falkland Islands", "Guyana", "Paraguay",
             "Peru", "Suriname", "Uruguay", "Venezuela"]

colors = ["blue", "green", "red", "yellow"]


def readData(input):
    rawData = matrix.zeros((len(countries), len(countries)))
    with open(input) as datafile:
        next(datafile)
        i = -1
        for line in datafile.read().splitlines():
            i += 1
            list = line.split(",")
            for item in countries:
                if item in list:
                    rawData[i][countries.index(item)] = 1

    return rawData


def check(colorIndex, areaIndex, graph, areaColors):
    for borderIndex in range(len(countries)):
        if graph[areaIndex][borderIndex] == 1 \
                and countries[borderIndex] in areaColors \
                and colors[colorIndex] == areaColors[countries[borderIndex]]:
            return False
    return True


def mapColoring(counter, data, areaColors):
    for insideCounter, value in enumerate(colors):
        if check(insideCounter, counter, data, areaColors):
            areaColors[countries[counter]] = colors[insideCounter]
            return

def plot_choropleth(colormap):
  fig=px.choropleth(locationmode="country names",
                  locations=countries,
                  color=countries,
                  color_discrete_sequence=[colormap[c] for c in countries],
                  scope="south america")
  fig.show()

if __name__ == "__main__":
    data = readData("SouthAmerica.csv")
    areaColors = dict()
    for index in range(len(countries)):
        mapColoring(index, data, areaColors)
    plot_choropleth(areaColors)
    # coloring test
    colormap_test = {"Argentina": "blue", "Bolivia": "red", "Brazil": "yellow", "Chile": "yellow", "Colombia": "red",
                     "Ecuador": "yellow", "Falkland Islands": "yellow", "Guyana": "red", "Paraguay": "green",
                     "Peru": "green", "Suriname": "green", "Uruguay": "red", "Venezuela": "green"}

    # plot_choropleth(colormap=colormap_test)
