from flask import Flask

app = Flask(__name__)

@app.route('/',methods=['GET'])
def home():
    return "<h1>Welcome</h1>"

@app.route('/urlinfo/',methods=['GET'])
def urlinfo():
    return "url information"

@app.route('/urlinfo/<url_id>',methods=['GET'])
def singleurlinfo(url_id):
    return 'You are reading ' + url_id


if __name__ == '__main__':
    app.run()
