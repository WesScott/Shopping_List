# The following list is a list of strings to write to the file
GroceryList = []

# readFile reads all the items in the txt file line by line and adds them to the GroceryList
def readFile():
    global GroceryList
    file1 = open("list.txt","r")
    GroceryList = file1.readlines()
    GroceryList = [i.strip() for i in GroceryList]
    file1.close()
    return

# Write to file writes all the items in GroceryList to the text file
def writeToFile():
    global GroceryList
    file1 = open("list.txt","w")
    for item in GroceryList:
        file1.write(item)
        file1.write("\n")
    file1.close()

# The following three lists are lists used to process user Inputs:
yesList = ["Yes", "yes", "Y", "y"]
noList = ["No", "no", "N", "n"]
quitList = ["Quit", "quit", "Exit", "exit", "Stop", "stop"]

# showList() will print the current GroceryList to the python console:
def showList():
    global GroceryList
    if len(GroceryList) == 0:
        print("LIST IS EMPTY")
    count = 1
    for item in GroceryList:
        print("{}) {}".format(count, item))
        count += 1
    return

# addItem(item) will add an item to the grocery list, as well as rewrite the list to the file:
def addItem(item):
    global GroceryList
    GroceryList.append(item)
    writeToFile()
    return

# clearList() will delete everything form the GroceryList, and then overwrite the txt file
def clearList():
    global GroceryList
    GroceryList = []
    writeToFile()
    return

# stripString(string) will remove any characters in '~`!@#$%^&*()-_=+|\/?><,.' from the string:
def stripString(string):
    for char in string:
        if char in '~`!@#$%^&*()-_=+|\/?><,.':
            string.replace(char,"")
    return string

# createFile() will create a new file based on the date and make it a printable txt file sorted by date of creation
def createFile():
    fname = str(input("What would you like to name your file?\n(Special characters will be removed)\n>>>"))
    newFile = open("{}.txt".format(stripString(fname)),'w+')
    for item in GroceryList:
        newFile.write(item)
        newFile.write("\n")
    newFile.close()

def deleteItem(item):
    global GroceryList
    for Item in GroceryList:
        if item == Item:
            GroceryList.remove(item)
            print("removed {}".format(item))
    writeToFile()
    return

# processChoice(choice) takes in a string and process the correct actions in accordance to mainMenu()
def processChoice(choice):
    if choice == "1":
        print("\n-- Shopping List --")
        showList()
        print("-- END Shopping List --\n")
    elif choice == "2":
        toAdd = str(input("Enter the item you wish to add:\n>>"))
        addItem(toAdd)
    elif choice == "3":
        createFile()
    elif choice == "4":
        clearList()
    elif choice == "5":
        toDel = str(input("\nEnter the item you wish to delete:\n>>"))
        deleteItem(toDel)
    elif choice in quitList:
        return
    else:
        print("Invalid choice, please try again")
    mainMenu()

# mainMenu() launches the main menu of the program, and will be called upon program init
def mainMenu():
    print("1) Show Grocery List")
    print("2) Add item to List")
    print("3) Make printable list")
    print("4) Clear list")
    print("5) Delete an Item")
    userIn = str(input(">>"))
    processChoice(userIn)


# Program Init:
readFile()
mainMenu()





