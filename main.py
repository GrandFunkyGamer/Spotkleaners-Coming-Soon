from google.appengine.ext import ndb
from flask import Flask, render_template, request, redirect

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/')
def home():
	return render_template('index.html')


