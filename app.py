from flask import Flask, render_template
import random
import string

app = Flask(__name__)

def generate_password(length=12):
    """Generate a random password."""
    characters = string.ascii_letters + string.digits + string.punctuation
    
    password = ''
    for i in range(length):
        random_character = random.choice(characters)
        password += random_character
    
    return password

@app.route('/') 
def index():
    password = generate_password()
    return render_template('index.html', password=password)

if __name__ == '__main__':
    app.run(debug=True)
