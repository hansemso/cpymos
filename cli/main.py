# cli/main.py
from prompt_toolkit import Application
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.widgets import TextArea
from prompt_toolkit.layout import HSplit, Layout, VSplit
from prompt_toolkit.styles import Style
from engine import c_engine
import numpy as np
import json

# -------------------- Globals --------------------
rows = []
cursor_row = 0
result_row = TextArea(height=1, focusable=False, style="class:result")
container = HSplit([result_row])  # result at top

# -------------------- Row Management --------------------
def add_row():
    left = TextArea(height=1, focusable=False, style="class:left")
    right = TextArea(height=1, style="class:right")
    rows.append((left, right))
    container.children.append(VSplit([left, right], padding=3))
    return left, right

def format_result(val):
    if isinstance(val, np.ndarray):
        # Convert to list and format each element
        return "[" + " ".join(str(x) for x in val.tolist()) + "]"
    elif isinstance(val, (int, float)):
        return f"{val:g}"
    else:
        return str(val)

def commit_row(event):
    global cursor_row
    left, right = rows[cursor_row]
    expr = right.text.strip()
    if expr:
        val = evaluate(expr)
        left.text = format_result(val)
    else:
        left.text = ""
    # Move cursor down
    if cursor_row < len(rows) - 1:
        cursor_row += 1
        event.app.layout.focus(rows[cursor_row][1])
    else:
        add_row()
        cursor_row += 1
        event.app.layout.focus(rows[cursor_row][1])

def evaluate(expr):
    """Evaluate expression: use C engine for math, Python/NumPy for np.array etc."""
    expr = expr.strip()
    if "np." in expr:   # detect numpy anywhere in the expression
        try:
            return eval(expr, {"np": np, "__builtins__": __builtins__})
        except Exception:
            return "Error"
    else:
        try:
            return c_engine.eval_numeric(expr)
        except Exception:
            return "Error"


def execute_all():
    total = 0
    for left, right in rows:
        expr = right.text.strip()
        if expr:
            val = c_engine.eval_numeric(expr)
            if isinstance(val, (int, float)):
                total += val
    result_row.text = str(total)

def clear_all():
    result_row.text = ""
    for left, right in rows:
        left.text = ""
        right.text = ""
    rows.clear()
    for _ in range(10):
        add_row()
    global cursor_row
    cursor_row = 0
    app.layout.focus(rows[0][1])

# -------------------- Initialize Rows --------------------
for _ in range(10):
    add_row()

# -------------------- Key Bindings --------------------
kb = KeyBindings()

@kb.add("enter")
def enter(event):
    commit_row(event)

@kb.add("f12")
def total(event):
    execute_all()

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
def refresh(event):
    global cursor_row
    # Clear all input rows
    for left, right in rows:
        right.text = ""
        left.text = ""
    # Move cursor to the first row
    cursor_row = 0
    event.app.layout.focus(rows[0][1])

    
    
# -------------------- Styles --------------------
style = Style.from_dict({
    "left": "fg:white",
    "right": "fg:white",
    "result": "fg:blue",
    "textarea.focused": "fg:black bg:green bold"
})

# -------------------- Application --------------------
app = Application(
    layout=Layout(container),
    key_bindings=kb,
    style=style,
    full_screen=True
)

if __name__ == "__main__":
    app.run()