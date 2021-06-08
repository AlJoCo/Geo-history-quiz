import requests
from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import BooleanField
from os import getenv

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.config['SECRET_KEY'] = "fdgsdfsdfg"

db = SQLAlchemy(app) 

class Storage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    longitude = db.Column(db.String(50), nullable=False)
    #y axis
    latitude = db.Column(db.String(50), nullable=False)
    #x axis
    Date = db.Column(db.String(50), nullable=False)
    Survivable = db.Column(db.Boolean)

class form(FlaskForm):
    Survivable = BooleanField("Is this survivable?")

def newcharacter():
    form = form()
    queryall = Storage.query.all()
    if form.validate_on_submit():
        new_entry = Storage(longitude = y.service-2.data)
        db.session.add(new_entry)
        db.session.commit()
    return render_template('newcharacter.html', queryall=queryall, form=form)