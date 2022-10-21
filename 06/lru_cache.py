"""hello pylint"""
from collections import deque


class LRUCache:
    """hello pylint"""

    def __init__(self, limit=42):
        self.var = deque()
        self.values = deque()
        self.maxlen = limit

    def get(self, key):
        """hello pylint"""
        i = 0
        cur_len = len(self.var)
        while i < cur_len and self.var[i] != key:
            i += 1
        if i == cur_len:
            return None

        j = i
        while j < cur_len - 1:
            tmp1 = self.var[j]
            self.var[j] = self.var[j + 1]
            self.var[j + 1] = tmp1
            tmp2 = self.values[j]
            self.values[j] = self.values[j + 1]
            self.values[j + 1] = tmp2
            j += 1

        return self.values[-1]

    def set(self, key, value):
        """hello pylint"""
        if len(self.var) == self.maxlen:
            self.var[0] = key
            self.values[0] = value
            self.var.rotate()
            self.values.rotate()
        else:
            self.var.append(key)
            self.values.append(value)
