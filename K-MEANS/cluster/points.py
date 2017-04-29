import imp
modl = imp.load_source('test', '/generators/test.py')
class points:
    listOfGenerateData = None

    def __init__(self):
        self.listOfGenerateData = modl.generate_data()

    # @staticmethod
    # def distance(i_dataObject, ):
    #     for d1,d2 in zip()
    #     return math.sqrt((pow((self.x-i_p.x), 2)+pow((self.y-i_p.y), 2)))

    def getCordinate(self):
        return self.x, self.y




