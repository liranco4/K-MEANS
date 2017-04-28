import random

import points


class cluster:

    listOfPoint = [None]
    centroied = None
    def __init__(self, i_listOfPoint):
        self.listOfPoint = i_listOfPoint

    def addPointToCluster(self, i_Point):
        self.listOfPoint.append(i_Point)
        self.centroied = self.calculateCentroid

    def removePointFromCluster(self, i_Point):
        self.listOfPoint.remove(i_Point)
        self.centroied = self.calculateCentroid

    def countOfObjectsInCluster(self):
        return len(self.listOfPoint)

    def getCentrozied(self):
        self.centroied = self.calculateCentroid()
        return self.centroied

    def getSSE(self):
        sumOfPowDistance = 0.0
        self.centroied = self.calculateCentroid()
        for point in self.listOfPoint:
            sumOfPowDistance += pow(point.distance(self.centroied), 2)
        return sumOfPowDistance

    def calculateCentroid(self):
        x = [p.x for p in self.listOfPoint]
        y = [p.y for p in self.listOfPoint]
        return points.point(sum(x) / len(self.listOfPoint), sum(y) / len(self.listOfPoint))

    def getListOfElement(self):
        return self.listOfPoint

    def getRandomCentersByDemand(self, k):
        newRandomPoints = [None]
        while k > 0:
            k -= 1
            newRandomPoints.append(random.choice(self.listOfPoint))
        return newRandomPoints

