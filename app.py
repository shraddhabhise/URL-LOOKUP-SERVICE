from flask import Flask
from flask import request
from flask import render_template
import re

import sqlite3

app = Flask(__name__)

@app.route('/',methods=['GET'])
def home():
    return "<h1>Welcome</h1>"

@app.route('/list')
def list():
    con = sqlite3.connect("database.db")
    con.row_factory = sqlite3.Row

    cur = con.cursor()
    cur.execute("select * from malwarehosts")

    rows = cur.fetchall();

    return render_template("list.html", rows=rows)

@app.route('/checkurl')
def new_url():
   return render_template("checkurl.html")


@app.route('/isvalid',  methods=['POST', 'GET'])
def isvalid():
    if request.method == 'POST':
        ur = request.form['url']
        isVALID=False
        isPresent=False

        regex = re.compile(
            r'^(?:http|ftp)s?://'  # http:// or https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
            r'localhost|'  # localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
            r'(?::\d+)?'  # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)

        match = re.search(regex, ur)
        if not match:
            msg= "malformed url. Enter proper format of url"

        else:
            hostname=match.group().strip(r'^(?:http|ftp)s?://')
            print("hostname", hostname)

            conn = sqlite3.connect("database.db")

            #check/search  in database and change ispresent flag
            print("Opened database successfully for searching malware")
            try:
                with conn:
                    conn.row_factory = sqlite3.Row
                    cur = conn.cursor()
                    cur.execute("select * from malwarehosts where url=?", (hostname,))
                    rows= cur.fetchone()
                    if rows:
                        isPresent=True

            except sqlite3.IntegrityError:
                    print("Database operation failed")
            conn.close()


            if isPresent==False:
                msg="Safe and valid URL. You can proceed to use it."
            else:
                msg = "Malware URL and is not safe to use"



    return render_template("result.html", msg=msg)

@app.route('/addmalware')
def new_malware():
   return render_template('malware.html')


@app.route('/add', methods=['POST', 'GET'])
def add():
    if request.method == 'POST':
        ur = request.form['url']
        print(ur)
        conn = sqlite3.connect("database.db")
        print("Opened database successfully")
        try:
            with conn:

                conn.execute("insert into malwarehosts (url) values (?)", (ur,))
                msg = "Record successfully added"
        except sqlite3.IntegrityError:
            print("couldn't add")
        conn.close()


        return render_template("result.html", msg=msg)


if __name__ == '__main__':
    #app.run()
    app.run(host="0.0.0.0", debug=True)



