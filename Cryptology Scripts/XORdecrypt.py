import base64

class DecryptRepeatingKeyB64():

    def __init__(self,encodedFile):
        assert isinstance(encodedFile,str)
        assert '.txt' in encodedFile[-4:]

        ciphertext = self.getCipher(encodedFile)
        while((len(ciphertext) % 4) != 0):
            ciphertext += '='#pad the b64 as needed
        self.ciphertext = \
            base64.b64decode(ciphertext)##Turn into a bytearray
        self.KEYSIZE = self.findKeySize()
##        self.KEY = self.findKey()
        self.message = ''

    def __repr__(self):
        theString = 'your decrypted message is:' + self.message
        return
    
#=================STRING READING AND MODIFICATION METHODS=============
    def getCipher(self,fileName):
        cipher = ''
        inF = open(fileName,'r')
        for line in inF:
            cipher += line[:-2]
        inF.close()
        return cipher   

#=================KEY FINDING METHODS=================================    
    
    def hammingDistance(self,b1,b2):
        '''
        Measures the amount of different bits between 2 byte arrays
        '''
        count = 0
        for byte in zip(b1,b2):
            count += bin(byte[0]^byte[1]).count('1')
        return count

    def findKeySize(self):
        ciphertext = self.ciphertext
        minDistance = 0
        minNormalDistance = float('inf')
        normalizedDistances = []
        for KEYSIZE in range(2,40):
            #make 4 different, equal sized blocks, and calculate the
            #distances between blocks. normalize them and average
            b1 = ciphertext[0:KEYSIZE]
            b2 = ciphertext[KEYSIZE:KEYSIZE*2]
            b3 = ciphertext[KEYSIZE*2:KEYSIZE*3]
            b4 = ciphertext[KEYSIZE*3:KEYSIZE*4]

            normalizedDistance = \
                self.hammingDistance(b1,b2) +\
                self.hammingDistance(b2,b3) +\
                self.hammingDistance(b3,b4) / (KEYSIZE * 3)

            normalizedDistances.append((KEYSIZE,normalizedDistance))
            sortedDistances = sorted(normalizedDistances,key=lambda aTuple:aTuple[1])

        return sortedDistances

    def scorePlaintext(self):
        commonChars = 'ULDRHSNIOATEuldrhs nioate' #will work in an enumerate function. Capitals score lower than others due to how English uses them
        score = 0
        for char in cipherText:
            for checkingChar in enumerate(commonChars,1):
                if ord(checkingChar[1]) == ord(char):
                    score += checkingChar[0]
        return score
    
    def breakSingleKeyXOR(self, ciphertext, key):
        message = ''
        for i in range(len(ciphertext)):
            message += ciphertext[i] ^ key[i%3]

        return message
        
    def cipherBlocks(self):
        KEYSIZE = self.KEYSIZE[0][0]
        ciphertext = self.ciphertext
        cipherBlocks = [''] * KEYSIZE
        for i in range(len(ciphertext)):
            cipherBlocks[i % KEYSIZE] += ciphertext[i]
        return cipherBlocks
                

            
            
cipher1 = DecryptRepeatingKeyB64('cipher2.txt')
