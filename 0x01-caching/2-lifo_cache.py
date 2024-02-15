#!/usr/bin/env python3

"""LIFO system"""
from base_caching import BaseCaching
from threading import RLock


class LIFOCache(BaseCaching):
    """Defines a LIFO algorithm"""

    def __init__(self):
        """Initialize the class"""
        super().__init__()
        self._stack_keys = []
        self._Rlock = RLock()

    def put(self, key, item):
        """Putting item in the dictionary"""
        with self._Rlock:
            if key is None or item is None:
                return
            if key in self.cache_data:
                self.cache_data[key] = item

                if key in self._stack_keys:
                    ''''move key to the top of the stack'''
                    self._stack_keys.remove(key)
                    self._stack_keys.append(key)

            else:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:

                    """discard the top key"""
                    discarded_key = self._stack_keys.pop()
                    del self.cache_data[discarded_key]
                    print(f"DISCARD: {discarded_key}")

                self.cache_data[key] = item
                self._stack_keys.append(key)

    def get(self, key):
        """
            args:

            key(str): dictionary key
            item(str): dictionary item
        """
        with self._Rlock:
            data = self.cache_data.get(key)

            if key is None or data is None:
                return None
            else:
                return data
