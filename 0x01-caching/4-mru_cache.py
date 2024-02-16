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
        self.key_order = []

    def put(self, key, item):
        """MRU algorithm setup"""
        with self._Rlock:
            if key is not None and item is not None:
                if key in self.cache_data:
                    # Update the order as this key
                    # is now the most recently used
                    self.key_order.remove(key)
                    self.key_order.append(key)
                else:
                    if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                        # Evict the most recently used item,
                        # which is the last item in key_order
                        discarded = self.key_order.pop()
                        self.cache_data.pop(discarded)
                        print(f"DISCARD: {discarded}")
                    self.cache_data[key] = item
                    self.key_order.append(key)

    def get(self, key):
        """Access the cached data"""
        with self._Rlock:
            if key is None or key not in self.cache_data:
                return None
            else:
                # Update the order as this key is now the most recently used
                self.key_order.remove(key)
                self.key_order.append(key)
                return self.cache_data[key]
