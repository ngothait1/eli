def wrongInputError(what_was_wrong, wrong_input_given):
    print("Error: " + what_was_wrong + " must be a number. " + wrong_input_given + " is not a number")
    

def properInputValidator(input_requested: str):
    while True:
        user_input = input("Enter a number for " +input_requested + ": ")
        if user_input.isdigit():
            return user_input
        wrongInputError(input_requested, user_input)


def printPersonMenu():
    print("Press 1 to save a student ")
    print("Press 2 to save an employee ")
    print("Press any other key for a regular person ")
