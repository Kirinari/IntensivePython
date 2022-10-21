import csv
import json
from abc import ABC
from abc import abstractmethod


class BaseReader(ABC):
    @abstractmethod
    def read(self, f):
        pass


class BaseWriter(ABC):
    @abstractmethod
    def write(self, data, f):
        pass


class TxtReader(BaseReader):
    def read(self, f):
        return f.readlines()


class TxtWriter(BaseWriter):
    def write(self, data, f):
        try:
            if not isinstance(data, list):
                f.write(data)
            else:
                for s in data:
                    f.write(s)
        except TypeError:
            print('Data is not str')


class CsvReader(BaseReader):
    def read(self, f):
        f.seek(0)
        rdr = list(csv.reader(f))
        return rdr


class CsvWriter(BaseWriter):

    def write(self, data, f):
        def get_depth(list_):
            if isinstance(list_, (list, tuple)):
                return 1 + max(get_depth(itm) for itm in list_)
            return 0

        wrt = csv.writer(f)
        if isinstance(data, (list, tuple)):
            if get_depth(data) > 1:
                wrt.writerows(data)
            else:
                wrt.writerow(data)
            return
        print('Data is not list or tuple')


class JsonReader(BaseReader):
    def read(self, f):
        return json.load(f)


class JsonWriter(BaseWriter):
    def write(self, data, f):
        if isinstance(data, dict):
            json.dump(data, f)
            return
        print('Data is not dict')


def read_data(f, reader: BaseReader):
    return reader.read(f)


def dump_data(data, f, writer: BaseWriter):
    writer.write(data, f)


if __name__ == "__main__":
    f = open('testfile.json', 'w')
    dump_data({"x": "1"}, f, writer=JsonWriter())
    f.close()
    f = open('testfile.json', 'r')
    data = read_data(f, reader=JsonReader())
    f.close()
    assert data == {"x": "1"}
