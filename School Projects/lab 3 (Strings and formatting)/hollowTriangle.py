##make a program that print's the user's name in a hollow triangle.

name = input('What is your name? ')

#Position the first letter by multiplying the length of the name times the first letter, length -1 times the second, etc.

for letterPosition in range(len(name)):
    if letterPosition == 0:
        print(' ' * (len(name) - (letterPosition + 1)) + name[letterPosition])
    #print the spaces, the letter, the spaces, then the letter again
    elif letterPosition in range(1,len(name)-1):
        print(' ' * (len(name) - (letterPosition + 1)) + (name[letterPosition] + (' ' * (2*letterPosition-1)) + name[letterPosition]))
    #print the last letter a bunch of times
    else:
         print(' ' * (len(name) - (letterPosition + 1)) + (name[letterPosition] + ' ') * len(name))
    
        
    
    
