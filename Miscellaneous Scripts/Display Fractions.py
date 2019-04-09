#Display Fractions will take fractions and display them in different formats

def mixedToFrac(lead, numerator, denominator):
    '''Takes a mixed fraction and converts it to an improper fraction
       lead -> leading number
       numerator -> numerator of the fraction
       denominator -> denominator of the fraction
    '''
    return str((lead * denominator) + numerator) + '/' + str(denominator)
                                            
def splitNumber(number, key):
    firstHalf = 0
    secondHalf = 0
    for i in range(len(number)):
        if number[i] == key:
            number = number[i + 1:]
            break
        firstHalf *= 10
        firstHalf += int(number[i])     
    secondHalf = int(number)
    return firstHalf, secondHalf

def splitFrac(number):
    key = '/'
    return splitNumber(number, key)

def splitDecimal(number):
    key = '.'
    number = str(number)
    return splitNumber(number, key)

def fracToDec(fraction):
    rationalNum = splitFrac(fraction)
    return rationalNum[0]/rationalNum[1]

def decToFrac(decimal):
    split = splitDecimal(decimal)
    denom = 10 ** len(str(split[1]))
    wholeNum = denom * split[0]
    fraction = reduceFrac(wholeNum + split[1], denom)
    return fraction

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def reduceFrac(num, den):
    factor = gcd(num,den)
    num = num // factor
    den = den // factor
    return str(num) + '/' + str(den)

print(decToFrac(1.44))
print(decToFrac(0.4))
print(decToFrac(0.34014))
