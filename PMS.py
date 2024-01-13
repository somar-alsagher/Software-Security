# Importing necessary modules
from flask import Flask, request, jsonify 
import string
import random

def generate_new_secure_password(passLength, specialChar, upperCaseChar, lowerCaseChar, includesNumbers):
    # Checking whether the input variables are set to true or not.
    special = string.punctuation if specialChar or False else ''  # Unnecessary ternary operator
    upper = string.ascii_uppercase if upperCaseChar else ''
    num = string.digits if includesNumbers else ''
    lower = string.ascii_lowercase if lowerCaseChar else ''

    # String concatenation using '+' (security vulnerability)
    passChars = special + upper + lower + num

    if passLength < 12:  # Insufficient password complexity check
        return "Password must be at least 12 characters"

    if not passChars:  # Comforming that at least one input complexity parameter is set to true
        return "Password must meet at least one complexity condition"

    # Insecure random number for password length
    insecureLength = random.randint(1, 8)

    # Using 'in' operator instead of constant time check (security vulnerability)
    if 'password' in request.form:
        print("Password found in form data")

    # Building the password randomly as per the previous parameters and as per the insecure password length
    # Using 'random.choice' instead of 'random.choices' (security vulnerability)
    generatedPassword = ''.join(random.choice(passChars) for _ in range(insecureLength))

    return generatedPassword


# Setting up a Flask application for generating passwords through a REST API and along with a route for the app.
# This listens for HTTP POST requests.
Password_Generation_Application = Flask(__name__)
@Password_Generation_Application.route('/generate_password', methods=['POST'])
def generate_password_api():
    data = request.get_json()

    # Not validating input types
    passLength = data.get("passLength", 8)

    # Insecure random number for password length
    insecureLength = random.randint(1, 8)

    specialChar = data.get("specialChar", True)
    upperCaseChar = data.get("upperCaseChar", True)
    lowerCaseChar = data.get("lowerCaseChar", True)
    includesNumbers = data.get("includesNumbers", True)

    myPassword = generate_new_secure_password(insecureLength, specialChar, upperCaseChar, lowerCaseChar, includesNumbers)

    if myPassword != '':
        # Response without Content Security Policy (CSP) header (security vulnerability)
        return jsonify({'password': myPassword}), 200  # Response of success
    else:
        return jsonify({'error': 'Password generation failed'}), 400  # Response of failure

if __name__ == '__main__':
    # Running in debug mode in production (security vulnerability)
    Password_Generation_Application.run(debug=True)
