"""
test module for LRUCache
"""

import unittest

from lru_cache import LRUCache


class TestLRUCache(unittest.TestCase):
    """
    unittest for LRU
    """
    def setUp(self) -> None:
        """
        setting up
        """
        self.cache_short = LRUCache(limit=2)
        self.cache_long = LRUCache(limit=32)
        self.res_short = []
        self.real_res = []

    def test_short1(self):
        """
        test1
        """
        self.res_short = []

        self.cache_short.set("k1", "val1")
        self.cache_short.set("k2", "val2")

        self.res_short.append(self.cache_short.get("k3"))
        self.res_short.append(self.cache_short.get("k2"))
        self.res_short.append(self.cache_short.get("k1"))

        self.assertEqual(self.res_short, [None, "val2", "val1"])

    def test_short2(self):
        """
        test2
        """
        self.res_short = []

        self.cache_short.set("k1", "val1")
        self.cache_short.set("k2", "val2")

        self.res_short.append(self.cache_short.get("k3"))
        self.res_short.append(self.cache_short.get("k2"))
        self.res_short.append(self.cache_short.get("k1"))

        self.cache_short.set("k3", "val3")

        self.res_short.append(self.cache_short.get("k3"))
        self.res_short.append(self.cache_short.get("k2"))
        self.res_short.append(self.cache_short.get("k1"))

        self.assertEqual(self.res_short, [None, 'val2', 'val1', 'val3', None, 'val1'])

    def test_long1(self):
        """
        test3
        """
        for i in range(self.cache_long.maxlen):
            self.cache_long.set("k" + str(i), "val" + str(i))

        self.real_res = []
        for i in range(self.cache_long.maxlen):
            self.real_res.append("k" + str(i))

        self.assertEqual(self.real_res, list(self.cache_long.var))


if __name__ == '__main__':
    unittest.main()
