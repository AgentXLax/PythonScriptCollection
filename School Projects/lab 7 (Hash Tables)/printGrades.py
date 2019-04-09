#print report constructs a thing with marks

def average(aList): #produce an average, is called a few times
    '''Returns an average from a list of integer values'''
    if len(aList) == 0:
        return 0
    else:
        return sum(aList) / len(aList)
    
def buildDictionary(inF): #the important infrastructure
    '''Returns a dictionary from an input file'''
    myFile = open(inF, 'r')
    outerDict = {}
    for line in myFile:
        listOfTheLine = line.split()
        lastName = listOfTheLine[0][:-1] #removes the comma
        innerDict = {} #a second, inner dictionary
        innerDict['first'] = listOfTheLine[1]
        gradesList = listOfTheLine[2:]
        for i in range(len(gradesList)): #converts grades to int
            gradesList[i] = int(gradesList[i])
        innerDict['marks'] = gradesList
        innerDict['average'] = average(gradesList)
        outerDict[lastName] = innerDict #installs innerDict to the main dictionary
    myFile.close
    return outerDict

def classAvg(aDict): #creates a class average, uses the average function
    '''Returns the class average'''
    avgList = []
    for key in aDict: #iterate through the keys of the dictionary
        avgList.append(aDict[key]['average'])
    return average(avgList)

def minAvg(aDict):
    '''Returns the smallest average and who got it
    as a tuple
    '''
    worstAvg = float('inf')
    for key in aDict:
        if aDict[key]['average'] < worstAvg:
            worstAvg = aDict[key]['average']
            worstPerson = str(aDict[key]['first']) + ' ' + str(key)
    return float(worstAvg), worstPerson #returns a tuple.
           
def maxAvg(aDict):
    '''Returns the largest average and who got it
    as a tuple
    '''
    bestAvg = float('-inf')
    for key in aDict:
        if aDict[key]['average'] > bestAvg:
            bestAvg = aDict[key]['average']
            bestPerson = str(aDict[key]['first']) + ' ' + str(key)
    return float(bestAvg), bestPerson

def printReport(inF):
    reportCard = buildDictionary(inF)
    print('{:>20}'.format('Marks Summary'))
    print('{:>20}'.format('-------------'))
    print('{0:<20}''{1:>10}'.format('Name','Average'))
    for key in sorted(reportCard):
        print('{0:<20}''{1:>10.2f}'.format(reportCard[key]['first'] + ' ' + key,reportCard[key]['average']))
    print('-' * 30)
    print('{0:<20}''{1:>10.2f}'.format('Class average:',classAvg(reportCard)))
    print('{0:<20}''{1:>10.2f}'.format('Lowest mark:',minAvg(reportCard)[0]),minAvg(reportCard)[1])
    print('{0:<20}''{1:>10.2f}'.format('Highest mark:',maxAvg(reportCard)[0]),maxAvg(reportCard)[1])

printReport('grades.txt')
