def countBits(num):
    count = 0
    while(num != 0):
        if(num & 1 == 1):
            count += 1
        num >>= 1
    return count

activeBits = countBits(int(input('enter a number: ')))
activeBits

