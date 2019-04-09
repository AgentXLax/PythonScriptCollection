#Implement a Python program that requests three integers. Your program must determine
#whether there are any duplicates.
#It must print the message “All unique” if there are no duplicates.
#It must print a message saying “Duplicate” along with the number that is duplicated.

x = int(input('Enter first integer: ' ))
y = int(input('Enter second integer: ' ))
z = int(input('Enter third integer: ' ))
List = [x,y,z]

if  List.count(x) > 1 : #counts the amount of times x, y, or z is in the list
    print ('Duplicate: ',x)
elif List.count(y) > 1 :
    print ('Duplicate: ',y)
else :
    print('Unique')
