
Database = []


def show_menu():
    print()
    print("press 1 to edit database")
    print("press 2 to show database")
    print("press 3 to exit the program")
    print()


def edit_database():
    while True:
        exit_adding = input(
            "do you want to add to your database? [yes]  [no] :\n>")
        if exit_adding == "yes":
            Database_creation = input(
                "type anything you want to add to the database :\n> ")
            Database.append(Database_creation)
            continue
        if exit_adding == "no":
            break


def show_database():
    print(f"this is your database {Database}")


def exit_program():
    print("you have exited the program")


while True:
    show_menu()
    keypressed = int(input("please type one option :\n>"))
    if keypressed == 1:
        edit_database()
    elif keypressed == 2:
        show_database()
    elif keypressed == 3:
        exit_program()
        break


"""
 
"""
"""
print("                                "
      " "
      " "
      " ")
print("press 1 to edit database")
print("press 2 to show database")
print("press 3 to exit the program")

Database = []
while True:
    keypressed = int(input("please type one option"))
    if keypressed == 1:
        Database_creation_input = int(
            input("press 4 to add to database and 5 to get to previous menu"))
        if Database_creation_input == 4:
            while True:
                Database_creation = input(
                    "add here your data")
                Database.append(Database_creation)
                exit_adding = input("do you want to keep adding? [yes]  [no] ")
                if exit_adding == "yes":
                    continue
                if exit_adding == "no":
                    break
        elif Database_creation_input == 5:
            "da noch eine while hinzufügen oben "
    elif keypressed == 2:
        print(f"this is your database {Database}")
    elif keypressed == 3:
        print("you have exited the program")
        break
"""
