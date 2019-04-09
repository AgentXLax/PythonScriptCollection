##Lab 4
##Nathan Wisla
##1375068
##AUCSC111
##October 13, 2016
##Lab 5: Remainder Table

##Print a row x column grid where each entry contains the remainder of dividing row by column

def remainder(row,col):
    '''Prints a row x col table that gives a remainder'''
    if row == 0 or col == 0:
        print('You can\'t have empty rows or columns, silly.')
        print()
    else:
        print('{:2}%|'.format(''), end='')
        for j in range(1, col + 1):
            print('{:3}'.format(j), end='') #prints the first row
        print(); print('{:2}'.format('') + '---' * (col + 1)) #separator
        for i in range(1, row + 1): 
            print('{:3}|'.format(i), end='') #prints the beginning of the ith row with a separator
            for j in range(1, col + 1):
                print('{:3}'.format(i % j), end='') #prints the jth entry in the ith row
            print()
        print() #buffer if you want to print multiple tables

remainder(0,1)
remainder(6,4)
remainder(10,2)
