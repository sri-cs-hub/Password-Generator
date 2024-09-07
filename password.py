from flask import Flask, render_template, request, jsonify
import random
import string
import re

app = Flask(__name__)

def password_generator(length, symbols):
    characters = string.ascii_letters + string.digits
    if symbols:
        characters += string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate-password', methods=['GET'])
def generate_password():
    try:
        length = int(request.args.get('length', 12))
        symbols = request.args.get('symbols', 'false').lower() == 'true'
        password = password_generator(length, symbols)
        return jsonify({"password": password})
    except ValueError:
        return jsonify({"error": "Invalid length parameter. Please provide a valid integer."}), 400

if __name__ == "__main__":
    app.run(debug=True)
