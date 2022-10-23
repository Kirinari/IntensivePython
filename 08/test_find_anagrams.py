from unittest import TestCase
from find_anagrams import find_anagrams


class TestFindAnagrams(TestCase):
    def test_find1(self):
        self.assertEqual(find_anagrams("abcba", "abc"), [0, 2])

    def test_find2(self):
        self.assertEqual(find_anagrams("aaa", "a"), [0, 1, 2])

    def test_find3(self):
        self.assertEqual(find_anagrams("abc cba xabcd", 'abc'), [0, 4, 9])

    def test_findrus4(self):
        self.assertEqual(find_anagrams("ффф", 'ф'), [0, 1, 2])

    def test_find5(self):
        self.assertEqual(find_anagrams("trccccytvbabc", "cc"), [2, 3, 4])

    def test_find6(self):
        self.assertEqual(find_anagrams("aaababaa", "aaba"), [0, 1, 4])

    def test_findrus7(self):
        self.assertEqual(find_anagrams("ракета", "карета"), [0])

    def test_findrus_empty(self):
        self.assertEqual(find_anagrams("тут нет анаграмм", "эх"), [])
