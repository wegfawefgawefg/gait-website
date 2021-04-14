import json
import datetime

from flask import Flask
from flask import request
from flask import render_template
from flask import url_for, redirect

from micro_forum import app, db

def get_last_n(N=20):
    with open(db) as f:
        j = json.load(f)
        messages = j["messages"]
        last_n = list(reversed(messages[-N:]))
    return last_n

def add_message(message):
    with open(db) as f:
        j = json.load(f)
        messages = j["messages"]
        new_message = {
            "time": datetime.datetime.now().strftime("%c"),
            "msg": message}
        messages.append(new_message)
        
    with open(db, 'w') as f:
        json.dump(j, f)

@app.route('/', methods=['GET'])
def main():
    if request.method == 'GET':
        new_message = request.args.get('nm')
        if new_message:
            if len(new_message) < 10000:
                add_message(new_message)
                return redirect(url_for('main'))

    last_n_message_items = get_last_n()
    return render_template("minimal_forum.html", message_items=last_n_message_items)