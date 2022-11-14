from flask import Flask

app = Flask(__name__)
'''
Author: Mahad Osman
Date: Nov 14
Exercise: Flask Greet and Calc
'''

""" Welcome messages application!"""

@app.route('/')
def show_home():
    """ Home page message"""
    return "<h1> Welcome to the home page </h1>" 

@app.route('/welcome')
def welcome_page():
    """ Welcome page message"""
    return "<h1> Welcome</h1>"

@app.route('/welcome/home')
def welcomeHome_page():
    """ Welcome home message"""
    return "<h1> Welcome Home</h1>"

@app.route('/welcome/back')
def welcomeBack_page():
    """ Welcome back message"""
    return "<h1> Welcome Back</h1>"