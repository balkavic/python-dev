def write_array_to_file(arr, filename):
    with open(filename, 'w') as f:
        f.write(' '.join(map(str, arr)))

def read_array_from_file(filename):
    with open(filename, 'r') as f:
        line = f.read()
        arr = list(map(int, line.split(' ')))
        return arr

def write_matrix_to_file(matrix, filename):
    with open(filename, 'w') as f:
        for row in matrix:
            f.write(' '.join(map(str, row)) + "\n")

def read_matrix_from_file(filename):
    matrix = []
    with open(filename, 'r') as f:
        for line in f:
            matrix.append(list(map(int, line.split(' '))))
    return matrix

