code = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
def decryptXOR(cipher, key):
    # create an anonymous function that
    #     performs the xor function on a hex byte against a character
    xor = lambda x,y: int(x,16) ^ int(y)
    # look at the hex code
    # since each byte has 2 hex digits, search them by 2 at a time
    #    and xor each byte with a constant character
    # search through the whole hex code
    decipher = ''
    for i in range(0,len(cipher),2):
        decipher += chr(xor(cipher[i:i+2],key))
    return decipher

def score(cipherText):
    '''scores a ciphertext based on the 12 most common characters
       in the English language: etaoin shrdlu, where u=1 and e=12
    '''
    #search the code for common characters and match the deciphered
    #characters with the commonChars string
    commonChars = 'ULDRHSNIOATEuldrhs nioate' #will work in an enumerate function. Capitals score lower than others due to how English uses them
    score = 0
    for char in cipherText:
        for checkingChar in enumerate(commonChars,1):
            if ord(checkingChar[1]) == ord(char):
                score += checkingChar[0]
    return score

def testAllChars(cipher):
    '''
    decrypts a cipher message using single character XOR by testing every character as a key
    cipher -> the encrypted hexadecimal message
    decrypt -> key, message
    '''
    keyToDecrypt=''
    leadingScore = 0
    message=''
    for i in range(0,256):
        decipherText = decryptXOR(cipher,i)
        cipherScore = score(decipherText)
        if (cipherScore > leadingScore):
            leadingScore = cipherScore
            message = decipherText
            keyToDecrypt = chr(i)
    return (keyToDecrypt, message)

def decipherFile(fileName):
    '''brute force deciphering of a file, testing each character in an xor decryption
       on each line, and scoring each line of the file after each line has been optimally decrypted.
       This will find the single encrypted line in the file. n^4 complexity
    '''
    inF = open(fileName,'r')
    leadingScore = 0
    leadingLine = 0
    lineNum = 0
    for line in inF:
        lineNum += 1 
        dcTuple = testAllChars(line[:-2]) #[:-2] ignores the \n at the end of each line
        cipherScore = score(dcTuple[1])
        if (cipherScore > leadingScore):
            leadingScore = cipherScore
            message = dcTuple[1]
            cipherKey = dcTuple[0]
            leadingLine = lineNum 
                
    inF.close()
    return cipherKey, message, leadingLine


print(testAllChars(code))

##print(decipherFile('cipher1.txt'))
