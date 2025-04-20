def saveNewEntry(given_id, user_data, id_index_list):
    given_name = input("Name: ")
    given_age = input("Age: ")
    age_sum_before_averaging += int(given_age)
    user_data[given_id] = {"name" : given_name, "age" : given_age}
    id_index_list.append(given_id)
    print("ID [" + given_id + "] saved successfully")

def searchById(id_to_search, user_data):
    user_entry = user_data[id_to_search]
    printEntry(id_to_search, user_entry)

def printAgesAverage(sum_before_divide, divide_by):
    if sum_before_divide == 0:
            print("0")
    else:
        print(sum_before_divide/divide_by)

def printAllNames(user_data, user_size):
    if user_size != 0:
        for index, id in enumerate(user_data):
            user_entry = user_data[id]
            print(str(index) + ". " + user_entry["name"])

def printAllIds(user_data, user_size):
    if  user_size != 0:
        for index, id in enumerate(user_data):
            print(str(index) + ". " + id)

def printAllEntries(user_data, user_size):
    if user_size != 0:
        for index, id in enumerate(user_data):
            user_entry = user_data[id]
            printEntryList(index, id, user_entry)

def pringEntryByIndex(user_data, id_index_list, index_to_print):
    retrieved_id = id_index_list[int(index_to_print)]
    user_entry = user_data[retrieved_id]
    printEntry(retrieved_id, user_entry)

def printMenu():
    print("1. Save a new entry")
    print("2. Search by ID")
    print("3. Print ages average")
    print("4. Print all names")
    print("5. Print all IDs")
    print("6. Print all entries")
    print("7. Print entry by index")
    print("8. Exit")
    return input("Please enter your choice: ")

def wrongIdInput(given_id):
    print("Error: ID must be a number. " + given_id + " is not a number")

def printEntryList(index, id, user_entry):
    print(str(index) + ". " + id)
    print("   Name: " + user_entry["name"])
    print("   Age: " + user_entry["age"])

def printEntry(given_id, user_entry):
    print("ID: " + given_id)
    print("Name: " + user_entry["name"])
    print("Age: " + user_entry["age"])

def confirmContinue():
    input("Press Enter to continue")


# collection of global variables and data structures
age_sum_before_averaging = 0
running_flag = True
id_index_list = []
user_data = {}


while running_flag:
    user_choice = printMenu()
    if user_choice == "1":
        given_id = input("ID: ")
        if not given_id.isdigit():
            wrongIdInput(given_id)
        elif given_id in user_data:
            print("Error: ID already exists: " + str(user_data[given_id]))
        else:
            saveNewEntry(given_id, user_data, id_index_list)
        confirmContinue()

    elif user_choice == "2":
        given_id = input("Please enter the ID you want to look for: ")
        if not given_id.isdigit():
            wrongIdInput(given_id)
        elif given_id not in user_data:
            print("Error: ID " + given_id + " not saved")
        else:
            searchById(given_id, user_data)
        confirmContinue()
            
    elif user_choice == "3":
        printAgesAverage(age_sum_before_averaging, len(id_index_list))
        confirmContinue()

    elif user_choice == "4":
        printAllNames(user_data, len(user_data))
        confirmContinue()

    elif user_choice == "5":
        printAllIds(user_data, len(user_data))
        confirmContinue()
    
    elif user_choice == "6":
        printAllEntries(user_data, len(user_data))
        confirmContinue()

    elif user_choice == "7":
        user_input = input("Please enter the index of the entry you want to print: ")
        if not user_input.isdigit():
            print("Error: index must be a number. " + user_input + " is not a number")
        elif int(user_input) >= len(user_data) or int(user_input) < 0:
            print("Error: Index out of range. The maximum index allowed is " +str(len(user_data) - 1))
        else:
            pringEntryByIndex(user_data, id_index_list, user_input)
        confirmContinue()

    elif user_choice == "8":
        keep_looping = True
        while keep_looping:
            user_choice = input("Are you sure? (y/n) ")
            if user_choice == "y" or user_choice == "yes":
                print("Goodbye!")
                running_flag = False
                keep_looping = False
            elif user_choice == "n" or user_choice == "no":
                keep_looping = False
    else: 
        print("Error: Option [" + user_choice + "] does not exist. Please try again.")