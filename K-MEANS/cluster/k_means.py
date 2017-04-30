import random
import test
import cluster
import math


def run(listOfDataObjects, numberOfClusters):
    listOfClusters = createMultipleClusterInList(numberOfClusters)
    genratedRandomDataObject = random.sample(listOfDataObjects, numberOfClusters)
    for clusterObj, centObj in zip(listOfClusters, genratedRandomDataObject):
        clusterObj.setCentrozied(centObj.get_data())
    runK_MEANSUntilCentroidStable(listOfClusters, listOfDataObjects)
    return listOfClusters

def createMultipleClusterInList(numberOfClusters):
    listOfClusters = []
    for i in range(0, numberOfClusters):
        listOfClusters.append(cluster.cluster([]))
    return listOfClusters


def distanceOfDataObjectAndCordinets(listOfCordintes, dataObject):
    try:
        assert len(listOfCordintes) == len(dataObject.get_data()),"length of listOfCordintes: {} doesn't equal to length of dataObject: {}".format(len(listOfCordintes),len(dataObject.get_data()))
    except Exception:
        print "error"
    dist = 0
    for i, j in zip(listOfCordintes, dataObject.get_data()):
        dist += math.sqrt((pow((i - j), 2)))
    return dist

# assignDataObjectToNearestCluster: True when succeeded otherwise False
def assignDataObjectToNearestCluster(listOfClusters, dataObject):
    listOftupleClustersAndDistance = []
    for clusterObj in listOfClusters:
        if len(clusterObj.getCentrozied())==0:
            print 1
        dist = distanceOfDataObjectAndCordinets(clusterObj.getCentrozied(), dataObject)
        listOftupleClustersAndDistance.append((clusterObj, dist))
    minDistance = min(distance[1] for distance in listOftupleClustersAndDistance)
    for tuple in listOftupleClustersAndDistance:
        if minDistance == tuple[1]:
            tuple[0].addDataObjectToCluster(dataObject)
            return True
    return False

# if one of the cluster centroid was changed: return True, otherwise return False
def checkIfCentroidWasChangedInAllClusters(listOfClusters):
    centroidWasChanged = False
    for clusterObj in listOfClusters:
        if clusterObj.checkEquivilantCentroid() == False:
            centroidWasChanged = True
    return centroidWasChanged

def runK_MEANSUntilCentroidStable(listOfClusters, listOfDataObjects):
    for dataObject in listOfDataObjects:
        assignDataObjectToNearestCluster(listOfClusters, dataObject)
    while checkIfCentroidWasChangedInAllClusters(listOfClusters):
        for clusterObj in listOfClusters:
            clusterObj.erazeListOfElement()
        for dataObject in listOfDataObjects:
            assignDataObjectToNearestCluster(listOfClusters, dataObject)

list = run(test.generate_data(), 3)
print list
dist = 0
print dist