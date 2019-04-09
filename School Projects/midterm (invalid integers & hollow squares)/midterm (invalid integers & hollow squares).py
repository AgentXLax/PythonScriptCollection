##AUCSC111
##Nathan Wisla
##October 27, 2016
##Midterm

##1)
##Create a function called hollowSquare(a,b) which takes two integers as parameters.
##Both integers should be positive and print an error if they are not
##Parameter 1: width and boundary of the square
##Parameter 2: specifies the hollow

def hollowSquare(boundWidth, hollow):
    '''creates a square of size 2 * boundWidth + hollow
    with a hollow square inside of the boundary
    '''
    if boundWidth < 0 or hollow < 0:
        print('you can\'t do that, silly!')
    else:
        for i in range(2 * boundWidth + hollow):
            if i >= boundWidth and i < boundWidth + hollow:
                print('*' * boundWidth + ' ' * hollow + '*' * boundWidth)
            else:
                print('{}'.format('*' * (2 * boundWidth + hollow)))
    print()
    return 0

hollowSquare(2,5)
##2)
##a function called printGraph which takes an open integer file. This file will mostly have i=pairs of positive integers on each line.
##Lines that do not contain pairs of positive integers will be considered invalid.
##
##For every valid line in the file, the function will print a simple histograph of the two quantities.
##The first quantity will be represented with asterisks, and the second with a percent symbol
##The function returns the number of invalid lines in the file

myFile = open('data.txt','r')

def printGraph(inF):
    '''prints a histogram and returns the amount of invalid
    lines in the file inF
    '''
    totalInvalids = 0
    for line in inF:
        listOfTheLine = line.split() #breaks the line up into a list
        if len(listOfTheLine) != 2 or (int(listOfTheLine[0]) < 0 or int(listOfTheLine[1]) < 0):
            totalInvalids += 1
        else:
        #if the length of the list is 2 and there are no negatives, print the table
            print('*' * int(listOfTheLine[0]) + '%' * int(listOfTheLine[1]))
    print(totalInvalids)       
    return totalInvalids
printGraph(myFile)
myFile.close()
