from unittest import TestCase
from io import StringIO
from file_generator import f_generator


class TestReadFileGen(TestCase):
    def test_read(self):
        f = StringIO()
        f.write("a ab\nab ab\nac ad\nae")
        f.seek(0)
        words = ["a", "ae"]

        ans = ["a ab\n", "ae"]
        res = list(f_generator(f, words))

        self.assertEqual(ans, res)
