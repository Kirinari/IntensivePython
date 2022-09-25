import math

def nearest_numbers(arr):
    min_dist = abs(arr[0])
    res = []
    for i in arr:
        if abs(i) < min_dist:
            min_dist = abs(i)
    for i in arr:
        if math.isclose(min_dist, abs(i), rel_tol=1e-20):
            res.append(i)
    return res

assert nearest_numbers([-5, 9, 6, -8]) == [-5]
assert nearest_numbers([-1, 2, -5, 1, -1]) == [-1, 1, -1]
assert nearest_numbers([-1.51, -2.38, 1.51, -2.47, 5.19]) == [-1.51, 1.51]
assert nearest_numbers([0, 0, 0, -1, 0, 1]) == [0, 0, 0, 0]
