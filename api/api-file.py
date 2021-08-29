from flask import Flask
from flask import json
from flask import request
from flask import Response
from flask import render_template
import re
import validators

import sqlite3

app = Flask(__name__)


DATABASE = "/Users/shraddhabhise/PycharmProjects/URL-LOOKUP-SERVICE/api/database.db"

@app.route('/',methods=['GET'])
def home():
    return "<h1>Welcome</h1>"

@app.route('/add', methods=['POST', 'GET'])
def add():
    if request.method == 'POST':
        ur = request.form['url']
        print(ur)
        conn = sqlite3.connect("/Users/shraddhabhise/PycharmProjects/URL-LOOKUP-SERVICE/api/database.db")
        print("Opened database successfully")
        try:
            with conn:

                conn.execute("insert into malwarehosts (url) values (?)", (ur,))
                msg = "Record successfully added"
        except sqlite3.IntegrityError:
            print("couldn't add")
        conn.close()


        return render_template("result.html", msg=msg)


@app.route('/list')
def list():
    con = sqlite3.connect("/Users/shraddhabhise/PycharmProjects/URL-LOOKUP-SERVICE/api/database.db")
    con.row_factory = sqlite3.Row

    cur = con.cursor()
    cur.execute("select * from malwarehosts")

    rows = cur.fetchall();

    return render_template("list.html", rows=rows)


@app.route('/addmalware')
def new_malware():
   return render_template('malware.html')

if __name__ == '__main__':
    app.run()
