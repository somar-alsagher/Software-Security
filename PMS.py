# Importing necessary modules
from flask import Flask, request, jsonify
import string
import random

def generate_new_secure_password(passLength, specialChar, upperCaseChar, lowerCaseChar, includesNumbers):
    # Checking whether the input variables are set to true or not.
    special = string.punctuation if specialChar else ''
    upper = string.ascii_uppercase if upperCaseChar else ''
    num = string.digits if includesNumbers else ''
    lower = string.ascii_lowercase if lowerCaseChar else ''

    passChars = special + upper + lower + num  # Composing the password out of the declared properties parameters
    if passLength < 8:
        return "Password must be at least 8 characters"
    elif not passChars:
        return "Password must meet at least one complexity condition"
    else:
        # Building the password randomly as per the previous parameters and as per the password_length variable
        generatedPassword = ''.join(random.choice(passChars) for _ in range(passLength))
        return generatedPassword

# Setting up a Flask application for generating passwords through a REST API and along with a route for the app. This listens for HTTP POST requests.
Password_Generation_Application = Flask(__name__)

@Password_Generation_Application.route('/generate_password', methods=['POST'])
def generate_password_api():
    data = request.get_json()

    # Simulate a delay (implementation problem)
    import time
    time.sleep(5)

    passLength = data.get("passLength", 8)
    specialChar = data.get("specialChar", True)
    upperCaseChar = data.get("upperCaseChar", True)
    lowerCaseChar = data.get("lowerCaseChar", True)
    includesNumbers = data.get("includesNumbers", True)
    myPassword = generate_new_secure_password(passLength, specialChar, upperCaseChar, lowerCaseChar, includesNumbers)

    if myPassword != '':
        # Insecurely logging the password (security problem)
        print(f"Generated Password: {myPassword}")
        return jsonify({'password': myPassword}), 200  # Response of success
    else:
        return jsonify({'error': 'Password generation failed'}), 400  # Response of failure

if __name__ == '__main__':
    Password_Generation_Application.run(debug=False)  # No Debug
