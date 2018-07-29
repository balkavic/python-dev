import random

def generate_int_array(size, min, max):
    return [random.randrange(min, max) for _ in range(size)]

def generate_int_matrix(rows, cols, min, max):
    return [[random.randrange(min, max) for _ in range(cols)] for _ in range(rows)]




