import os
import json
from flask import Flask

db = "messages.json"

if not os.path.isfile(db):
    with open("./default_messages.json") as f:
        j = json.load(f)
    with open(db, "w") as f:
        json.dump(j, f)

app = Flask(__name__)
from .host import *
