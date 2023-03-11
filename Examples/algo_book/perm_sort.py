import numpy as np
import math
from scipy.optimize import curve_fit
from itertools import permutations
from scipy.special import factorial
import timeit


def factorial_model(n, a):
    return a * factorial(n)


def check_sorted(a):
    for i, val in enumerate(a):
        if i > 0 and val < a[i - 1]:
            return False
    return True


def permutation_sort(A):
    for attempt in permutations(A):
        if check_sorted(attempt):
            A[:] = attempt[:]  # copy back into A
            return


elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

input_lists = []

for n in range(1, 13):
    # print(elements[0:n])
    input_lists.append(list(reversed(elements[0:n])))

# for lis in input_lists:
#     print(lis)

xs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
ys = []

for i in xs:
    my_time = timeit.timeit(lambda: permutation_sort(input_lists[i]), number=1)
    print(f"My time for {i + 1} long list: {my_time}")
    ys.append(my_time)

print(ys)

[a, _] = curve_fit(factorial_model, np.array(xs), np.array(ys))
print('Factorial = {} * N!'.format(a))
