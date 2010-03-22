from django.core.exceptions import ImproperlyConfigured
from django.db import models


def is_app_installed(app_name):
    """
    Gets the app_name and returns True if it is installed, False otherwise.
    """
    try:
        app = models.get_app(app_name)
    except ImproperlyConfigured:
        return False
    return True


def if_app(func, app_name):
    """
    Decorator that gets the app_name and executes the wrapped methods only
    if the app is installed.
    """
    def wrapped(*args, **kwargs):
        if is_app_installed(app_name):
            return func(*args, **kwargs)
    return wrapped()

