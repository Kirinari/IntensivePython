from customlist import CustomList
a = CustomList([5, 1, 3, 7])
b = CustomList([1, 2, 7])
assert a - b == CustomList([4, -1, -4, 7])
assert list(a - b) == [4, -1, -4, 7]
assert a + b == CustomList([6, 3, 10, 7])
assert list(a + b) == [6, 3, 10, 7]
assert a + CustomList() == a
assert list(a + CustomList()) == list(a)
assert [1, 2, 3] + CustomList([1, 1, 1]) == CustomList([9])
assert list([1, 2, 3] + CustomList([1, 1, 1])) == [2, 3, 4]
assert list(CustomList([1]) + [1, 2, 3]) == [2, 2, 3]
assert str(a) == '5 1 3 7 \nsum: 16'
