#!/usr/bin/env python3

"""A basic cache system"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Defines a Basic cache that inherits from
    BaseCaching"""

    def put(self, key, item):
        """
            args:
                key(str): dic key
                item(str): dic item
        """

        if key is None or item is None:
            return
        else:
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
