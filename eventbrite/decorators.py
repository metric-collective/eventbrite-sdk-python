import functools

# import requests

from .exceptions import InternetConnectionError
from .models import EventbriteObject


def objectify(func):
    """ Converts the returned value from a models.Payload to
        a models.EventbriteObject. Used by the access methods
        of the client.Eventbrite object
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            payload = func(*args, **kwargs)
        except urlfetch.DownloadError as e:
            raise InternetConnectionError()
        return EventbriteObject.create(payload)
    return wrapper
