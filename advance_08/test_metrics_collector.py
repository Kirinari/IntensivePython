import unittest
from metrics_collector import *
import time

class TestStat(unittest.TestCase):
    def setUp(self) -> None:
        Stats.names = {}

    def test_timer_context_and_add(self):
        
        def f1():
            time.sleep(0.1)

        with Stats.timer("f1"):
            f1()
        t1 = time.time()
        f1()
        t2 = time.time()
        Stats.timer("f1").add(t2 - t1)

        self.assertListEqual(["f1.timer"], list(Stats.names.keys()))
        self.assertAlmostEqual( Stats.timer("f1").get_value(), 0.2, 1)
    
    def test_count_add(self):
        
        def f1():
            return 5

        def f2():
            return 6

        f1()
        Stats.count('f1').add()
        for i in range(5):
            f2()
            Stats.count('f2').add()
        for i in range(3):
            f1()
            Stats.count('f1').add()

        self.assertListEqual(["f1.count", "f2.count"], list(Stats.names.keys()))
        self.assertEqual(Stats.count("f1").get_value(), 4)
        self.assertEqual(Stats.count("f2").get_value(), 5)

    def test_avg_add(self):
        def f1(n):
            return n

        for i in range(1, 5):
            res = f1(i)
            Stats.avg('f1').add(res)

        self.assertListEqual(["f1.avg"], list(Stats.names.keys()))
        self.assertAlmostEqual(Stats.avg("f1").get_value(), 2.5, 2)
    
    def test_clear(self):
        def f1(n):
            return n
        res = f1(2)
        Stats.avg("f1").add(res)
        Stats.count("f1").add()
        Stats.timer("f1").add(1)

        Stats.avg("f1").clear()
        Stats.count("f1").clear()
        Stats.timer("f1").clear()
        self.assertDictEqual({"f1.timer" : 0, "f1.count" : 0, "f1.avg" : 0},  Stats.collect())
    
    def test_collect(self):
        Stats.count("f1").add()
        Stats.count("f2").add()
        Stats.count("f1").add()

        Stats.avg("f3").add(1)
        Stats.avg("f3").add(5)

        Stats.timer("f4").add(1)

        self.assertDictEqual({"f1.count" : 2, "f2.count" : 1, "f3.avg" : 3, "f4.timer" : 1},  Stats.collect())
        self.assertDictEqual({},  Stats.collect())
    
    def test_get_value_empty(self):
        self.assertEqual(Stats.avg("f1").get_value(), None)
    
    def test_get_name(self):
        Stats.count("f1").add()
        self.assertEqual( Stats.count("f1").get_name(), "f1.count")
    



