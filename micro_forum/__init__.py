from flask import Flask
app = Flask(__name__)
from .host import *

db = "messages.json"
