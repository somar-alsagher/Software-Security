from flask import Flask, request, jsonify
import string
import random

app = Flask(__name__)

def generate_new_secure_password(passLength, specialChar=True, upperCaseChar=True, lowerCaseChar=True, includesNumbers=True) :
    special = string.punctuation if specialChar else ''
    upper = string.ascii_uppercase if upperCaseChar else ''
    num = string.digits if includesNumbers else ''
    lower = string.ascii_lowercase if lowerCaseChar else ''

    passChars = special + upper + lower + num
    if not passChars:
        return "Password must meet at least one complexity condition"
    
    generatedPassword = ''.join(random.choice(passChars) for _ in range(passLength))
    return generatedPassword

@app.route('/generate_password', methods=['POST'])
def generate_password_api():
    data = request.get_json()

    myPassword = generate_new_secure_password(passLength = 8, specialChar = True,  upperCaseChar = True,  lowerCaseChar = True, includesNumbers=True)
    
    if myPassword:
     return jsonify({'password': myPassword}), 200  #Success code
    else:
     return jsonify({'error': 'Password generation failed'}), 400 #Failure Code

if __name__ == '__main__':
    app.run(debug=False) #No Debug


"""
curl -X POST -H "Content-Type: application/json" -d '{
  "passLength": 16,
  "specialChar": true,
  "upperCaseChar": true,
  "lowerCaseChar": true,
  "includesNumbers": true"
}' http://127.0.0.1:5000/generate_password
"""