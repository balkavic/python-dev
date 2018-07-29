import utilities.inputgenerator as inputgen
import utilities.filehandler as filehandler
from sorting.bubblesort import BubbleSort

arr = inputgen.generate_int_array(50, 0, 100)

print(arr)

# filehandler.write_array_to_file(arr, "input_file.txt")
#
# file_array = filehandler.read_array_from_file("input_file.txt")

# print(file_array)

# matr = inputgen.generate_int_matrix(4, 3, 0, 100)
#
# for row in matr:
#     print(row)
#
# filehandler.write_matrix_to_file(matr, 'input_matrix.txt')
#
# file_matrix = filehandler.read_matrix_from_file('input_matrix.txt')
#
#
# for row in file_matrix:
#     print(row)

arr.sort(reverse=True)

print(arr)

bubble_sort = BubbleSort(arr)

print(bubble_sort.sort())

bubble_sort.print_measurements()


