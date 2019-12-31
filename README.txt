First:
 pip install Flask
 pip install Flask-PyMongo 
 pip install dnspython if it isn't installed
Second (powershell): 
 $env:FLASK_APP = "projj.py"
 $env:FLASK_DEBUG = 1 
 FLASK run
Next, add a PyMongo to your code:
from flask import Flask
from flask_pymongo import PyMongo 

app = Flask(__name__)  
app.config['MONGO_URI'] = 'mongodb+srv://oum:123456KK@oum-kcdhs.mongodb.net/test?retryWrites=true&w=majority'
mongo = PyMongo(app) 

PyMongo connects to the MongoDB server running on port 27017 on localhost(Default), 
to the database. This database is exposed as the db attribute. 
