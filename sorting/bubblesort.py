import time
from sorting.sort import Sort


class BubbleSort(Sort):

    comparison_number = 0

    def sort_array(self):
        time_start = time.time()
        for sorted_index in reversed(range(0, len(self.arr))):
            for ind in range(0, sorted_index):
                self.comparison_number += 1
                if self.arr[ind] > self.arr[ind + 1]:
                    self._swap(ind, ind + 1)
                ind += 1
            sorted_index -= 1
        time_end = time.time()
        self.elapsed_time = (time_end - time_start) * 1000.0
        return self.arr

    def print_measurements(self):
        print("Comparison number: %d" % self.comparison_number)
        self.print_swap()
        self.print_time()

