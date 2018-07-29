import time

class Sort:
    swap_number = 0
    elapsed_time = 0

    def __init__(self, array):
        self.arr = array

    def sort(self):
        time_start = time.time()
        self.arr = self.sort_array()
        time_end = time.time()
        self.elapsed_time = (time_end - time_start) * 1000.0
        return self.arr

    def sort_array(self):
        return self.arr

    def _swap(self, ind1, ind2):
        self.swap_number += 1
        tmp = self.arr[ind1]
        self.arr[ind1] = self.arr[ind2]
        self.arr[ind2] = tmp

    def print_swap(self):
        print("Swap number: %d" % self.swap_number)

    def print_time(self):
        print("Elapsed time: %s" % str(self.elapsed_time))