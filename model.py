import json
#simulation of a db with a json
def load_db():
    with open("test_db.json") as t:
        return json.load(t)

db = load_db()