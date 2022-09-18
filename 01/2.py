def split_into(L):
    odd = []
    even = []
    for i in L:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return (even, odd)


assert split_into([1, 2, 3, 4]) == ([2, 4], [1, 3])
assert split_into([1, 1, 1, 1]) == ([], [1, 1, 1, 1])
assert split_into([2, 2, 2, 2]) == ([2, 2, 2, 2], [])
assert split_into([1]) == ([], [1])
assert split_into([13, 41, 20, 19, 40, 52]) == ([20, 40, 52], [13, 41, 19])
