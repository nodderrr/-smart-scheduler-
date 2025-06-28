examSchedule = []


def userInterface():
    print("\nSmart Scheduler")
    print("1. Add New Exam")
    print("2. View All Exams")
    print("3. Edit Exam")
    print("4. Delete Exam")
    print("5. Exit")
    

def choiceFunction(choice, examSchedule):
    if choice == 1:
        addFunction(examSchedule)
    elif choice == 2:
        viewFunction(examSchedule)
    elif choice == 3:
        editFunction(examSchedule)
    elif choice == 4:
        deleteFunction(examSchedule)
    elif choice == 5:
        exitFunction()
    else:
        print("Invalid Choice. Please Enter 1-5.")


def addFunction(examSchedule):
    name = input("Enter Name: ")
    date = input("Enter Date: ")
    time = input("Enter Time: ")
    room = input("Enter Room: ")

    examValue = {
        "name": name,
        "date": date,
        "time": time,
        "room": room,
    }
        
    examSchedule.append(examValue)
    print("Exam Added Successfully")
    

def viewFunction(examSchedule):
    print("\nAll Exams:")
    if not examSchedule:
        print("No Exams Found.")
    else:
        for examValue in examSchedule:
            print("Name:", examValue["name"])
            print("Date:", examValue["date"])
            print("Time:", examValue["time"])
            print("Room:", examValue["room"])


def editFunction(examSchedule):
    print("\nEdit Exam:")
    if not examSchedule:
        print("No Exams To Edit.")
    else:
        for index, examValue in enumerate(examSchedule):
            print(f"{index}. {examValue['name']} {examValue['date']} {examValue['time']} {examValue['room']}")

        edit = int(input("Enter Index Number You Want To Edit: "))
        name = input("Enter New Name: ")
        date = input("Enter New Date: ")
        time = input("Enter New Time: ")
        room = input("Enter New Room: ")

        examValue = {
            "name": name,
            "date": date,
            "time": time,
            "room": room,
        }

        examSchedule[edit] = examValue
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
