import math
def distanceOfDataObjectAndCordinets(listOfCordintes, dataObject):
    try:
        assert len(listOfCordintes) == len(dataObject.get_data()),"length of listOfCordintes: {} doesn't equal to length of dataObject: {}".format(len(listOfCordintes),len(dataObject.get_data()))
    except Exception:
        print "error"
    dist = 0
    for i, j in zip(listOfCordintes, dataObject.get_data()):
        dist += math.sqrt((pow((i - j), 2)))
    return dist