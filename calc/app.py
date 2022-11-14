# Put your app in here.
#from typing_extensions import Required
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

'''
Author: Mahad Osman
Date: Nov 14
Exercise: Flask Greet and Calc
'''

''' An application to handle simple mathematical operations. 

-----------------
Dependent:
Opertions.py


'''

ops = {
    "add": add,
    "subtract": sub,
    "multiply": mult,
    "divide": div
}

@app.route("/")
def index ():
    ''' Home index'''
    return "<h1>Welcome to the home calculator page!</h1>"

# @app.route("/add")
# def adding():
#     a = int(request.args.get("a"))
#     b = int(request.args.get("b"))
#     sum = add(a,b)
#     return f"<h2>The sum of {a} + {b} is = {sum}<h2>"

# @app.route("/sub")
# def subtract():
#     a = int(request.args.get("a"))
#     b = int(request.args.get("b"))
#     sum = sub(a,b)
#     return f"<h2>The sum of {a} - {b} is = {sum}<h2>"

# @app.route("/multi")
# def multiply():
#     a = int(request.args.get("a"))
#     b = int(request.args.get("b"))
#     sum = mult(a,b)
#     return f"<h2>The sum of {a} * {b} is = {sum}<h2>"

# @app.route("/div")
# def divide():
#     a = int(request.args.get("a"))
#     b = int(request.args.get("b"))
#     sum = div(a,b)
#     return f"<h2>The sum of {a} / {b} is = {sum}<h2>"


@app.route('/operation/<op>')
def get_operation(op):
    '''An function to receive our indicated math operation and return the approriate sum. 
    It will use our dict to call the correct operation. 
    ------------------
    Arguments
    - op: Operator value route parameter
    ------------------
    '''
    operation = ops.get(op, "Operation not in list")
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    sum = operation(a,b)
    return f"<h2>The sum of {a} {op} {b} is = {sum}<h2>" 