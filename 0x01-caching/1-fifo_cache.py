#!/usr/bin/env python3

"""FIFO system"""
from base_caching import BaseCaching
from threading import RLock


class FIFOCache(BaseCaching):
    """Defines a fifo algorithm"""

    def __init__(self):
        """Initialize the class"""
        super().__init__()
        self._keys = []
        self._Rlock = RLock()

    def put(self, key, item):
        """Putting item in the dictionary"""

        with self._Rlock:
            if key is None or item is None:
                return

            if key in self.cache_data:
                self.cache_data[key] = item

            else:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    deleted_key = self._keys.pop(0)
                    self.cache_data.pop(deleted_key)
                    print(f"DISCARD: {deleted_key}")

                self.cache_data[key] = item
                self._keys.append(key)

    def get(self, key):
        """
            args:

            key(str): dictionary key
            item(str): dictionary item
        """

        data = self.cache_data.get(key)

        if key is None or data is None:
            return None
        else:
            return data
