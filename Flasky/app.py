from flask import Flask

app = Flask(__name__)

DETAILS = [
    {
        'name': 'Admin',
        'email': '',
        'password': 'letmein', 
    }
]

@app.route('/login/<name>/<password>')
def login(name, password):
    pass
