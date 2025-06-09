from Person import Person
from Employee import Employee
from Student import Student

def saveNewEntry(user_data, id_index_list):
    given_id = input("ID: ")
    if not given_id.isdigit():
        wrongInputError("ID", given_id)
        return False
    if given_id in user_data:
        print("Error: ID already exists: " + str(user_data[given_id]))
        return False
    
    given_name = input("Name: ")
    given_age = input("Age: ")
    if not given_age.isdigit():
        wrongInputError("Age", given_age)
        return False
    
    printMenu(False)
    user_choice = input("Please enter your choice: ")
    if user_choice == "1":
        field_of_study = input("What is their field of study? ")
        year_of_study = input("How long have they been a student? ")
        if not year_of_study.isdigit():
            wrongInputError("year of study", year_of_study)
            return False
        student_avg = input("What is their avarage? ")
        if not student_avg.isdigit():
            wrongInputError("studnet avarage", student_avg)
            return False
        user_data[given_id] = Student(given_id, given_name, given_age, field_of_study, year_of_study, student_avg)
    elif user_choice == "2":
        field_of_work = input("What is their field of work? ")
        salary = input("What is their salary? ")
        if not salary.isdigit():
            wrongInputError("salary", salary)
            return False
        user_data[given_id] = Employee(given_id, given_name, given_age, field_of_work, salary)
    else:
        user_data[given_id] = Person(given_id, given_name, given_age)
        print("Saved as a regular person.")
    id_index_list.append(given_id)
    print("ID [" + given_id + "] saved successfully")
    return True
    
def extractAgeForSum(user_data, id_index_list):
    saved_id = id_index_list[len(id_index_list) -1]
    user_entry = user_data[saved_id]
    return int(user_entry.getAge())

def searchById(user_data):
    given_id = input("Please enter the ID you want to look for: ")
    if not given_id.isdigit():
        wrongInputError("ID", given_id)
    elif given_id not in user_data:
        print("Error: ID " + given_id + " not saved")
    else:
        user_entry = user_data[given_id]
        printEntry(user_entry)

def printAgesAverage(sum_before_divide, divide_by):
    if sum_before_divide == 0:
            print("0")
    else:
        print(sum_before_divide/divide_by)

def printAllNames(user_data, user_size):
    if user_size != 0:
        for index, id in enumerate(user_data):
            user_entry = user_data[id]
            print(str(index) + ". " + user_entry.getName())

def printAllIds(user_data, user_size):
    if  user_size != 0:
        for index, id in enumerate(user_data):
            print(str(index) + ". " + id) # Is there a better way to do this using the instances stored in my dictionary?

def printAllEntries(user_data, user_size):
    if user_size != 0:
        for index, id in enumerate(user_data):
            user_entry = user_data[id]
            printEntryList(index, user_entry)

def printEntryByIndex(user_data, id_index_list):
    user_input = input("Please enter the index of the entry you want to print: ")
    if not user_input.isdigit():
        wrongInputError("index", user_input)
    elif int(user_input) >= len(user_data) or int(user_input) < 0:
        print("Error: Index out of range. The maximum index allowed is " +str(len(user_data) - 1))
    else:
        retrieved_id = id_index_list[int(user_input)]
        user_entry = user_data[retrieved_id]
        printEntry(user_entry)
       

def printMenu(flag):
    if flag:
        print("1. Save a new entry")
        print("2. Search by ID")
        print("3. Print ages average")
        print("4. Print all names")
        print("5. Print all IDs")
        print("6. Print all entries")
        print("7. Print entry by index")
        print("8. Print people's information")
        print("9. Exit")
    else:
        print("Press 1 to save a student")
        print("Press 2 to save an employee")


def wrongInputError(what_was_wrong, wrong_input_given):
    print("Error: " + what_was_wrong + " must be a number. " + wrong_input_given + " is not a number")

def printEntryList(index, user_entry):
    print(str(index) + ". " + user_entry.getId())
    print("   Name: " + user_entry.getName())
    print("   Age: " + user_entry.getAge())

def printEntry(user_entry):
    print("ID: " + user_entry.getId())
    print("Name: " + user_entry.getName())
    print("Age: " + user_entry.getAge())


def printPeopleData(user_data):
    for person in user_data.values():
        person.printMyself()

       
def toExitOrNotExit(): 
    while True:
        user_choice = input("Are you sure? (y/n) ")
        if user_choice.lower() in ["y", "yes"]:
            print("Goodbye!")
            return False
        elif user_choice.lower() in ["n", "no"]:
            return True
       
       
def main():
    # collection of global variables and data structures
    age_sum_before_averaging = 0
    id_index_list = []
    user_data = {}
    running_flag = True
    while running_flag:
        printMenu(True) # TODO need to add if a person it just a person, studnet or employee
        user_choice = input("Please enter your choice: ")
        if user_choice == "1":
            save_success = saveNewEntry(user_data, id_index_list)
            if save_success:
                given_age = extractAgeForSum(user_data, id_index_list)
                age_sum_before_averaging += given_age

        elif user_choice == "2":
            searchById(user_data)

        elif user_choice == "3":
            printAgesAverage(age_sum_before_averaging, len(id_index_list))

        elif user_choice == "4":
            printAllNames(user_data, len(user_data))

        elif user_choice == "5":
            printAllIds(user_data, len(user_data))

        elif user_choice == "6":
            printAllEntries(user_data, len(user_data))

        elif user_choice == "7":
            printEntryByIndex(user_data, id_index_list)

        elif user_choice =="8":
            printPeopleData(user_data)

        elif user_choice == "9":
            running_flag = toExitOrNotExit()

        else: 
            print("Error: Option [" + user_choice + "] does not exist. Please try again.")

        if running_flag:
            input("Press Enter to continue")

main()