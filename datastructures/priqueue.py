class PriQueue:
    comp_number = 0
    assignment_number = 0
    current_index = 0
    arr = []

    def __init__(self, size):
        self.size = size
        self.arr = [None] * size

    def insert(self, element):
        pass

    def max(self):
        pass

    def del_max(self):
        pass

    def isEmpty(self):
        return self.current_index < 1

    def print_measurements(self):
        print("Comparison number: %d" % self.comp_number)
        print("Assignment number: %d" % self.assignment_number)

class PriQueueUnsortedArray(PriQueue):

    def search_max(self):
        if self.current_index == 0:
            print("Array is empty!")
            return -1
        max_index = 0
        max_element = self.arr[0]
        for i in range(1, self.current_index):
            self.comp_number += 1
            if self.arr[i] > max_element:
                max_index = i
                max_element = self.arr[i]
        return max_index

    def insert(self, element):
        if self.current_index == self.size:
            print("ERROR, size '%d' is exceeded!" % self.size)
            return None
        self.arr[self.current_index] = element
        self.current_index += 1
        self.assignment_number += 1

    def max(self):
        if self.current_index == 0:
            print("ERROR, array is empty!")
            return None
        self.assignment_number += 1
        return self.arr[self.search_max()]

    def del_max(self):
        if self.current_index == 0:
            print("ERROR, array is empty!")
            return None
        max_index = self.search_max()
        max_element = self.arr[max_index]
        self.assignment_number += 1
        self.arr[max_index] = self.arr[self.current_index - 1]
        self.current_index -= 1
        return max_element

class PriQueueUnsortedArrayImproved(PriQueue):

    max_index = 0

    def search_max(self):
        if self.current_index == 0:
            print("Array is empty!")
            return -1
        max_index = 0
        max_element = self.arr[0]
        for i in range(1, self.current_index):
            self.comp_number += 1
            if self.arr[i] > max_element:
                max_index = i
                max_element = self.arr[i]
        return max_index

    def insert(self, element):
        if self.current_index == self.size:
            print("ERROR, size '%d' is exceeded!" % self.size)
            return None
        self.arr[self.current_index] = element
        if self.max_index < 0 or self.arr[self.max_index] < element:
            self.max_index = self.current_index
        print("Current index: %d" % self.current_index)
        self.current_index += 1
        self.assignment_number += 1

    def max(self):
        if self.current_index == 0:
            print("ERROR, array is empty!")
            return None
        self.assignment_number += 1
        return self.arr[self.max_index]

    def del_max(self):
        if self.current_index == 0:
            print("ERROR, array is empty!")
            return None
        max_element = self.arr[self.max_index]
        self.assignment_number += 1
        self.arr[self.max_index] = self.arr[self.current_index - 1]
        self.assignment_number += 1
        self.current_index -= 1
        self.max_index = self.search_max()
        return max_element


class PriQueueSortedArray(PriQueue):

    max_index = 0

    def search_max(self):
        if self.current_index == 0:
            print("Array is empty!")
            return -1
        max_index = 0
        max_element = self.arr[0]
        for i in range(1, self.current_index):
            self.comp_number += 1
            if self.arr[i] > max_element:
                max_index = i
                max_element = self.arr[i]
        return max_index

    def insert(self, element):
        if self.current_index == self.size:
            print("ERROR, size '%d' is exceeded!" % self.size)
            return None
        self.arr[self.current_index] = element
        if self.max_index < 0 or self.arr[self.max_index] < element:
            self.max_index = self.current_index
        print("Current index: %d" % self.current_index)
        self.current_index += 1
        self.assignment_number += 1

    def max(self):
        if self.current_index == 0:
            print("ERROR, array is empty!")
            return None
        self.assignment_number += 1
        return self.arr[self.max_index]

    def del_max(self):
        if self.current_index == 0:
            print("ERROR, array is empty!")
            return None
        max_element = self.arr[self.max_index]
        self.assignment_number += 1
        self.arr[self.max_index] = self.arr[self.current_index - 1]
        self.assignment_number += 1
        self.current_index -= 1
        self.max_index = self.search_max()
        return max_element


