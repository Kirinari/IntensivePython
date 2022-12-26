import unittest

class TestStrPart(unittest.TestCase):
    def test_simple(self):
        s = "first second"
        res = s.partition(' ')
        expected = ('first', ' ', 'second')
        self.assertTupleEqual(expected, res)
    
    def test_multiple_sep_in_string(self):
        s = "1 2 3"
        res = s.partition(' ')
        expected = ('1', ' ', '2 3')
        self.assertTupleEqual(expected, res)
    
    def test_not_found(self):
        s = '123'
        res = s.partition(' ')
        expected = ('123', '', '')
        self.assertTupleEqual(expected, res)
    
    def test_empty(self):
        f = lambda x: str.partition()
        self.assertRaises(TypeError, f)
    
    def test_long_sep(self):
        s = '1, 2, 3'
        res = s.partition(', ')
        expected = ('1', ', ', '2, 3')
        self.assertTupleEqual(expected, res)
    
    def test_empty_left(self):
        s = ' 123'
        res = s.partition(' ')
        expected = ('', ' ', '123')
        self.assertTupleEqual(expected, res)

    def test_empty_right(self):
        s = '123 '
        res = s.partition(' ')
        expected = ('123', ' ', '')
        self.assertTupleEqual(expected, res)
    
    def test_string_is_sep(self):
        s = '123'
        res = s.partition('123')
        expected = ('', '123', '')
        self.assertTupleEqual(expected, res)
    
