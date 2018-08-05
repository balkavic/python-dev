import utilities.inputgenerator as inputgen
import utilities.filehandler as filehandler
from datastructures.priqueue import PriQueueUnsortedArray, PriQueueUnsortedArrayImproved
from sorting.bubblesort import BubbleSort
from datastructures import queue

arr = inputgen.generate_int_array(10, 0, 100)

print(arr)

filehandler.write_array_to_file(arr, "input_file.txt")

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

# arr.sort(reverse=True)
#
# print(arr)
#
# bubble_sort = BubbleSort(arr)
#
# print(bubble_sort.sort())
#
# bubble_sort.print_measurements()

pri_queue_unsorted = PriQueueUnsortedArray(10)
pri_queue_unsorted_improved = PriQueueUnsortedArrayImproved(10)

for element in arr:
    pri_queue_unsorted.insert(element)
    pri_queue_unsorted_improved.insert(element)

while not pri_queue_unsorted.isEmpty():
    print(pri_queue_unsorted.del_max())

while not pri_queue_unsorted_improved.isEmpty():
    print(pri_queue_unsorted_improved.del_max())

print("Unsorted:")
pri_queue_unsorted.print_measurements()

print("Improved unsorted:")
pri_queue_unsorted_improved.print_measurements()


