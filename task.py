#!/usr/bin/python3
# task.py


def printIntro():
    # greet user
    print('Greetings there')


def getInput():
    while True:
        try:
            choice = int(input(
                "\nEnter either 1,2,3 or 4 \n[1]Genereate Stem and Leaf \n[2]Genereate Stem and Leaf \n[3]Genereate Stem and Leaf \n[4]Exit \n"))
        except ValueError:
            print("Invalid Input")
            continue

        if 1 <= choice <= 3:
            # print("Your input is: {}".format(choice))
            generateStemLeaf(choice)
        elif choice == 4:
            leaving()
        else:
            print("invalid input")


def generateStemLeaf(selectedNo):
    print(selectedNo)
    print('Generate the leaf stem here')
    getInput()

# function exits the loop
def leaving():
    print('Exiting')
    exit()

printIntro()
getInput()
#     # read the appropriate datafile & display a stem-and-leaf plot
#     filename1 = "C:/directory/StemAndLeaf1.txt"
#     filename2 = "C:/directory/StemAndLeaf2.txt"
#     filename3 = "C:/directory/StemAndLeaf3.txt"
#     if selectedNo == 1:
#         infile = open(filename, "r")
#         lineList = infile.readlines()
#         infile.close()
#         for i in range(0, len(lineList)):
#             x = int(lineList[i].strip())
#             print(x)
# # iteration getInput(a)


# printIntro()
# getInput()
# # generateStemLeaf()
