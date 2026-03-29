# engine/calc.py
import numpy as np
import pandas as pd
import math

# ----------------------------
# Basic arithmetic
# ----------------------------
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b if b != 0 else float('inf')

# ----------------------------
# Vector operations
# ----------------------------
def vector_add(v1, v2):
    return np.add(v1, v2)

def vector_dot(v1, v2):
    return np.dot(v1, v2)

# ----------------------------
# Trigonometry
# ----------------------------
def sin_deg(x):
    return math.sin(math.radians(x))

def cos_deg(x):
    return math.cos(math.radians(x))

def tan_deg(x):
    return math.tan(math.radians(x))

# ----------------------------
# Pandas table example
# ----------------------------
def mean_series(data):
    s = pd.Series(data)
    return s.mean()

def std_series(data):
    s = pd.Series(data)
    return s.std()