from Person import Person

class Employee(Person):
    def __init__(self, id, name, age, field_of_work, salary):
        super().__init__(id, name, age)
        self._field_of_work = field_of_work
        self._salary = salary


    def getFieldOfWork(self):
        return self._field_of_work
    

    def setFieldOfWork(self, field_of_work):
        self._field_of_work = field_of_work


    def getSalary(self):
        return self._salary
    

    def setSalary(self, new_salary):
        self._salary = new_salary

    
    def printEmployee(self):
        print(self.getPersonString() + ", their field of work is " + self.getFieldOfWork() 
              + ", and their salary is " + str(self.getSalary()))
    

    def printMyself(self):
        self.printEmployee()