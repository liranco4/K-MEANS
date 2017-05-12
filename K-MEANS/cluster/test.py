import random
#determine how many data dimentions will be in each of the data objects, 
#please note that all of the data objects are consistent in thier dims

n = random.randint(1,100)

class data_object:
    def __init__(self, n):
        """
        will init self.data as a list of data
        :param n: how many dimensions i have?
        """
        import random
        self.data = [random.randint(1,1000) for i in range(n)]

    def get_data(self):
        """

        :return: return the data as a simple list of numbers
        """
        return self.data

    def __str__(self):
        return str(self.data)

def generate_data():
    """

    :return: will return a list of data objects
    """
    how_much_data = random.randint(10,100)
    return [data_object(n) for i in range(how_much_data)]

if __name__ == "__main__":
    #this is a simple example of how to use this script to generate data for you to test your scripts.
    print generate_data()
