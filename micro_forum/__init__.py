from flask import Flask
db = "messages.json"


app = Flask(__name__)
from .host import *

