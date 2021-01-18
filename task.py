#!/usr/bin/python3
#task.py

def Hello():
	print("Hello!\n")

def Hi():
	while True:
		try:
			choice = int(input("\nEnter either \n[1] \n[2] \n[3] \n "))
		except ValueError:
			print("Invalid Input")
			continue

		if 1 < choice < 3:
			break
		else: 
			print("invalid input")
	print("Your input is: {}".format(choice))
	mydict = {1,2,3}
	mydict[choice]()

# def getInput():
#     #get user input either 1, 2 or 3
# 	select = input("\nEnter either \n[1] \n[2] \n[3] \n ")
# 	if(select == 1 or select == 2 or select == 3):
# 		return select
# 	# else:
# 		# getInput()
# getInput()

# def Fuck():
# 	if select == 1: 
# 		filename = "Data/StemAndLeaf1.txt"

# 		infile = open(filename, "r")
# 		lineList = infile.readlines()
# 		infile.close()

# 		for i in range(0, len(lineList)):
# 			x = int(lineList[i].strip())
# 			print(x)

	# if select == 1: 
	# 	filename = "Data/StemAndLeaf2.txt"

	# if select == 1: 
	# 	filename = "Data/StemAndLeaf3.txt"

		
	
# def getInput():
# 	user_input = input("Enter 1, 2 or 3 : ")
# 	if user_input == 1 :
# 		#openfile1
# 	if user_input == 2 : 
# 		#openfile2
# 	if user_input == 3 :
# 		# open file3
# 	else 

	 

    # answer = input("What flavor do u want [vanilla]?")
    # if answer:
    #     flavor = answer
    # else:
    #     flavor = "vanilla"

    # print("The flavor you chose is", flavor)
   
#    # if __name__ =='__main__'
#    # 
# filename = "Data/StemAndLeaf1.txt"

# 		infile = open(filename, "r")
# 		lineList = infile.readlines()
# 		infile.close()

# 		for i in range(0, len(lineList)):
# 			x = int(lineList[i].strip())
# 			print(x)

# def printIntro():
#     # greet user
#     print('Greetings there')

# def getInput(a,b,c):
#     #get user input either 1,2 or 3
#     print('Select one Input')
#     print('[1] Genereate Stem and Leaf')
#     print('[2] Genereate Stem and Leaf')
#     print('[3] Genereate Stem and Leaf')
#     print('[4] Exit')

# def generateStemLeaf(directory,selectedNo):
#     #read the appropriate datafile & display a stem-and-leaf plot
#     filename1 = "C:/directory/StemAndLeaf1.txt"
#     filename2 = "C:/directory/StemAndLeaf2.txt"
#     filename3 = "C:/directory/StemAndLeaf3.txt"
#     if selectedNo == 1:
#         infile = open(filename, "r")
#         lineList = infile.readlines()
#         infile.close()
#         for i in range ( 0, len(lineList) ):
#          x = int(lineList[i].strip())
#          print (x)
# # iteration getInput(a)

# printIntro()
# getInput()
# generateStemLeaf()

