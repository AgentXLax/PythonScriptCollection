#October 6, 2016
#Nathan Wisla
#AUCSC111
#Lab 4: Computing a Worker's Gross Pay


#compute an employee's pay
#by multiplying the hours worked and the rate of pay.
##if the employee has worked more than 40 hours,
##then they should be paid at 1.5 times the for the hours spent over 40.
###if the employee worked over 60 hours,
###then they should be payed double the rate for hours over 60

def grossPay(numHours, payRate):
    maxRTHours = 40 #maximum amount of hours in reg. time
    OTHours = numHours - maxRTHours #amount of hours spent in overtime
    maxOTHours = 20 #maximum amount of hours in overtime
    DTHours = numHours - (maxRTHours + maxOTHours) #amount of hours spent in double-time
    
    if numHours > 60:
        return maxRTHours * payRate + maxOTHours * payRate * 1.5 + DTHours * payRate * 2
    elif numHours > 40:
        return maxRTHours * payRate + OTHours * payRate * 1.5
    elif numHours < 0:
        return 0
    else:
        return numHours * payRate

#The function being implemented
print('10 hours at $10: ', grossPay(10, 10))
print('39 hours at $15: ', grossPay(39, 15))
print('40 hours at $10: ', grossPay(40, 10))
print('40.5 hours at $10: ', grossPay(40.5, 10))
print('50 hours at $10: ', grossPay(50, 10))
print('59 hours at $10: ', grossPay(59, 10))
print('60 hours at $10: ', grossPay(60, 10))
print('60.5 hours at $20: ', grossPay(60.5, 20))
print('65 hours at $10: ', grossPay(65, 10))
print('0 hours at $10: ', grossPay(0, 10))
print('-2 hours at $10: ', grossPay(-2, 10))

