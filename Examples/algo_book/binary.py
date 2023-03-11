import random
import timeit
import numpy as np
from scipy.optimize import curve_fit


def log_model(n, a):
    # print(type(n))
    # print(n)
    return a * (np.log2(n))


def binary_array_search(A, target):
    lo = 0
    hi = len(A) - 1

    while lo <= hi:
        mid = (lo + hi) // 2

        if target < A[mid]:
            hi = mid - 1
        elif target > A[mid]:
            lo = mid + 1
        else:
            return mid

    return -(lo + 1)


n = 2 ** 5

xs = []
ys = []

filename = 'binary_output.txt'

with open(filename, "w+") as file_object:

    while n < 2 ** 12:
        xs.append(n)
        search_list = sorted(random.sample(list(range(0, 4 * n)), n))
        num_to_search = random.randint(0, 4 * n)

        # print(f"Searching for {num_to_search} in list {search_list}...")

        my_time = timeit.timeit(lambda: binary_array_search(search_list, num_to_search), number=1)

        search_result = binary_array_search(search_list, num_to_search)

        # print(f"Binary search for number {num_to_search} in {n} values result: {search_result}")
        # print(f"My time for it: {my_time}")
        file_object.write(f"{n}: --- {search_result} --- {my_time}\n")
        ys.append(my_time)
        n = n + 1

[a, _] = curve_fit(log_model, np.array(xs), np.array(ys))
print('Log = {}*log(N)'.format(a))



