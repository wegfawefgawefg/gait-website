from flask import Flask
from flask import request
from flask import render_template
import json

import datetime

app = Flask(__name__)

import os

def get_last_n(N=20):
    with open("messages.json") as f:
        j = json.load(f)
        messages = j["messages"]
        last_n = list(reversed(messages[-N:]))
    return last_n

def add_message(message):
    with open("messages.json") as f:
        j = json.load(f)
        messages = j["messages"]
        new_message = {
            "time": datetime.datetime.now().strftime("%c"),
            "msg": message}
        messages.append(new_message)
        
    with open("messages.json", 'w') as f:
        json.dump(j, f)

@app.route('/', methods=['GET'])
def micro_forum():
    if request.method == 'GET':
        new_message = request.args.get('nm')
        if new_message:
            add_message(new_message)

    last_n_message_items = get_last_n()
    return render_template("minimal_forum.html", message_items=last_n_message_items)
