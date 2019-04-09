class ArmstrongNumber:
    '''
    A class that creates an armstrong number, with methods to check
    if the number is a valid armstrong number and methods to add numbers
    armstrong style
    '''
    def __init__(self, armstrongNumber):
        #constructor
        self.armstrongNumber = armstrongNumber
        self.length = len(str(armstrongNumber))
    
    def toList(self):
        '''
        toList converts a number to an array with the digits reversed
        returns a reversed list of the number
        '''
        aList = []
        num = self.armstrongNumber
        while(num != 0):
            aList.append(num % 10)
            num //= 10 #integer divide by 10 so we can actually get to zero
        return aList

    def armstrongSum(self):
        '''
        sums the armstrong number armstrong style
        '''
        aList = self.toList()
        armySum = 0
        for i in range(0, self.length):
            armySum += aList[i] ** self.length
        return armySum

    def isArmstrong(self):
        '''
        checks to see if the armstrong number is actually an armstrong number
        '''
        return self.armstrongSum() == self.armstrongNumber

armstrong = ArmstrongNumber(153)
print (armstrong.isArmstrong())
armstrong = ArmstrongNumber(1643)
print (armstrong.isArmstrong())
armstrong = ArmstrongNumber(1634)
print (armstrong.isArmstrong())
