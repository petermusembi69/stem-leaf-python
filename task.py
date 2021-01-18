#!/usr/bin/python3
# task.py
import stemgraphic
import numpy

# function is used to greet the user
def printIntro():
    print('Greetings there')


# function is used to prompt the user for input
def getInput():
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
    print("Your input is: {}".format(selectedNo))
    print("Generating the stem-Leaf Diagram ...")
    numbers = [11,12,2,10,3,22,33,45]
    stemgraphic.stem_graphic(numbers, scale=2)
    print(numpy.median(numbers))
    getInput()

# function exits the loop
def exiting():
    print('Exiting ...')
    exit()

def main():
    printIntro()
    getInput()

if __name__ == "__main__":
    main()


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
