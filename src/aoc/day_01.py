from collections import deque
from functools import reduce
from functools import wraps
from typing import Callable
from typing import List


def queue_decorator(func: Callable, maxlen: int = 2):
    """Decorator for injecting a queue into our reduce function."""
    queue = deque([], maxlen=maxlen)

    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(queue, *args, **kwargs)
        return result

    return wrapper


@queue_decorator
def measurement_counter(queue: deque, count: int, new_measurement: int) -> int:
    """Counts

    Arguments
    ---------
    queue : deque
        Queue to keep track of the previous measurements.
    count : int
        Left value from reduce call.
    new_measurement : int
        Right value from reduce call.

    Returns
    -------
    count : int
        Count of measurements matching our criteria.
    """

    # store the next measurement in our queue
    queue.append(new_measurement)

    # no previous measurement, skip count
    if count is None:
        return 0

    # fetch the previous measurement from our queue
    old_measurement = queue.popleft()

    # increment count when the current measurement is higher
    inc = 1 if new_measurement > old_measurement else 0

    return count + inc


def partition(items: List[int], maxlen: int):
    """Partition a list of number using a sliding window algorithm.

    Arguments
    ---------
    items : list[int]
        List of number to partition
    maxlen : int
        Size of the sliding window

    Yields
    ------
    values : iter
        Iterator matching our window size.
    """
    for i in range(0, len(items)):
        values = items[i : i + maxlen : 1]
        if len(values) < 3:
            return
        yield values


def answer_1(input: List[str]) -> int:
    normalized_list = list(map(int, input))
    result = reduce(measurement_counter, normalized_list, None)

    return result


def answer_2(input: List[str]) -> int:
    normalized_list = list(map(int, input))
    partitioned_list = [sum(p) for p in partition(normalized_list, 3)]
    result = reduce(measurement_counter, partitioned_list, None)

    return result
