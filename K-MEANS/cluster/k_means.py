import random
import test
import cluster
from Utils import distanceOfDataObjectAndCordinets

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
        if not clusterObj.checkEquivilantCentroid():
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
for c in list:
    print c.getSSE()
    list1 = c.getRandomCentersByDemand(3)
    for v in list1:
        print v.get_data()
    s = c.getListOfElement()[0]
    if c.has_object(s) == 1:
        print "sucess"

