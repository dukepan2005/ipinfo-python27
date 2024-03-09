from __future__ import unicode_literals

from .handler import Handler


def getHandler(access_token=None, **kwargs):
    """Create and return Handler object."""
    return Handler(access_token, **kwargs)


def getHandlerAsync(access_token=None, **kwargs):
    """Create an return an asynchronous Handler object."""
    return AsyncHandler(access_token, **kwargs)
