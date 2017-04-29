
#class main:

#     @staticmethod
#     def getRandomListOfXYaxises(amountOfPatients):
#
#         listOfXY = []
#         dictOfGeneratedNumbers = {}
#         amount = 0
#         while amount < amountOfPatients:
#             genNumber = randint(10, 99)
#             while genNumber in dictOfGeneratedNumbers:
#                 genNumber = randint(100, 299)
#             listOfXY.append((genNumber / 10, genNumber % 10))
#             dictOfGeneratedNumbers[genNumber] = genNumber
#             amount += 1
#         return listOfXY
#
# listOfNamesAndAge = []
# for p in gen.generate():
#     listOfNamesAndAge.append((p.get_name(), p.get_age()))
# amountOfPatients = len(listOfNamesAndAge)
#
# listOfXY = main.getRandomListOfXYaxises(amountOfPatients)
# dictionary = dict(zip(listOfXY, listOfNamesAndAge))
# copyOfOrigin = dictionary
#
# listOfClusters = [cluster.cluster([]), cluster.cluster([]), cluster.cluster([]), cluster.cluster([])]
# amount = 0
# while amount < amountOfPatients:
#     randomCluster = random.choice(listOfClusters)
#     randomKeyValue = random.choice(list(dictionary.items()))
#     dictionary.pop(randomKeyValue[0])
#     point1 = point.point(randomKeyValue[0][0], randomKeyValue[0][1])
#     randomCluster.addPointToCluster(point1)
#     amount += 1
#
# for c in listOfClusters:
#     for p in c.listOfPoint:
#         print p.getCordinate()
#     print "centroid of cluster is: ", c.getCentrozied().getCordinate(), "SSE is: ", c.getSSE()


print 1
d = sum(z+f for z in [1,1,1] for f in [1])
print d

print min(s[0] for s in [(9,8),(3,4)])
