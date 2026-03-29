import ctypes
import os
import re

# Load the DLL
dll_path = os.path.join(os.path.dirname(__file__), "fastmath.dll")
lib = ctypes.CDLL(dll_path)

lib.eval_numeric.restype = ctypes.c_double
lib.eval_numeric.argtypes = [ctypes.c_char_p]
lib.fast_pow.restype = ctypes.c_double
lib.fast_pow.argtypes = [ctypes.c_double, ctypes.c_double]

# Regex to match "number ^ number" (floating point allowed)
number_re = r'\d+(?:\.\d+)?'

def eval_numeric(expr):
    """Evaluate math expression using C engine, supporting ^ and ()."""
    expr = expr.replace(' ', '')  # remove spaces

    # Recursive replacement of ^ operators
    while '^' in expr:
        # This regex finds the rightmost simple exponent to replace first
        # It handles things like 2^3 or 2^(1+2)
        match = re.search(r'(\(?[^\^\(\)]+\)?)\^(\(?[^\^\(\)]+\)?)', expr)
        if not match:
            break
        base, exp = match.groups()
        # Evaluate base and exponent recursively (to handle nested parentheses)
        base_val = lib.eval_numeric(base.encode())
        exp_val = lib.eval_numeric(exp.encode())
        result = lib.fast_pow(base_val, exp_val)
        expr = expr[:match.start()] + str(result) + expr[match.end():]

    # Evaluate the final expression with parentheses using C engine
    return lib.eval_numeric(expr.encode())