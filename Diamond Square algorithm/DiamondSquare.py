import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


from random import seed, uniform


def diamondStep(HM, r, force=None):
    """
    Input is height map.
    Adds a row between every row and a column between every column.
    Sets the intersection of each of these new things to the average of the
    corners plus a random amount.
    """
    n = len(HM)

    newHM = []
    for i in range(2*n-1):
        oldRowInd = i//2  # only applies to the even rows
        newRow = []
        for j in range(2*n-1):
            oldColInd = j//2  # only applies to the even collumns
            if i % 2 == 0 and j % 2 == 0:
                newRow.append(HM[oldRowInd][oldColInd])
            elif i % 2 == 1 and j % 2 == 1:
                avg = (HM[(i-1)//2][(j-1)//2] + HM[(i-1)//2][(j+1)//2] +
                       HM[(i+1)//2][(j-1)//2] + HM[(i+1)//2][(j+1)//2])/4

                newRow.append(avg+uniform(-1*r, r))
            else:
                newRow.append(0)

        newHM.append(newRow)

    if force is not None and n == 2:
        print("force")
        newHM[1][1] = force
        print(newHM[1][1])

    return newHM


def squareStep(HM, r):
    """
    Input is height map.
    Takes all the points ignored by diamond step (the centers of the new
    diamonds) and gives them an average + random value.
    Works in a way that allows wrapping. Each edge point is the same height
    as the point on the opposite side.
    """
    n = len(HM)

    # Don't look at the last row or column since I will already have assigned there.
    for i in range(n-1):
        for j in range(n-1):
            if (i % 2 == 1 and j % 2 == 0) or (i % 2 == 0 and j % 2 == 1):
                if HM[i][j] != 0:
                    print("error in assignment somewhere")

                s = 0
                if i == 0:
                    s += HM[n-2][j]  # i and n-1 are the same line
                else:
                    s += HM[i-1][j]

                if j == 0:
                    s += HM[i][n-2]
                else:
                    s += HM[i][j-1]

                s += HM[i+1][j]+HM[i][j+1]

                avg = s/4
                val = avg+uniform(-1*r, r)
                HM[i][j] = val

                if i == 0:
                    HM[n-1][j] = val
                if j == 0:
                    HM[i][n-1] = val

    return HM


if __name__ == "__main__":
    p = 7

    # seeded values
    heightMap = [[0, 0], [0, 0]]

    # random number start range
    r = 1
    # random number reduce ratio
    rr = .5

    for i in range(p):
        heightMap = diamondStep(heightMap, r)
        heightMap = squareStep(heightMap, r)
        r *= rr

    n = 2**p+1
    X = np.arange(0, n)
    Y = np.arange(0, n)
    X, Y = np.meshgrid(X, Y)

    Z = np.array(heightMap)
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='hot',
                           linewidth=0, antialiased=False)
    ax.set_zlim(-1.01, 1.01)

    fig.colorbar(surf, shrink=0.5, aspect=5)
    plt.show()
