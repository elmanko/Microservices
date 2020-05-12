from flask import Flask, render_template
#from datetime import datetime
from model import db

app = Flask(__name__)


@app.route("/")
def welcome():
    #return "Welcome to my Flask app"
    return render_template("welcome.html",message='Not sure.')

"""
@app.route("/date")
def date():
    return "The datetime is " + str(datetime.now())

count = 0
@app.route("/views")
def views():
    global count
    count += 1
    return "The view count is " + str(count)
"""

@app.route("/query/<int:index>")
def query(index):
    query=db[index]
    return render_template("query.html",query=query)
