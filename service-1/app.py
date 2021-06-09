import random
import requests
from flask import Flask, render_template, redirect, url_for, request, jsonify
from flask_wtf import FlaskForm
from wtforms import BooleanField, SubmitField
from flask_sqlalchemy import SQLAlchemy
from os import getenv

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.config['SECRET_KEY'] = getenv('SECRET_KEY')

db = SQLAlchemy(app) 

class Storage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Coords = db.Column(db.String(50), nullable=False)
    Date = db.Column(db.String(50), nullable=False)
    Survivable = db.Column(db.Boolean)

class Form(FlaskForm):
    Survivable = BooleanField("Could you survive?")
    Submit = SubmitField("Submit")

@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def home():
    coords = requests.get('http://service-2:5000/get_coords').text
    date = requests.get('http://service-3:5000/get_date').json()
    form = Form()
    queryall = Storage.query.all()
    if form.validate_on_submit():
        new_entry = Storage(Coords = coords, Date = date, Survivable = form.data)
        db.session.add(new_entry)
        db.session.commit()
    return render_template('home.html',coords=coords, date=date, queryall=queryall, form=form)

if __name__ == "__main__": 
    app.run(host="0.0.0.0", port=5000, debug=True)