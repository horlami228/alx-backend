#!/usr/bin/env python3

"""MRU cache"""
from base_caching import BaseCaching
from threading import RLock
from collections import OrderedDict


class MRUCache(BaseCaching):

    """defines a Most Recently Used Algorithm"""

    def __init__(self):
        """initialize a new MRU system"""
        super().__init__()
        self._Rlock = RLock()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """MRU algorithm setup"""
        with self._Rlock:
            if key is None or item is None:
                return

            if key in self.cache_data:
                self.cache_data[key] = item
                self.cache_data.move_to_end(key)

            else:
                if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                    poped_item = self.cache_data.popitem(last=True)
                    print(f"DISCARD: {poped_item[0]}")

                self.cache_data[key] = item
                self.cache_data.move_to_end(key)

    def get(self, key):
        """Access the cached data"""
        with self._Rlock:
            data = self.cache_data.get(key, None)

            if data:
                self.cache_data.move_to_end(key)
                return data
            else:
                return None
