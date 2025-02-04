"""
Details returned by the IPinfo service.
"""

from __future__ import unicode_literals

class Details:
    """Encapsulates data for single IP address."""

    def __init__(self, details):
        """Initialize by settings `details` attribute."""
        self.details = details

    def __getattr__(self, attr):
        """Return attribute if it exists in details array, else return error."""
        if attr not in self.details:
            raise AttributeError("%s is not a valid attribute of Details" % attr)

        return self.details[attr]

    @property
    def all(self):
        """Return all details as dict."""
        return self.details
