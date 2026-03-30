# CPyMOS

[GitHub Repository](https://github.com/hansemso/cpymos)

## Description

CPyMOS is a lean fully customizable(no annoying features) fast and interactive command-line calculator built with Python, a C engine, and NumPy support. It supports standard math operations, exponentiation, parentheses, and advanced NumPy array operations. The interface is powered by `prompt_toolkit` for a smooth CLI experience with row-based input and real-time results.

---

## Features

- Fully modularized customizable structure. 
- Fast C engine (`fastmath.dll`) for numeric evaluation
- ^ and () supported. Ex: (2^(2+3))/3^3+4)^1/2  ⏎  1.749064371
- NumPy supported.  
- F12 returns at top total for results in left column from expressions in right column 
- esc key to refresh inputs
- ans to insert result into new expression
-🧑‍💻 More features on the way

---

## Installation

1. Clone the repository:

```powershell
git clone https://github.com/hansemso/cpymos.git
```

---
To Run: 

py -m cli.main

```
cpymos/
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