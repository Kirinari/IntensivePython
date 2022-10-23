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

    def test_short1(self):
        """
        test1
        """
        cache_short = LRUCache(limit=2)

        res_short = []

        cache_short.set("k1", "val1")
        cache_short.set("k2", "val2")

        res_short.append(cache_short.get("k3"))
        res_short.append(cache_short.get("k2"))
        res_short.append(cache_short.get("k1"))

        self.assertEqual(res_short, [None, "val2", "val1"])

    def test_short2(self):
        """
        test2
        """
        cache_short = LRUCache(limit=2)
        res_short = []

        cache_short.set("k1", "val1")
        cache_short.set("k2", "val2")

        res_short.append(cache_short.get("k3"))
        res_short.append(cache_short.get("k2"))
        res_short.append(cache_short.get("k1"))

        cache_short.set("k3", "val3")

        res_short.append(cache_short.get("k3"))
        res_short.append(cache_short.get("k2"))
        res_short.append(cache_short.get("k1"))

        self.assertEqual(res_short, [None, 'val2', 'val1', 'val3', None, 'val1'])

    def test_long1(self):
        """
        test3
        """
        cache_long = LRUCache(limit=32)
        for i in range(cache_long.maxlen):
            cache_long.set("k" + str(i), "val" + str(i))

        real_res = []
        for i in range(cache_long.maxlen):
            real_res.append("k" + str(i))

        self.assertEqual(real_res, list(cache_long.var))

    def test_super_short(self):
        """
        testing length 1
        """
        cache_super_short = LRUCache(limit=1)
        res_super_short = []
        cache_super_short.set("k1", "val1")
        cache_super_short.set("k2", "val2")
        res_super_short.append(cache_super_short.get("k1"))
        res_super_short.append(cache_super_short.get("k2"))

        self.assertEqual(res_super_short, [None, 'val2'])

    def test_set_changer(self):
        """
        testing set
        """
        cache = LRUCache(2)
        res_changer = []
        cache.set("k1", "val1")
        cache.set("k2", "val2")
        cache.set("k1", "val1")
        cache.set("k2", "val2")

        res_changer.append(cache.get("k3"))
        res_changer.append(cache.get("k2"))
        res_changer.append(cache.get("k1"))

        cache.set("k3", "val1")
        cache.set("k3", "val5")
        cache.set("k3", "val3")
        cache.set("k3", "val5")

        res_changer.append(cache.get("k3"))
        res_changer.append(cache.get("k2"))
        res_changer.append(cache.get("k1"))

        self.assertEqual(res_changer, [None, 'val2', 'val1', 'val5', None, 'val1'])


if __name__ == '__main__':
    unittest.main()
