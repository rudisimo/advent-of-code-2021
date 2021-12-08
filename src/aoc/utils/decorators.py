from collections import deque
from functools import wraps
from typing import Callable


def queue_decorator(func: Callable, maxlen: int = 2):
    """Decorator for injecting a queue into our reduce function."""
    queue = deque([], maxlen=maxlen)

    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(queue, *args, **kwargs)
        return result

    return wrapper
