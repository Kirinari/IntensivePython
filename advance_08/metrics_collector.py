from time import time, sleep
from contextlib import contextmanager
from random import randint
from typing import Any
class BaseMetric:
    def __init__(self, name: str):
        self.name = name
        self.metric_name = ''

    def get_name(self) -> str:
        return self.name + '.' + self.metric_name

    def get_value(self) -> int | float | None:
        name = self.get_name()
        if name in Stats.names:
           return  Stats.names[name]
        return None

    def add(self, value : int | float) -> None:
        name = self.get_name()
        if name not in Stats.names:
            Stats.names[name] = 0
        Stats.names[name] += value

    def clear(self) -> None:
        name = self.get_name()
        if name in Stats.names:
             Stats.names[name] = 0


class MetricTimer(BaseMetric):
    def __init__(self, name : str):
        super().__init__(name)
        self.metric_name = 'timer'

    def __enter__(self) -> None:
        self.time = time()

    def __exit__(self, *args) -> None:
        self.time = time() - self.time
        self.add(self.time)



class MetricAvg(BaseMetric):
    def __init__(self, name : str):
        super().__init__(name)
        self.metric_name = 'avg'

    def add(self, value : float | int) -> None:
        name = self.get_name()
        if name not in Stats.names:
            Stats.names[name] = [0, 0]
        Stats.names[name][0] += value
        Stats.names[name][1] += 1

    def get_value(self) -> int | float | None:
        name = self.get_name()
        if name in Stats.names:
            if Stats.names[name][1] == 0:
                return 0
            return  Stats.names[name][0] / Stats.names[name][1]
        return None
    
    def clear(self) -> None:
        name = self.get_name()
        if name in Stats.names:
            Stats.names[name] = [0, 0]

class MetricCount(BaseMetric):
    def __init__(self, name):
        super().__init__(name)
        self.metric_name = 'count'

    def add(self, value = 1) -> None:
        name = self.get_name()
        if name not in Stats.names:
            Stats.names[name] = 0
        Stats.names[name] += value


class Stats:
    names : dict[str, Any]
    names = {}
    
    @staticmethod
    def timer(name : str) -> MetricTimer:
        return MetricTimer(name)

    @staticmethod
    def avg(name : str) -> MetricAvg:
        return MetricAvg(name)

    @staticmethod
    def count(name : str) -> MetricCount:
        return MetricCount(name)

    @staticmethod
    def collect() -> dict[str, Any]:
        result_dict = {}
        for name in Stats.names:
            f_name, metric_name = name.split('.')
            if metric_name == 'avg':
                result_dict[name] = Stats.avg(f_name).get_value()
            elif metric_name == 'count':
                 result_dict[name] = Stats.count(f_name).get_value()
            elif metric_name == 'timer':
                 result_dict[name] = Stats.timer(f_name).get_value()
        Stats.names = {}
        return result_dict
            


if __name__ == '__main__':

    def calc():
        sleep(0.2)
        return 5

    with Stats.timer("calc"):  # 0.1
        res = calc()  # 3

    res = calc()

    Stats.count("calc").add()
    Stats.avg("calc").add(res)

    t1 = time()
    res = calc()  # 7
    t2 = time()
    Stats.timer("calc").add(t2 - t1)  # 0.3
    Stats.count("calc").add()
    Stats.avg("calc").add(res)

    Stats.count("http_get_data").add()
    Stats.avg("http_get_data").add(0.7)

    Stats.count("no_used")  # не попадет в результат collect

    metrics = Stats.collect()
    print(metrics)
    assert metrics == {
        "calc.count": 2,
        "calc.avg": 5.0,
        "calc.timer": 0.4,
        "http_get_data.count": 1,
        "http_get_data.avg": 0.7,
    }

    metrics = Stats.collect()
    assert metrics == {}