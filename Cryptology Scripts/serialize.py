import string
import random

#create a key that works in the string
def keyGenerator(size):
    randString = ''
    #generate a random set of characters
    for i in range(size):
        rChar = random.choice(string.ascii_letters + string.digits \
                              + string.punctuation + string.whitespace)
        randString += rChar
    return randString

key = keyGenerator(12) #make a global key

##take two strings as parameters and output them as a single string
def serialize(str1, str2):
    #Check the key against the string, create a new one if needed
    global key
    while key in str1 + str2:
        key = keyGenerator(12)
    return str1 + key + str2

# take the string from serialize and output it as the two original strings
def deserialize(serialized):
    global key
    keyPos = serialized.find(key)
    endPos = keyPos + len(key)
    return serialized[:keyPos],serialized[endPos:]
    

#TESTING AREA:
a = 'adfghgfrty44'; b = 'fgdnhgmhfgdaw7'; s = serialize(a,b);d = deserialize(s)
print('{}{}\n{}{}\n{}{}'.format('string 1: ', a, 'string 2: ', b, 'key: ', key))
print('{}{}\n{}{}\n'.format('serialized: ', s, 'deserialized: ', d))

a = ' '; b = '/*sjgfhjy5649848799&*&^6549%#@@aw7'; s = serialize(a,b);d = deserialize(s)
print('{}{}\n{}{}\n{}{}'.format('string 1: ', a, 'string 2: ', b, 'key: ', key))
print('{}{}\n{}{}\n'.format('serialized: ', s, 'deserialized: ', d))

a = ''; b = 'fgdnhgmhfgdaw7'; s = serialize(a,b);d = deserialize(s)
print('{}{}\n{}{}\n{}{}'.format('string 1: ', a, 'string 2: ', b, 'key: ', key))
print('{}{}\n{}{}\n'.format('serialized: ', s, 'deserialized: ', d))

a = 'sdfsgui tr$%^7823^%&b*Fw$3'; b = ''; s = serialize(a,b);d = deserialize(s)
print('{}{}\n{}{}\n{}{}'.format('string 1: ', a, 'string 2: ', b, 'key: ', key))
print('{}{}\n{}{}\n'.format('serialized: ', s, 'deserialized: ', d))

a = 'lkjsdfgkgdfs*976$af%3f)0!`~'; b = ' '; s = serialize(a,b);d = deserialize(s)
print('{}{}\n{}{}\n{}{}'.format('string 1: ', a, 'string 2: ', b, 'key: ', key))
print('{}{}\n{}{}\n'.format('serialized: ', s, 'deserialized: ', d))
