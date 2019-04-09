##Nathan Wisla
##AUCSC111
##November 13, 2016
##7AM all-nighter because the file wiped itself for some reason
##but hey, at least I got to reorganize part 1 with functions...
##lab 7: Dictionaries


#1)Print a specialized report on data from a file using a dictionary
#  Build the dictionary first
#  Special functions will be called to find class avg, highest and lowest
#  Print all relevant functions in printReport.

def average(aList): #produce an average, is called a few times
    '''Returns an average from a list of integer values'''
    if len(aList) == 0:
        return 0
    else:
        return sum(aList) / len(aList)
    
def reportDict(inF): #the nested dictionary infrastructure
    '''Returns a "report card" formatted
       dictionary from an input file
    '''
    myFile = open(inF, 'r')
    outerDict = {}
    for line in myFile:
        listOfTheLine = line.split()
        innerDict = {}
        
        #removes the comma in the last name
        lastName = listOfTheLine[0][:-1]
        innerDict['first'] = listOfTheLine[1]

        #for loop converts grades to integer type
        gradesList = listOfTheLine[2:]
        for i in range(len(gradesList)):
            gradesList[i] = int(gradesList[i])
        
        innerDict['marks'] = gradesList
        innerDict['average'] = average(gradesList)
        #installs innerDict to the main dictionary
        outerDict[lastName] = innerDict

    myFile.close()
    return outerDict

#creates a class average, uses the average function
def classAvg(aDict): 
    '''Returns the class average'''
    avgList = []
    #iterate through the keys of the dictionary and append each average
    for key in aDict:
        avgList.append(aDict[key]['average'])
    return average(avgList)

#creates the smallest average in the dictionary
def minAvg(aDict):
    '''Returns the smallest average and who got it
       as a tuple in the report card format dictionary
    '''
    worstAvg = float('inf')
    #iterate through the keys of the dictionary and find the
    #worst mark and person associated
    for key in aDict:
        if aDict[key]['average'] < worstAvg:
            worstAvg = aDict[key]['average']
            worstPerson = str(aDict[key]['first']) + ' ' + str(key)
    #returns a tuple of a float and a string
    return float(worstAvg), worstPerson

#creates the largest average in the dictionary, same format as minAvg
def maxAvg(aDict):
    '''Returns the largest average and who got it
       as a tuple in the report card format dictionary
    '''
    bestAvg = float('-inf')
    for key in aDict:
        if aDict[key]['average'] > bestAvg:
            bestAvg = aDict[key]['average']
            bestPerson = str(aDict[key]['first']) + ' ' + str(key)
    return float(bestAvg), bestPerson

def printReport(inF):
    '''Prints a report card from an input file'''
    reportCard = reportDict(inF)
    print('{:>20}'.format('Marks Summary'))
    print('{:>20}'.format('-------------'))
    print('{0:<24}''{1:>6}'.format('Name','Average'))
    for key in sorted(reportCard):
        print('{0:<24}''{1:>6.2f}'\
              .format(reportCard[key]['first'] + ' ' + \
                      key,reportCard[key]['average']))
    print('-' * 30)
    print('{0:<24}''{1:>6.2f}'\
          .format('Class average:',classAvg(reportCard)))
    print('{0:<24}''{1:>6.2f}'\
          .format('Lowest mark:',minAvg(reportCard)[0]),\
          '(' + minAvg(reportCard)[1] + ')')
    print('{0:<24}''{1:>6.2f}'\
          .format('Highest mark:',maxAvg(reportCard)[0]),\
          '(' + maxAvg(reportCard)[1] + ')')
    print()

printReport('grades.txt')

#2)Create an index using a dictionary
#  Build the dictionary. {word : [first appearance, ..., nth appearance],...}
#  Print the dictionary
#We want a dictionary that

def buildIndexDict(inF):
    '''Returns a dictionary that counts the lines where
       a word with more than 3 letters appears in a file
    '''
    myFile = open(inF,'r')
    aDict = {}
    #counts which line the word appears
    lineLoc = 1
    for line in myFile:
        listOfTheLine = line.split()
        #iterates through words, checks if they are longer than 3 letters
        for word in listOfTheLine: 
            if len(word) > 3:

                #checks if the word is in the dictionary
                if word.lower() in aDict:
                    #if the word appears more than once
                    #don't append the line again
                    if lineLoc not in aDict[word.lower()]:
                        aDict[word.lower()].append(lineLoc)
                else:
                    #creates a list associated with the word
                    aDict[word.lower()] = [lineLoc]
                    
        lineLoc += 1
    myFile.close()
    return aDict

def indexMaker(inF):
    '''Prints an index from an input file. The index
       counts the lines where a word with more than
       3 letters appears.
    '''
    indexDict = buildIndexDict(inF)
    for key in sorted(indexDict):
        print('{:<20}'.format(key),end='')
        i = 0
        #print where the lines occured with nice commas
        while i < len(indexDict[key]) - 1:
            print(indexDict[key][i],end=', ')
            i += 1
        #except for the last one. NO COMMAS FOR YOU
        print(indexDict[key][i])
    print()
    

indexMaker('hump.txt')
