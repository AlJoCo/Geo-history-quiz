import random
import requests
from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from os import getenv

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.config['SECRET_KEY'] = "fdgsdfsdfg"

db = SQLAlchemy(app) 

@app.route('/')
@app.route('/home', methods=['GET'])
def home():
    coords = request.get('http://geo_history_api:5000/get_coords')
    date = request.get('http://geo_history_api:5000/get_date')
    return render_template('home.html',coords=coords.text,date=date.text)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)