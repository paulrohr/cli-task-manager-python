print("press 1 to edit database")
print("press 2 to show database")
print("press 3 to exit the program")

Database = [1]
while True:
    keypressed = int(input("please type one option"))
    if keypressed == 1:
        print("test")
    elif keypressed == 2:
        print(f"this is your database {Database}")
    elif keypressed == 3:
        print("you have exited the program")
        break
