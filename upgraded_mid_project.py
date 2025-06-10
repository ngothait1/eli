from Person import Person
from Employee import Employee
from Student import Student
import pandas as pd
import util


def saveNewEntry(user_data, id_index_list):
    given_id = util.properInputValidator("ID")
    if given_id in user_data:
        print("Error: ID already exists: " + str(user_data[given_id].dictWrapper()))
        return False
    given_name = input("Name: ")
    given_age =  util.properInputValidator("age")
    util.printPersonMenu()
    user_choice = input("Please enter your choice: ")
    if user_choice == "1":
        new_person = Student(given_id, given_name, given_age)
    elif user_choice == "2":
        new_person = Employee(given_id, given_name, given_age)
    else:
        new_person = Person(given_id, given_name, given_age)
        print("Saved as a regular person.")
    user_data[given_id] = new_person
    id_index_list.append(given_id)
    print("ID [" + str(given_id) + "] saved successfully")
    return True
    
def extractAgeForSum(user_data, id_index_list):
    saved_id = id_index_list[-1] # Supposed to access the last element in the array.
    user_entry = user_data[saved_id]
    return int(user_entry.getAge())

def searchById(user_data):
    given_id = util.properInputValidator("ID search")
    if given_id not in user_data:
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
            print(str(index) + ". " + user_data[id].getId()) # Is there a better way to do this using the instances stored in my dictionary?

def printAllEntries(user_data, user_size):
    if user_size != 0:
        for person in user_data.values():
            person.printMyself()


def printEntryByIndex(user_data, id_index_list):
    user_input = util.properInputValidator("index to print")
    if int(user_input) >= len(user_data) or int(user_input) < 0:
        print("Error: Index out of range. The maximum index allowed is " +str(len(user_data) - 1))
    else:
        retrieved_id = id_index_list[int(user_input)]
        user_entry = user_data[retrieved_id]
        printEntry(user_entry)
       

def printMenu():
    print("1. Save a new entry")
    print("2. Search by ID")
    print("3. Print ages average")
    print("4. Print all names")
    print("5. Print all IDs")
    print("6. Print all entries")
    print("7. Print entry by index")
    print("8. Save all data")
    print("9. Exit")


def printEntry(user_entry):
    user_entry.printMyself()


def saveAllData(user_data):
    file_name = input("What is your output file name? ")
    if not file_name.endswith(".csv"):
        file_name += ".csv"
        print("adding .csv extension")
    
    headers = []
    for user_id in user_data:
        person_entry = user_data[user_id]
        dict_form_entry = person_entry.dictWrapper()
        for key in dict_form_entry.keys():
            if not key in headers:
                headers.append(key)
                
    csv_format_data = []
    for id in user_data:
        person = user_data[id]
        person_dict = person.dictWrapper()
        prep_entry_for_export = {key: person_dict.get(key, None) for key in headers}
        csv_format_data.append(prep_entry_for_export)
    df = pd.DataFrame(csv_format_data)
    df = df[headers]
    df.fillna(0, inplace=True)
    df.to_csv(file_name, index=False)

       
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
        printMenu()
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


        elif user_choice == "8":
            saveAllData(user_data)

        elif user_choice == "9":
            running_flag = toExitOrNotExit()

        else: 
            print("Error: Option [" + user_choice + "] does not exist. Please try again.")

        if running_flag:
            input("Press Enter to continue")

main()