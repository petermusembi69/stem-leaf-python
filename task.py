#!/usr/bin/python3
# task.py

def printIntro():
    """
    -------------------
    printIntro() METHOD
    -------------------
    
    function greets the user
    """
    print('Greetings there')

def getInput():
    """
    -----------------
    getInput() METHOD
    -----------------

    function prompt the user to
    enter a value

    calls
    -----  
    generateSteamLeaf(arg_1)
        generates the stem leaf diagram
    
    exiting()
        exits the program

    """
    while True:
        try:
            choice = int(input(
                "\nEnter either 1,2,3 or 4 \n[1]Genereate Stem and Leaf \n[2]Genereate Stem and Leaf \n[3]Genereate Stem and Leaf \n[4]Exit \n"))
        except ValueError:
            print("Invalid Input")
            continue
        if 1 <= choice <= 3:
            generateStemLeaf(choice)
        elif choice == 4:
            exiting()
        else:
            print("invalid input")

# function is used to generate a stem leaf diagram
def generateStemLeaf(selectedNo):
    """
    ------------------------
    generateStemLeaf() METHOD
    ------------------------
    
    function draws stem leaf diagram
    and prompt the user to enter
    another value

    Parameters
    ----------
    arg_1 : int
    contains the selected value

    calls
    ----- 
    drawStemLeaf(arg_1)
        to generate the stem
        leaf diagram
    
    getInput()
        to prompt the user to
        enter a value

    """
    print("Your input is: {}".format(selectedNo))
    print("Generating the stem-Leaf Diagram ...")
    drawStem(selectedNo)
    getInput()

def drawStem(selectedNo):
    """
    ------------------
    drawStem() METHOD
    ------------------

    function reads the appropriate
    file inputs and draws the
    stem-leaf diagram

    Parameters
    ----------
    arg_1 : int
    contains the selected value

    calls
    ----- 
    generateSteamLeaf(arg_1)
        generates the stem leaf diagram
    
    exiting()
        exits the program
    """
    filename1 = "F:/stem-leaf-python/Data/StemAndLeaf1.txt"
    filename2 = "F:/stem-leaf-python/Data/StemAndLeaf2.txt"
    filename3 = "F:/stem-leaf-python/Data/StemAndLeaf3.txt"
    if selectedNo == 1:
        inFile = open(filename1, "r")
    elif selectedNo == 2:
        inFile = open(filename2, "r")
    else:
        inFile = open(filename3, "r")
    lineList = inFile.readlines()
    inFile.close()
    myDict = {}
    for i in range(0, len(lineList)):
        x = int(lineList[i].strip())
        y = str(x)
        if y[0:-1] in myDict:
            z = myDict[y[0:-1]]
            z.append(y[-1])
            myDict[y[0:-1]] = z
        else:
            myList = []
            myList.append(y[-1])
            myDict[y[0:-1]] = myList
    for key in myDict:
        print(key + "|", end = '')
        for key2 in myDict[key]:
            print(key2, end = '')
        print()


def exiting():
    """
    ----------------
    exiting() METHOD
    ----------------

    function exits the loop
    and  prints Exiting ...
    the terminal
    """
    print('Exiting ...')
    exit()


def printDocString():
    """
    -----------------------
    printDocString() METHOD
    -----------------------

    function prints the doc
    """
    print(printIntro.__doc__)
    print(getInput.__doc__)
    print(generateStemLeaf.__doc__)
    print(drawStem.__doc__)
    print(exiting.__doc__)


def main():
    """
    -------------
    main() METHOD
    -------------

    functions calls the required
    methods in order of execution
    """
    printDocString()
    printIntro()
    getInput()
    

if __name__ == "__main__":
    main()

