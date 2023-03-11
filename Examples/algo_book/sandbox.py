import time
import timeit
import random


def tournament_two(A):
    N = len(A)
    winner = [None] * (N - 1)
    loser = [None] * (N - 1)
    prior = [-1] * (N - 1)

    idx = 0

    for i in range(0, N, 2):
        if A[i] < A[i + 1]:
            winner[idx] = A[i + 1]
            loser[idx] = A[i]
        else:
            winner[idx] = A[i]
            loser[idx] = A[i + 1]
        idx += 1

    m = 0
    while idx < N - 1:
        if winner[m] < winner[m + 1]:
            winner[idx] = winner[m + 1]
            loser[idx] = winner[m]
            prior[idx] = m + 1
        else:
            winner[idx] = winner[m]
            loser[idx] = winner[m + 1]
            prior[idx] = m
        m += 2
        idx += 1

    largest = winner[m]
    second = loser[m]
    m = prior[m]

    while m >= 0:
        if second < loser[m]:
            second = loser[m]
        m = prior[m]

    return (largest, second)


def is_palindrom_rev(A):
    temp_list = list(A)
    temp_list.reverse()
    return str(A) ==  ''.join(temp_list)


def is_palindrom_loop(A):
    for i in range(0, len(A) // 2):
        if A[i] != A[(i + 1) * (-1)]:
            return False
        # print(A[(i + 1) * (-1)])

    return True


def is_palindrom_slice(A):
    half = len(A) // 2
    # print(half)
    first_part = A[0:half]
    second_part = A[half if len(A) % 2 == 0 else half + 1:]
    # print(first_part)
    # print(second_part[::-1])
    return first_part == second_part[::-1]
    # for i in range(0, len(A) // 2):
    #     if A[i] != A[(i + 1) * (-1)]:
    #         return False
    #     # print(A[(i + 1) * (-1)])
    #
    # return True


def is_palindrome1(w):
    """Create slice with negative step and confirm equality with w."""
    return w[::-1] == w


def is_palindrome2(w):
    """Strip outermost characters if same, return false when mismatch."""
    while len(w) > 1:
        if w[0] != w[-1]:     # if mismatch, return False
            return False
        w = w[1:-1]           # strip characters on either end; repeat

    return True             # must have been palindrome


def partition(A, lo, hi, idx):
    """Partition using A[idx] as value."""
    if lo == hi: return lo

    A[idx], A[lo] = A[lo], A[idx]  # swap into position
    i = lo
    j = hi + 1
    while True:
        while True:
            i += 1
            if i == hi: break
            if A[lo] < A[i]: break

        while True:
            j -= 1
            if j == lo: break
            if A[j] < A[lo]: break

        if i >= j: break
        A[i], A[j] = A[j], A[i]

    A[lo], A[j] = A[j], A[lo]
    return j


def linear_median(A):
    """
    Efficient implementation that returns median value in arbitrary list,
    assuming A has an odd number of values. Note this algorithm will
    rearrange values in A.
    """
    lo = 0
    hi = len(A) - 1
    mid = hi // 2
    while lo < hi:
        idx = random.randint(lo, hi)  # select valid index randomly
        j = partition(A, lo, hi, idx)

        if j == mid:
            return A[j]
        if j < mid:
            lo = j + 1
        else:
            hi = j - 1
    return A[lo]


def my_median(A):
    temp_list = []
    # print(temp_list)
    # print(len(temp_list))

    for item in A:
        i = 0
        while i < len(temp_list) and item > temp_list[i]:
            i += 1
        temp_list.insert(i, item)
    # print(temp_list)
    return temp_list[len(temp_list) // 2]


def counting_sort(A, M):
    counts = [0] * M
    for v in A:
        counts[v] += 1

    pos = 0
    v = 0
    while pos < len(A):
        for idx in range(counts[v]):
            A[pos + idx] = v
        pos += counts[v]
        v += 1


def my_counting_sort(A, M):
    counts = [0] * M
    for v in A:
        counts[v] += 1

    pos = 0
    v = 0
    while pos < len(A):
        A[pos:pos+counts[v]-1] = [v] * counts[v]
        pos += counts[v]
        v += 1


# filename = 'input.txt'


filename = 'short_input.txt'

with open(filename) as file_object:
    contents = file_object.read()
    input_list = list(map(int, contents.split(' ')))

# print(contents)
print(input_list * 2)
# print(sorted(input_list))

# my_time = timeit.timeit(lambda: my_median(input_list), number=10000)
# print(f"My time: {my_time}")
#
# book_time = timeit.timeit(lambda: linear_median(input_list), number=10000)
# print(f"Book time: {book_time}")

for i in range(10):
    new_input_list = input_list * (i**2)
    exec_time = timeit.timeit(lambda: counting_sort(new_input_list, 13), number=10000)
    print(f"Book {2**i}: {exec_time}")
    my_exec_time = timeit.timeit(lambda: my_counting_sort(new_input_list, 13), number=10000)
    print(f"Mine {2 ** i}: {my_exec_time}")


# print(input_list)


# print(median)


#
# (largest, second) = tournament_two(input_list)
#
# print(f"Largest: {largest}")
# print(f"Second: {second}")


# filename = 'input_text.txt'
#
# with open(filename) as file_object:
#     input_text = file_object.read()

# print(input_text)
# temp_list = list(input_text)
# temp_list.reverse()
# print(''.join(temp_list))
# print()
# print(f"Word length: {len(input_text)}")
#
# my_time = timeit.timeit(lambda: is_palindrom_slice(input_text), number=1000)
# print(f"Mine: {my_time}")
#
# book1_time = timeit.timeit(lambda: is_palindrome1(input_text), number=1000)
# print(f"Book1: {book1_time}")
#
# book2_time = timeit.timeit(lambda: is_palindrome2(input_text), number=1)
# print(f"Book2: {book2_time}")

