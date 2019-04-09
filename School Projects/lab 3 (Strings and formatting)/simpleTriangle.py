##make a program that print's the user's name in a simple triangle.

name = input('What is your name? ')

for letterPosition in range(len(name)):
    print(name[letterPosition] * (letterPosition+1))
