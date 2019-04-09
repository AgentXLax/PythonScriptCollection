str1 = 'this is a test'
str2 = 'wokka wokka!!!'
byte1 = b'this is a test'
byte2 = b'wokka wokka!!!'
hex1 = byte1.hex()
hex2 = byte2.hex()
def hammingDistance(str1,str2):
    xor = lambda b1,b2: b1^b2
    count = 0
    for byte in zip(str1,str2):
        
        count += bin(byte[0]^byte[1]).count('1')

    return count
print(hammingDistance(byte1,byte2))


