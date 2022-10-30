"""hello pylint"""
from collections import deque
import logging
import sys


class LRUCache:
    """hello pylint"""

    def __init__(self, limit=42):
        self.var = deque()
        self.values = deque()
        self.maxlen = limit
        logger.info("New LRU created with limit: %s", limit)

    def get(self, key):
        """hello pylint"""
        logger.info("Trying get %s", key)
        i = 0
        cur_len = len(self.var)
        while i < cur_len and self.var[i] != key:
            i += 1
        if i == cur_len:
            logger.error("No record for %s", key)
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
        logger.info("Got {%s, %s}", key, self.values[-1])

        return self.values[-1]

    def set(self, key, value):
        """hello pylint"""
        logger.info("Trying set {%s, %s}", key, value)

        if key not in self.var:
            if len(self.var) == self.maxlen:
                logger.warning("Dropped out {%s, %s}",
                               self.var[0], self.values[0])
                self.var[0] = key
                self.values[0] = value
                self.var.rotate()
                self.values.rotate()
            else:
                self.var.append(key)
                self.values.append(value)
                i = 0
            logger.info("Added new {%s, %s}", key, value)
            return

        cur_len = len(self.var)
        i = 0
        while i < cur_len and self.var[i] != key:
            i += 1
        logger.info("Replaced {%s, %s} -> {%s, %s}",
                    key, self.values[i], key, value)
        self.values[i] = value
        j = i
        while j < cur_len - 1:
            tmp1 = self.var[j]
            self.var[j] = self.var[j + 1]
            self.var[j + 1] = tmp1
            tmp2 = self.values[j]
            self.values[j] = self.values[j + 1]
            self.values[j + 1] = tmp2
            j += 1


if __name__ == "lru_cache_logs":
    logger = logging.getLogger("LRU")
    logger.setLevel(logging.INFO)
    fhandler = logging.FileHandler("cache.log")

    formatter = logging.Formatter(
        "%(asctime)s\t%(levelname)s\t%(name)s\t%(message)s")

    fhandler.setFormatter(formatter)
    fhandler.setLevel(logging.INFO)

    logger.addHandler(fhandler)

    for param in sys.argv:
        if param == "-s":
            shandler = logging.StreamHandler()
            shandler.setFormatter(formatter)
            shandler.setLevel(logging.INFO)
            logger.addHandler(shandler)
