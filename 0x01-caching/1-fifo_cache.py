#!/usr/bin/env python3

"""FIFO system"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Defines a fifo algorithm"""

    def __init__(self):
        """Initialize the class"""
        super().__init__()

    def put(self, key, item):
        """Putting item in the dictionary"""

        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            """sort the keys"""
            keys = [key for key in sorted(self.cache_data.keys())]
            '''discard the first key'''

            print(f"DISCARD: {keys[0]}")
            deleted_key = keys[0]
            del self.cache_data[deleted_key]

        self.cache_data[key] = item

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
