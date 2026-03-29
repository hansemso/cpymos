# cli/main.py
from prompt_toolkit import Application
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.widgets import TextArea
from prompt_toolkit.layout import HSplit, Layout, VSplit
from prompt_toolkit.styles import Style
import json
import numpy as np
import pandas as pd

rows = []
cursor_row = 0
result_row = TextArea(height=1, focusable=False)

# -------------------- Functions --------------------
def add_row():
    left = TextArea(height=1, focusable=False, style="class:left")
    right = TextArea(height=1, style="class:right")
    rows.append((left, right))
    container.children.append(VSplit([left, right], padding=3))
    return left, right

def commit_row(event):
    global cursor_row
    left, right = rows[cursor_row]
    expr = right.text.strip()
    if expr and not expr.startswith("#"):
        try:
            val = eval(expr, {"__builtins__": None}, {"np": np, "pd": pd})
        except:
            val = "Error"
        left.text = str(val)
    else:
        left.text = ""
    if cursor_row < len(rows) - 1:
        cursor_row += 1
        event.app.layout.focus(rows[cursor_row][1])

def execute_all():
    total = 0
    for left, right in rows:
        expr = right.text.strip()
        if expr and not expr.startswith("#"):
            try:
                total += eval(expr, {"__builtins__": None}, {"np": np, "pd": pd})
            except:
                pass
    result_row.text = str(total)

def save_work():
    data = [(left.text, right.text) for left, right in rows]
    with open("cpymos_save.json", "w") as f:
        json.dump(data, f)

def load_work():
    try:
        with open("cpymos_save.json") as f:
            data = json.load(f)
            for i, (l, r) in enumerate(data):
                if i >= len(rows): add_row()
                rows[i][0].text = l
                rows[i][1].text = r
    except FileNotFoundError:
        pass

# -------------------- Layout --------------------
container = HSplit([result_row])
for _ in range(10):
    add_row()
load_work()

# -------------------- Key Bindings --------------------
kb = KeyBindings()
@kb.add("enter")
def enter(event): commit_row(event)
@kb.add("f12")
def total(event): execute_all()
@kb.add("c-s")
def save(event): save_work()
@kb.add("up")
def up(event):
    global cursor_row
    if cursor_row > 0:
        cursor_row -= 1
        event.app.layout.focus(rows[cursor_row][1])
@kb.add("down")
def down(event):
    global cursor_row
    if cursor_row < len(rows) - 1:
        cursor_row += 1
        event.app.layout.focus(rows[cursor_row][1])
@kb.add("escape")
def exit_app(event): event.app.exit()

# -------------------- Styles --------------------
style = Style.from_dict({
    "left": "fg:white",
    "right": "fg:white",
    "textarea.focused": "fg:black bg:green bold"
})

# -------------------- Application --------------------
app = Application(
    layout=Layout(container),
    key_bindings=kb,
    style=style,
    full_screen=True
)
app.run()