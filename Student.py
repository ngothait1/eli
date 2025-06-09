from Person import Person

class Student(Person):
    def __init__(self, id, name, age, field_of_study, year_of_study, grade_avg):
        super().__init__(id, name, age)
        self._field_of_study = field_of_study
        self._year_of_study = year_of_study
        self._grade_avg = grade_avg
    

    def getFieldOfStudy(self):
        return self._field_of_study
    

    def setFieldOfStudy(self, field):
        self._field_of_study = field
    
    
    def getYearOfStudy(self):
        return self._year_of_study
    

    def setYearOfStudy(self, year):
        self._year_of_study = year


    def getGradeAvg(self):
        return self._grade_avg
    

    def setGradeAvg(self, avg):
        self._grade_avg = avg

    
    def printStudent(self):
        print(self.getPersonString() + ", their field of study is " + self.getFieldOfStudy() 
              + ", they are in year " + str(self.getYearOfStudy()) + ", their avarage is " + str(self.getGradeAvg()))
        

    def printMyself(self):
        self.printStudent()