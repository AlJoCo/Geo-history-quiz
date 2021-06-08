import requests
from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import BooleanField, SubmitField
from service-1 import form, Storage
from os import getenv

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

db = SQLAlchemy(app) 

@app.route('/submission', methods=['GET', 'POST'])
def submission():
    form = form()
    queryall = Storage.query.all()
    if form.validate_on_submit():
        new_entry = Storage(Coords = service-2.data, Date = service-3.json, Survivable = form.data)
        db.session.add(new_entry)
        db.session.commit()
    return render_template('home.html', queryall=queryall, form=form)