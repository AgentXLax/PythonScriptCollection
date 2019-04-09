##Nathan Wisla
##1375068
##AUCSC 111
##Lab 3: Make a program that print's the user's name in a diamond.

#General format of the code:
#Position the first letter by multiplying the length of the name times for the first letter, length -1 times for the second, etc.
#Print the top tip by just positioning it.
#For everywhere but the tips, print the spaces, the letter, an odd amount of spaces (2n-1), then the letter again.
#Make another loop and do it in reverse.

name = input('What is your name? ')

#'i' represents the 'ith' position of the name. I initially used 'letterPosition,' but it got hella confusing and long.
for i in range(len(name)):
    if i == 0: #tip of the top triangle
        print(' ' * (len(name) - (i + 1))\
              + name[i])
    else: #body of the top triangle, including the last letter.
        print(' ' * (len(name) - (i + 1))\
              + (name[i] + (' ' * (2*i - 1)) + name[i]))

#Use the same iterator and do it in reverse.
for i in range(1,len(name)):
    if i == len(name) - 1: #tip of the bottom triangle. 
        print(' ' * i + name[-(i + 1)])
    else: #body of the bottom triangle
        print(' ' * i\
        + name[-(i + 1)] + (' ' * (2*(len(name) - (i + 1)) - 1)) + name[-(i + 1)])
         
