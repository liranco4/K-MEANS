import random

class patient:
    name = None
    id = None
    age = None

    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_id(self):
        return self.id


def generate():

    names = ["yosi", "roni", "moshe"]
    patients = []

    for i in range(100):
        name = random.choice(names)
        id = [random.randint(0,9) for i in range(9)]
        id = "".join(str(j) for j in id)
        age = random.randint(1,100)
        patients.append(patient(id,name,age))

    return patients
