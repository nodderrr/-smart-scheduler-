examSchedule = []


def userInterface():
    print("5. Exit")
    

def choiceFunction(choice, examSchedule):
        print("Invalid Choice. Please Enter 1-5.")


def addFunction(examSchedule):
    print("Exam Added Successfully")
    

def viewFunction(examSchedule):
            print("Room:", examValue["room"])


def editFunction(examSchedule):
        print("Exam Edited Successfully")


def deleteFunction(examSchedule):
    print("\nDelete Exam:")
    if not examSchedule:
        print("No Exams To Delete.")
    else:
        for index, examValue in enumerate(examSchedule):
            print(f"{index}. {examValue['name']} {examValue['date']} {examValue['time']} {examValue['room']}")

        delete = int(input("Enter Index Number You Want To Delete: "))
        examSchedule.pop(delete)
        print("Exam Deleted Successfully")


def exitFunction():
    print("Exit Successfully, Thank You!")
    exit()

 
while True:
    userInterface()
    inputNumber = int(input("Enter Your Choice: "))
    choiceFunction(inputNumber, examSchedule)
