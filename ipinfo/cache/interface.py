"""
Abstract interface for caching IPinfo data.
"""

import abc


class CacheInterface:
    """Interface for using custom cache."""

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def __contains__(self, key):
        pass

    @abc.abstractmethod
    def __setitem__(self, key, value):
        pass

    @abc.abstractmethod
    def __getitem__(self, key):
        pass

    @abc.abstractmethod
    def __delitem__(self, key):
        pass
