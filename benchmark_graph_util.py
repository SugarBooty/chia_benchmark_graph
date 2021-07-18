"""
This is a quick program makde to graph data from benchmarking Chia parameters.
It accepts data in the form of CSV files as follows:
THREADS,BUCKETS,DURATION
"""

from matplotlib.colors import Normalize
import matplotlib.pyplot as plt
from matplotlib import cm

def readFromFile(filePath: str) -> list:
    with open(filePath) as f:
        content = f.read().splitlines()
    return content

# converts the list formatted "T,B,D" into lists of T, B, and D
# returns a tuple of the lists
def extrapolateData(data: list) -> tuple:
    x = []
    y = []
    z = []
    for entry in data:
        T, B, D = entry.split(',')
        x.append(int(T))
        y.append(int(B))
        z.append(float(D))
    return (x, y, z)

def dedupeList(input: list) -> list:
    # dicts cant have duplicate keys, so I convert the list into one and then back to remove duplicates
    return list(dict.fromkeys(input))

def makeGraph(data: list, data2: list = []) :
    x1, y1, z1 = data

    if (data2 != []):
        x2, y2, z2 = data2

#   Configure matplotlib for 3d graphing
    fig = plt.figure()
    ax = plt.axes(projection ='3d')

    '''
    here is where the data is specified

    x, y, z is self explanitory, they are the 1d arrays containing the data
    cmap is the color map used. To choose a different one look up "matplotlib how to choose a colormap"
    norm makes the colormap corelate to the z axis. it makes it easier to read the graph
    edgecolor is also self explanitory, I made the edges black
    alpha lets you set the opacity of a graph. it needs to be within 0 and 1
    '''

    ax.plot_trisurf(x1, y1, z1, cmap=cm.bwr, norm=Normalize(), edgecolor = "black", alpha=0.8)

    if (data2 != []):
        ax.plot_trisurf(x2, y2, z2, cmap=cm.bwr, norm=Normalize(), edgecolor = "black")

    ax.set_xticks(dedupeList(x1))
    ax.set_yticks(dedupeList(y1))

    plt.show()

# tiny bit messy shhh
content1 = extrapolateData(readFromFile("benchmarkNoRaidCut"))
content2 = extrapolateData(readFromFile("benchmarkRaidCut"))

# content2 can be ommitted to show only one graph

makeGraph(content1, content2)
