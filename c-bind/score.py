# cpymos/c-bind/score.py
import ctypes

lib = ctypes.CDLL("../pymos-cpp/libcalcscore.so")

def calculate_score(durations):
    n = len(durations)
    arr = (ctypes.c_int * n)(*durations)
    result = lib.calculate_score(arr, n)
    return result
    
  
from score import calculate_score

durations = [5, 10, 15]
total = calculate_score(durations)
print(total)  # 30