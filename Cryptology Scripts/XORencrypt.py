#encrypt a statement with the key being ice
#encrypt each byte of the sentence with I, C, E, repeated sequentially

message = 'Burning \'em, if you ain\'t quick and nimble I go crazy when I hear a cymbal'
key = 'ICE'

def xorEncrypt(message, key):
    #for loop to read each char in the string
    ciphertext = ''
    for i in range(len(message)):
        ciphertext += hex(ord(message[i]) ^ ord(key[i%3]))[2:]
        print('char1:',message[i],'keychar:',key[i%3],'encoded char:',hex(ord(message[i]) ^ ord(key[i%3])))

    return ciphertext

print(xorEncrypt(message, key))
