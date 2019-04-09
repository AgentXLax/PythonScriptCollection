##Lab 4
##Nathan Wisla
##1375068
##AUCSC111
##October 13, 2016
##Lab 5: screwing around with a .txt file

##Given a text file, perform operations on the file.
##3. Find the number of occurrences of a number in the entire file 'howMany(inF, num)'
##inF is the open input file


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
howMany(myFile, 23)
myFile.close()
