print("Enter a number from the menu to obtain a facr")
print("about the United States or to exit the program. \n")
print("1. Capital")
print("2. National Bird")
print("3. National flower")
print("4. Quit\n")
while True:
    num = int(input("Make a selection from the menu: "))
    if num == 1:
        print("Washington, DC is the capital of the United States")
    elif num ==2:
        print("The American Bald Eagle is the narional bird")
    elif num ==3:
        print("The Rose is the national flower")
    elif num ==4:
        break