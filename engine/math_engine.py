import numpy as np
import pandas as pd

class Engine:
    def __init__(self):
        self.rows = []

    def add_row(self, left_text="", right_text=""):
        self.rows.append([left_text, right_text])
        return self.rows[-1]

    def eval_row(self, index):
        left, right = self.rows[index]
        expr = right.strip()
        if expr and not expr.startswith("#"):
            try:
                val = eval(expr, {"__builtins__": None}, {"np": np, "pd": pd})
            except Exception:
                val = "Error"
            self.rows[index][0] = str(val)
        else:
            self.rows[index][0] = ""
        return self.rows[index][0]

    def eval_all(self):
        total = 0
        for i in range(len(self.rows)):
            left, right = self.rows[i]
            expr = right.strip()
            if expr and not expr.startswith("#"):
                try:
                    total += eval(expr, {"__builtins__": None}, {"np": np, "pd": pd})
                except Exception:
                    pass
        return total

    def save(self, filename="cpymos_save.json"):
        import json
        with open(filename, "w") as f:
            json.dump(self.rows, f)

    def load(self, filename="cpymos_save.json"):
        import json
        try:
            with open(filename) as f:
                self.rows = json.load(f)
        except FileNotFoundError:
            self.rows = []