from matplotlib import collections as mc
from matplotlib import pyplot as plt

from random import seed, uniform
# seed(35484)


def addMidpoints(points, r):
    newPoints = []
    for i in range(len(points)):
        newPoints.append(points[i])

        if i < len(points)-1:  # no line segment after last point
            midx = (points[i][0]+points[i+1][0])/2
            midy = (points[i][1]+points[i+1][1])/2

            newPoints.append((midx, midy+uniform(-1*r, r)))

    return newPoints


def display(points):
    lines = []
    for i in range(len(points)-1):
        lines.append([points[i], points[i+1]])

    lc = mc.LineCollection(lines, linewidths=2)
    fig, ax = plt.subplots()
    ax.add_collection(lc)
    ax.autoscale()
    ax.margins(0.1)
    plt.show()


if __name__=="__main__":
    # number of displacements
    N = 14

    # x,y values of points
    points = [(-1.0, 0.0), (1.0, 0.0)]

    # random number start range
    r = 1
    # random number reduce ratio
    rr = .5

    for i in range(N):
        points = addMidpoints(points, r)
        r *= rr

    display(points)
