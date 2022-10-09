"""
hello pylint
"""
from customlist import CustomList
TEST_A = CustomList([5, 1, 3, 7])
TEST_B = CustomList([1, 2, 7])
assert TEST_A - TEST_B == CustomList([4, -1, -4, 7])
assert list(TEST_A - TEST_B) == [4, -1, -4, 7]
assert TEST_A + TEST_B == CustomList([6, 3, 10, 7])
assert list(TEST_A + TEST_B) == [6, 3, 10, 7]
assert TEST_A + CustomList() == TEST_A
assert list(TEST_A + CustomList()) == list(TEST_A)
assert [1, 2, 3] + CustomList([1, 1, 1]) == CustomList([9])
assert list([1, 2, 3] + CustomList([1, 1, 1])) == [2, 3, 4]
assert list(CustomList([1]) + [1, 2, 3]) == [2, 2, 3]
assert str(TEST_A) == '5 1 3 7 \nsum: 16'
