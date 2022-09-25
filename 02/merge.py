def merge(arr1, arr2):
    res = []
    i = 0
    j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            i += 1
        elif arr1[i] > arr2[j]:
            j += 1
        else:
            if len(res) == 0 or res[-1] != arr1[i]:
                res.append(arr1[i])
            i += 1
            j += 1
    return res

assert merge([1, 1, 2, 5, 7], (1, 1, 2, 3, 4, 7)) == [1, 2, 7]
assert merge([1, 2, 3], [4, 5, 6]) == []
assert merge((1, 3, 5), (2, 4, 6)) == []
assert merge([1, 2, 3, 4, 5], (3, 5, 6)) == [3, 5]
            
