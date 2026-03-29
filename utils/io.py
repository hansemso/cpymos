# utils/io.py
import json

def save_work(rows, path="cpymos_save.json"):
    data = [(l, r) for l, r in rows]
    with open(path, "w") as f:
        json.dump(data, f)

def load_work(path="cpymos_save.json"):
    try:
        with open(path) as f:
            return json.load(f)
    except FileNotFoundError:
        return []