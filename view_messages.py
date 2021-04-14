from pprint import pprint

import json

from micro_forum import db

j = json.load(db)
pprint(j)