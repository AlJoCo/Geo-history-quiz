import random
from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from os import getenv

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.config['SECRET_KEY'] = "fdgsdfsdfg"

db = SQLAlchemy(app) 

@app.route('/')
@app.route('/coords', methods=['GET'])
def coords():
    x = str(random.randrange(-85, 85))
    y = str(random.randrange(-180, 180))
    return x + ", " + y

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)