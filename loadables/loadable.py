# Author: Raymond Malicdem


import collections


def most_number_element(iter_elem):
    counters = None
    if iter_elem is not None:
        try:
            if not hasattr(iter_elem, "__iter__"):
                raise AttributeError()
            counters = collections.Counter(iter_elem)
        except AttributeError:
            counters = None
        return max(counters, key=lambda x: counters[x])
