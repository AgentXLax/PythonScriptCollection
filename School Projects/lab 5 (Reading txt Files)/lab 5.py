##Lab 4
##Nathan Wisla
##1375068
##AUCSC111
##October 13, 2016
##Lab 5: screwing around with a .txt file

##Given a text file, perform operations on the file.
##1. Total each line of the file 'totalOnLines(inF)'
##2. Find the biggest number on each line of the file 'biggestOnLines(inF)'
##3. Find the number of occurrences of a number in the entire file 'howMany(inF, num)'
##inF is the open input file

myFile = open('data.txt','r')

def totalOnLines(inF):
    '''Returns the total of each line of a file.'''
    for line in inF:
        listOfTheLine = line.split()
        #breaks the line up into a list
        sumTotal = 0
        for element in listOfTheLine:
            #sum the elements of the list
            sumTotal = int(element) + sumTotal
        print(sumTotal)

def biggestOnLines(inF):
    '''Returns the largest value in each line of a file'''
    for line in inF: #go through the file        
        listOfTheLine = line.split()
        if listOfTheLine == []:
            listOfTheLine = [0]
        else:
            for i in range(len(listOfTheLine)):
                #converting the list into a list of integers
                listOfTheLine[i] = int(listOfTheLine[i])
        print(max(listOfTheLine))
        #print off the max value for each line

def howMany(inF,num):
    '''Finds the number of times num appears in the file'''
    ultimateList = []
    for line in inF:
        listOfTheLine = line.split()
        for element in listOfTheLine:
            #append each element of the file into the ultimate list
            ultimateList.append(int(element))
    if num in ultimateList:
        print(ultimateList.count(num))
        #count the number you want to count in the ultimate list
    else:
        print('Can\'t find it, sorry.')

myFile = open('data.txt','r')
totalOnLines(myFile)
myFile.close()
print('------')
myFile = open('data.txt','r')
biggestOnLines(myFile)
myFile.close()
print('------')
myFile = open('data.txt','r')
howMany(myFile,30)
myFile.close()
print('------')
myFile = open('data.txt','r')
howMany(myFile,23)
myFile.close()


        
            
