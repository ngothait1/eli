class Person:
    _name = None
    _age = None
    _id = None

    def __init__(self, id, name, age):
        self._id = id
        self._name = name
        self._age = age
    

    def getName(self):
        return self._name
    

    def setName(self, name):
        self._name = name
    

    def getAge(self):
        return self._age
    

    def setAge(self, age):
        self._age = age


    def getId(self):
        return self._id
    

    def setId(self, id):
        self._id = id


    def personToDict(self):
        return {"id": self.getId(), 
                "name": self.getName(), 
                "age": self.getAge()}

    
    def dictWrapper(self):
        return self.personToDict()


    def getPersonString(self):
        return str(self.getName()) + "'s id is " + str(self.getId()) + " and they are " + str(self.getAge()) +" years old"


    def printMyself(self):
        print(self.getPersonString())


if __name__ == "__main__":
    test_id = 101
    test_name = "Sam"
    test_age = 35
    person_1 = Person(test_id, test_name, test_age)
    if person_1.getId() != test_id:
        print("The ID should be " + str(test_id) + ", instead it's " + str(person_1.getId()))
    if person_1.getName() != test_name:
        print("The person's name should be " + test_name + ", instead it's " + str(person_1.getName()))
    if person_1.getAge() != test_age:
        print("The age should be " + str(test_age) + ", instead it's " + str(person_1.getAge()))