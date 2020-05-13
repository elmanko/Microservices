import json
#simulation of a db with a json
def load_db():
    with open("test_db.json") as t:
        return json.load(t)

def save_db():
    with open("test_db.json", "w") as t:
        return json.dump(db,t)
        
db = load_db()