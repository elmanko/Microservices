from flask import Flask, render_template,abort,jsonify,request,redirect,url_for
from datetime import datetime
from model import db,save_db

app = Flask(__name__)


@app.route("/")
def welcome():
    #return "Welcome to my Flask app"
    #return render_template("welcome.html",message='Not sure.')
    return render_template(
        "welcome.html",
        querys=db
    )


@app.route("/date")
def date():
    return jsonify('date time is:', str(datetime.now()))
"""
count = 0
@app.route("/views")
def views():
    global count
    count += 1
    return "The view count is " + str(count)
"""

@app.route("/query/<int:index>")
def query_view(index):
    try:
        query=db[index]
        return render_template("query.html",
                                query=query, 
                                index=index,
                                max_index=len(db)-1)
    except IndexError:
        abort(404)

@app.route("/add_query", methods=['GET','POST'])
def add_query():
    if request.method == 'POST':
        #submission
        query= {"value1": request.form['value1'],
                "value2": request.form['value2']}
        db.append(query)
        save_db()
        return redirect(url_for('query_view', index=len(db)-1))
    else:
        return render_template("add_query.html")

@app.route('/remove_query/<int:index>',methods=['GET','POST'])
def remove_query(index):
    try:
        if request.method == 'POST':
            del db[index]
            save_db
            return redirect(url_for('welcome'))
        else:
            return render_template("remove_query.html", query=db[index])
    except IndexError:
        abort(404)

#RESTful API test, returning json

@app.route("/api/query/")
def api_query_list():
    return jsonify(db)

@app.route("/api/query/<int:index>")
def api_query_detail(index):
    try:
        return jsonify(db[index])
    except IndexError:
        abort(404)

