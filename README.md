# CPyMOS

[GitHub Repository](https://github.com/hansemso/cpymos)

## Description

CPyMOS is a fast and interactive command-line calculator built with Python, a C engine, and NumPy support. It supports standard math operations, exponentiation, parentheses, and advanced NumPy array operations. The interface is powered by `prompt_toolkit` for a smooth CLI experience with row-based input and real-time results.

---

## Features

- Fast C engine (`fastmath.dll`) for numeric evaluation
- Exponentiation with `^`
- Parentheses `()` supported for grouping
- NumPy array operations (e.g., `np.array([1,2,3]) + np.array([4,5,6])`)
- Interactive row-based CLI with:
  - Enter to evaluate
  - Up/Down arrows to navigate
  - esc key to refresh inputs
  - F12 to sum answer column
  - ans to insert answer in new expression

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