#Importing necessary modules
from flask import Flask, request, jsonify 
import string
import random

def generate_new_secure_password(passLength, specialChar, upperCaseChar, lowerCaseChar, includesNumbers) :
    #Checking whether the input variabls are set to true or not.
    special = string.punctuation if specialChar else '' #
    upper = string.ascii_uppercase if upperCaseChar else ''
    num = string.digits if includesNumbers else ''
    lower = string.ascii_lowercase if lowerCaseChar else ''

    passChars = special + upper + lower + num #Composing the password out of the declared proporties parameters
    if passLength < 8 :
       return "Password must be at least 8 characters"
    elif not passChars: #Comforming that at least of the input complexity parameters are set to true
        return "Password must meet at least one complexity condition"
    else :
        #Builidng the password randowmly as per the previous paramenters and as per the password_length variable
        generatedPassword = ''.join(random.choice(passChars) for _ in range(passLength))
        return generatedPassword


#Seting up a Flask application for generating passwords through a REST API and along with a route for the app. This listens for HTTP POST requests.
Password_Generation_Application = Flask(__name__)
@Password_Generation_Application.route('/generate_password', methods=['POST'])
def generate_password_api():
    data = request.get_json()
    passLength = data.get("passLength", 8)
    specialChar = data.get("specialChar", True)
    upperCaseChar = data.get("upperCaseChar", True)
    lowerCaseChar = data.get("lowerCaseChar", True)
    includesNumbers = data.get("includesNumbers", True)
    myPassword = generate_new_secure_password(passLength, specialChar, upperCaseChar, lowerCaseChar, includesNumbers)
    
    if myPassword != '':
      return jsonify({'password': myPassword}), 200  # Responce of success
    else:
      return jsonify({'error': 'Password generation failed'}), 400 # Responce of failure





if __name__ == '__main__':
    Password_Generation_Application.run(debug=False) #No Debug
