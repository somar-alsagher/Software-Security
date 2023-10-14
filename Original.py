import string
import random

def generate_new_secure_password (passLength,  specialChar = True,  upperCaseChar = True,  lowerCaseChar = True, includesNumbers=True) :

    special = string.punctuation if specialChar  else ''
    upper   = string.ascii_lowercase if upperCaseChar else ''
    num = string.digits if includesNumbers else  '' 
    lower = string.ascii_lowercase if lowerCaseChar else ''

    passChars = special + upper + lower + num
    if not passChars : #Checking if none of the parameters is True
        print ("Password must meet at least one complexity condition") #Printing a message in case all supplied complexity paramters are false
        return None
    
    generatedPassword = ''.join(random.choice(passChars) for _ in range (passLength))
    return generatedPassword


myPassword = generate_new_secure_password(passLength = 8, specialChar = True,  upperCaseChar = True,  lowerCaseChar = True, includesNumbers=True)
print("Generated Password:", myPassword)