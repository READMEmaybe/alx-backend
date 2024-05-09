#!/usr/bin/env python3
""" LFU Caching """

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """ LFU caching system """

    def __init__(self):
        """ Initiliaze
        """
        super().__init__()
        self.freq = {}

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key and item:
            if (len(self.cache_data) >= BaseCaching.MAX_ITEMS) and \
                   (key not in self.cache_data):
                least_freq = min(self.freq.values())
                keys = [k for k, v in self.freq.items() if v == least_freq]
                discard = min(keys, key=self.freq.get)
                self.cache_data.pop(discard)
                self.freq.pop(discard)
                print("DISCARD: {}".format(discard))

            if key in self.cache_data:
                self.freq[key] += 1
            else:
                self.freq[key] = 1
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key in self.cache_data:
            self.freq[key] += 1
            return self.cache_data[key]
        return None
