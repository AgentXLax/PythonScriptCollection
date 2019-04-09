##Nathan Wisla
##1375068
##AUCSC 111
##November 3, 2016
##Lab 6

##Make a file that decrypts a message in the input file

def fDecrypt(inF):
    '''Decrypts an encrypted file'''
    ##The alphabet in ASCII: Captials are 65 to 90
    ##                       lowers are 97-122
    myFile = open(inF,'r')
    ##distance == ((numberInFile * 2) - 40) // 300
    distance = ((int(myFile.readline()) * 2) - 40) // 300
    for line in myFile:
        for char in line:
          #decrypt is the value of the character after the shift
            if ord(char) in range(65,91): #if the character is a capital
                decrypt = ord(char) - distance
                if decrypt in range(65,91): #if decrypt is in capitals
                    print(chr(decrypt), end='')
                else:
                    outOfRange = 65 - decrypt
                    #outOfRange == distance of the how far decrypt is from 'A'
                    backInRange = 91 - outOfRange
                    #backInRange == distance of decrypt wrt 'Z'
                    print(chr(backInRange), end='')

            elif ord(char) in range(97,123): #do the same for lower-case letters
                decrypt = ord(char) - distance
                if decrypt in range(97,123): 
                    print(chr(decrypt), end='')
                else:
                    outOfRange = 97 - decrypt
                    backInRange = 123 - outOfRange
                    print(chr(backInRange), end='') 
            
            else:
                print(char, end='')
        print(' ', end='')
    print()
    myFile.close()


##Construct a function that displays a grid of stars
##two parameters:
##              integer size -- grid must be a square this size
##              A list of tuples -- the positions that the stars should be located
##                                  print an error if the stars are out of range

def displayGrid(aNum, aTupleList):
    '''Prints out a square grid of size aNum and puts stars on
       the coordinates described by aTupleList
    '''
    if aNum > 0:
        #1. build the aNum x aNum matrix
        sqMatrix = []
        for row in range(aNum):
            sqMatrix.append([])
            for col in range(aNum):
                sqMatrix[row].append('')

        #2. place the stars in the matrix at the locations the tuples describe
        for i in range(len(aTupleList)):
            if aTupleList[i][0] not in range(1, aNum + 1) \
               or aTupleList[i][1] not in range(1, aNum + 1):  #The error print
                print(str(aTupleList[i]) + ' is out of range.')
            else:
                #the matrix located at the ordered pair tuple
                sqMatrix[aTupleList[i][0] - 1][aTupleList[i][1] - 1] = '*' 

        #3. print out the grid
        print('{:1}'.format(''), end='') 
        for row in range(len(sqMatrix)): #prints 0th row
            print('{:>3}'.format(row + 1), end='')
        print()
        for row in range(len(sqMatrix)):
            print('{:>2}'.format(row + 1),end='') #prints 0th column
            for col in range(len(sqMatrix[row])):
                print('{:^3}'.format(sqMatrix[row][col]),end='') #prints matrix
            print()

    else:
        print('What is this, a grid for ants? I\'m not printing this out.')
    print()
