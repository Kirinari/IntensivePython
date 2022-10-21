from unittest import TestCase
from unittest import mock
from io import StringIO
from reader_writer import *


class TestRead(TestCase):
    def test_read_txt(self):
        reader = TxtReader()
        f = StringIO()

        f.write('Hello\nworld\n!')
        f.seek(0)
        res = read_data(f, reader)
        template = ['Hello\n', 'world\n', '!']

        self.assertEqual(res, template)
    
    def test_write_txt(self):
        writer = TxtWriter()
        f = StringIO()

        dump_data('Hello\n', f, writer)
        f.seek(0)
        ans = ['Hello\n']
        res = f.readlines()
        self.assertEqual(res, ans)

        dump_data(['world\n', '!\n'], f, writer)
        f.seek(0)
        res = f.readlines()
        ans = ['Hello\n', 'world\n', '!\n']
        self.assertEqual(res, ans)
    
    @mock.patch('reader_writer.print')
    def test_write_txt_err(self, myprint):
        writer = TxtWriter()
        f = StringIO()

        dump_data({'a': 1}, f, writer)
        f.seek(0)

        self.assertEqual(
            [mock.call('Data is not str')], myprint.mock_calls)


    def test_read_json(self):
        reader = JsonReader()
        f = StringIO()
        words = {'a': '1', 'b': '2'}

        json.dump(words, f)
        f.seek(0)
        res = read_data(f, reader)

        self.assertEqual(res, words)
    
    def test_write_to_json(self):
        writer = JsonWriter()
        f = StringIO()
        ans = {1: 2}

        dump_data(ans, f, writer)
        f.seek(0)
        res = json.load(f)
        ans_after = {'1': 2}

        self.assertEqual(ans_after, res)

    @mock.patch('reader_writer.print')
    def test_write_to_json_err(self, myprint):
        writer = JsonWriter()
        f = StringIO()

        dump_data("Hello World!", f, writer)

        self.assertEqual(
            [mock.call("Data is not dict")], myprint.mock_calls)

    def test_read_csv(self):
        reader = CsvReader()
        f = StringIO()
        ans = [['a', 1], ['b', 2], ['c', 3]]
        writer = csv.writer(f)
        writer.writerows(ans)

        res = read_data(f, reader)
        
        for ind, pair in enumerate(ans):
            pair[1] = str(pair[1])
            
        self.assertEqual(res, ans)

    def test_write_to_csv(self):
        writer = CsvWriter()
        f = StringIO()

        dump_data((('a', 1), ('b', 2)), f, writer)
        f.seek(0)
        reader = csv.reader(f)
        ans = [['a', '1'], ['b', '2']]
        res = list(reader)
        self.assertEqual(res, ans)

    @mock.patch('reader_writer.print')
    def test_write_to_csv_err(self, myprint):
        writer = CsvWriter()
        f = StringIO()

        dump_data("Hello world!", f, writer)

        self.assertEqual(
            [mock.call('Data is not list or tuple')], myprint.mock_calls)
