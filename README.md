# pymos

[GitHub Repository](https://github.com/hansemso/pymos)

## Description

pymos is a lean fully customizable(no annoying features) fast and interactive command-line calculator built with Python and NumPy and SciPy support. It makes scientific calculations customizable and simplifiable. The interface is powered by `prompt_toolkit` for a smooth CLI experience with row-based input and real-time results.

---

## Features

- Fully modularized customizable structure. 
- Fast C engine (`fastmath.dll`) for numeric evaluation
- ^ and () supported. Ex: (2^(2+3))/3^3+4)^1/2  ⏎  1.749064371
- NumPy supported.  
- F12 returns at top total for results in left column from expressions in right column 
- esc key to refresh inputs
- ans to insert result into new expression...apply numpy to ans to get new result and keep applying and app will keep transition going. Work is savable to continue the next day.
- Accompanying graph that follows your work in graphical representation
- More features on the way 🧑‍💻 

---

## Installation

1. Clone the repository:

```powershell
git clone https://github.com/hansemso/pymos.git
```

---
To Run: 

py -m cli.main

```
pymos/
├─ cli/
│  ├─ __init__.py
│  └─ main.py
├─ engine/
│  ├─ __init__.py
│  ├─ c_engine.py
│  ├─ fastmath.c
│  ├─ fastmath.dll
│  └─ math_engine.py
├─ README.md
```


===========
[PyMOS CLI] --> (writes JSON) --> [Monitor Server] --> (feeds) --> [Browser Graph]

[PyMOS CLI] --writes--> pymos_monitor.json
        |
        v
[Flask server reads JSON] --serves--> Browser (JS fetch)
        |
        v
[Graph or display updates automatically]