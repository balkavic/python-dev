def binary_search(arr, start, end, element, profiling=False):
    l = start
    r = end
    comp_number = 0
    while l < r:
        m = (l + r) // 2
        comp_number += 1
        if arr[m] < element:
            l = m + 1
        elif arr[m] > element:
            r = m
        else:
            return m
    return l