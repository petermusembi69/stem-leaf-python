#!/usr/bin/python3

def printIntro():
    # greet user
    print('Greetings there')

def getInput(a,b,c):
    #get user input either 1,2 or 3
    print('Select one Input')
    print('[1] Genereate Stem and Leaf')
    print('[2] Genereate Stem and Leaf')
    print('[3] Genereate Stem and Leaf')
    print('[4] Exit')

def generateStemLeaf(directory,selectedNo):
    #read the appropriate datafile & display a stem-and-leaf plot
    filename1 = "C:/directory/StemAndLeaf1.txt"
    filename2 = "C:/directory/StemAndLeaf2.txt"
    filename3 = "C:/directory/StemAndLeaf3.txt"
    if selectedNo == 1:
        infile = open(filename, "r")
        lineList = infile.readlines()
        infile.close()
        for i in range ( 0, len(lineList) ):
         x = int(lineList[i].strip())
         print (x)
# iteration getInput(a)

printIntro()
getInput()
generateStemLeaf()

