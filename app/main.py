from flask import Flask , render_template ,redirect , url_for
import json
import os

app = Flask(__name__)

@app.route("/home")
def home():
    return '<title>logs</title> <h1>home</h1>'



@app.route('/log')
def log():
    data = json.load(open('./output/output.json'))
    page = '<h1>LOGS</h1>'
    for log_dict in data:
        page += f'<p>{log_dict}</p>'
    return page



@app.route(f'/test/<lol>')
def lol(lol):
    return f'text goo brrrrrrrr \n<h1>{lol}</h1>'
