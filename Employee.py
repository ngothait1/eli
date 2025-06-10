from Person import Person
import util

class Employee(Person):
    def __init__(self, id, name, age, field_of_work = None, salary = None):
        super().__init__(id, name, age)
        if field_of_work == None:
            self._field_of_work = input("What is their field of work? ")
        else:
            self._field_of_work = field_of_work

        if field_of_work == None:
            self._salary = util.properInputValidator("salary")
        else:
            self._salary = salary


    def getFieldOfWork(self):
        return self._field_of_work
    

    def setFieldOfWork(self, field_of_work):
        self._field_of_work = field_of_work


    def getSalary(self):
        return self._salary
    

    def setSalary(self, new_salary):
        self._salary = new_salary

    
    def EmployeeToDict(self):
        return {"id": self.getId(), 
                "name": self.getName(), 
                "age": self.getAge(), 
                "Field Of Work": self.getFieldOfWork(), 
                "Salary": self.getSalary()}


    def dictWrapper(self):
        return self.EmployeeToDict()

    def printEmployee(self):
        print(self.getPersonString() + ", their field of work is " + self.getFieldOfWork() 
              + ", and their salary is " + str(self.getSalary()))
    

    def printMyself(self):
        self.printEmployee()

if __name__ == "__main__":
    test_id = 280
    test_name = "Alex"
    test_age = 47
    test_salary = 100000
    test_field_of_work = "Content Creator"
    employee1 = Employee(test_field_of_work, test_name, test_age, test_field_of_work, test_salary)
    if employee1.getId() != test_id:
        print("The ID should be " + str(test_id) + ", instead it's " + str(employee1.getId()))
    if employee1.getName() != test_name:
        print("The employee's name should be " + test_name + ", instead it's " + str(employee1.getName()))
    if employee1.getAge() != test_age:
        print("The age should be " + str(test_age) + ", instead it's " + str(employee1.getAge()))
    if employee1.getFieldOfWork() != test_field_of_work:
        print("The employee's field of work should be " + test_field_of_work + ", instead it's " + employee1.getFieldOfWork())
    if employee1.getSalary() != test_salary:
        print("The employee's salary should be " + str(test_salary) + ", instead it's " +str(employee1.getSalary()))