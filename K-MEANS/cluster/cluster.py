import random
from Utils import distanceOfDataObjectAndCordinets

class cluster:

    listOfDataObject = None
    currentCentroid = None
    previousCentroid = None

    def __init__(self, i_listOfPoint=[]):
        self.listOfDataObject = i_listOfPoint
        self.currentCentroid = []
        self.previousCentroid = []

    def addDataObjectToCluster(self, i_Point):
        self.listOfDataObject.append(i_Point)

    def removeDataObjectFromCluster(self, i_Point):
        self.listOfDataObject.remove(i_Point)

    def countOfObjectsInCluster(self):
        return len(self.listOfDataObject)

    def getCentrozied(self):
        return self.currentCentroid

    def setCentrozied(self, listOfCordinets):
        self.currentCentroid = listOfCordinets
        self.previousCentroid = self.currentCentroid

    def getSSE(self):
        sumOfPowDistance = 0.0
        self.currentCentroid = self.calculateCentroid()
        for dataObj in self.listOfDataObject:
            sumOfPowDistance += pow(distanceOfDataObjectAndCordinets(self.currentCentroid, dataObj), 2)
        return sumOfPowDistance

    def calculateCentroid(self):
        sizeOfDataObject = len(self.currentCentroid)
        self.previousCentroid = self.currentCentroid
        listOfSumDimensions = []
        self.currentCentroid = []
        for i in range(0, sizeOfDataObject):
            listOfSumDimensions.append(sum([p.get_data()[i] for p in self.listOfDataObject]))
            self.currentCentroid.append(listOfSumDimensions[i] / len(self.listOfDataObject))
        return self.currentCentroid

    def getListOfElement(self):
        return self.listOfDataObject

    def erazeListOfElement(self):
        del self.listOfDataObject[:]
        self.previousCentroid = self.currentCentroid

    def getRandomCentersByDemand(self, k):
        maximumAmount = len(self.listOfDataObject)
        if k <= maximumAmount:
            return random.sample(self.listOfDataObject, k)
        else:
            return random.sample(self.listOfDataObject, maximumAmount)

    def checkEquivilantCentroid(self):
        self.calculateCentroid()
        if cmp(self.previousCentroid, self.currentCentroid) == 0:
            print "Equal"
            return True
        print "UnEqual"
        return False

    def has_object(self, dataObj):
        if dataObj in self.listOfDataObject:
            return 1
        return 0

