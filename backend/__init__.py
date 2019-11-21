import platform
from functools import wraps


def disable_for_raspberry(f):
    """Decorator function. disable the function for raspberry pi."""

    @wraps(f)
    def wrap(*args, **kwargs):
        if all(keyword in platform.platform() for keyword in ["debian", "arm"]):
            return dict(message="function disable for raspberry pi nodes")
        return f(*args, **kwargs)

    return wrap
