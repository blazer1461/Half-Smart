def encryptString (theString, rotation):
    rotation %= 26
    encrypted = ""
    length = len(theString)
    for ex in xrange(length):
        tempStr = theString[ex]
        #print tempStr
        tempInt = ord(tempStr)
        #print tempInt
        if (tempInt >= 65 and tempInt <= 90) or (tempInt >= 97 and tempInt <= 122):#check if letter
            temp = tempInt + rotation
            #print temp
            if (temp >= 97 and temp <= 122) or (temp >= 65 and temp <= 90):#check is rotation does not need help
                encrypted += chr(temp)
            elif temp > 122:
                 encrypted += chr(temp - 26)
            elif temp > 90 and temp < 110:
                encrypted += chr(temp - 26)
            else:
                encrypted += chr(temp)
        else:
            encrypted += tempStr
    return encrypted
        
def decryptString (theString, key):
    return encryptString (theString, 26-key)

