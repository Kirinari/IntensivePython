import unittest

class TestInt(unittest.TestCase):
    def test_empty_call(self):
        var = int()
        self.assertEqual(0, var)

    def test_string(self):
        var = int("123")
        self.assertEqual(123, var)
    
    def test_zeros(self):
        var = int("00000123")
        self.assertEqual(123, var)
    
    def test_trunc_float(self):
        var = int(-3.4)
        self.assertEqual(-3, var)
    
    def test_custom_magic_int(self):
        class A:
            def __init__(self, n):
                self.n = n
            def __int__(self):
                return self.n + 1
        
        var1 = A(5)
        var1.n = int(var1)
        self.assertEqual(var1.n, 6)
    
    def test_custom_magic_index(self):
        class A:
            def __init__(self, n):
                self.n = n
            def __index__(self):
                return self.n + 1
        var1 = A(5)
        var1.n = int(var1)
        self.assertEqual(var1.n, 6)
    
    def test_custom_magic_trunc(self):
        class A:
            def __init__(self, n):
                self.n = n
            def __trunc__(self):
                return self.n + 1
        var1 = A(5)
        var1.n = int(var1)
        self.assertEqual(var1.n, 6)
    
    def test_base_2(self):
        var = int("10", base=2)
        self.assertEqual(2, var)
    
    def test_base_16(self):
        var = int("1A", base=16)
        self.assertEqual(26, var)
    
    def test_byte(self):
        var = int(b"0b_1110_0101", base=2)
        self.assertEqual(229, var)

    def test_negative_string(self):
        var = int("-123")
        self.assertEqual(-123, var)


        
            


