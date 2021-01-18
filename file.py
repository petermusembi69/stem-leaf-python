filename = "Data/StemAndLeaf1.txt"

infile = open(filename, "r")
lineList = infile.readlines()
infile.close()

for i in range(0, len(lineList)):
    x = int(lineList[i].strip())
    print(x)
