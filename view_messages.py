from pprint import pprint

import json

from micro_forum import db

with open(db) as f:
    j = json.load(f)
    pprint(j)