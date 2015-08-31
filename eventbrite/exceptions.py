# -*- coding: utf-8 -*-

from google.appengine.api import urlfetch

class EventbriteException(Exception):
    pass


class IllegalHttpMethod(EventbriteException):
    pass


class InvalidResourcePath(EventbriteException):
    pass


class UnknownEndpoint(EventbriteException):
    pass


class UnsupportedEndpoint(EventbriteException):
    pass


# class InternetConnectionError(ConnectionError):
class InternetConnectionError(urlfetch.DownloadError):
    """
    Wraps urlfetch.DownloadError in order to provide a more
    intuitively named exception.
    """
    pass


class InvalidWebhook(EventbriteException):
    pass
