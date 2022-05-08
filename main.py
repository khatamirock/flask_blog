from ast import Dict
import flask
from flask import Flask, render_template, request, redirect, url_for
import requests
import json
app = Flask(__name__)

ls={}


url='https://jsonplaceholder.typicode.com/posts'



@app.route('/')
def index():
    global ls
    ls = requests.request("GET", url).json()

    return render_template('index.html',data=ls)

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/post/<int:dat>')
def post(dat):
    data=ls[dat-1]
    return render_template('post.html',data=data)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/home')
def home():
    return render_template('index.html')






app.run(debug=True)