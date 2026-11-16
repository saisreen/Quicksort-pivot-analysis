"""In-place Quicksort with fixed-last and randomized pivots.

Both variants recurse on the smaller side and iterate on the larger side,
keeping auxiliary stack usage O(log n) even for unfavorable partitions.
"""
import random
from typing import MutableSequence, Optional


def _partition(values: MutableSequence[int], low: int, high: int) -> int:
    """Lomuto partition around the element at high (inclusive)."""
    pivot = values[high]
    boundary = low
    for index in range(low, high):
        if values[index] <= pivot:
            values[boundary], values[index] = values[index], values[boundary]
            boundary += 1
    values[boundary], values[high] = values[high], values[boundary]
    return boundary


def _sort(values: MutableSequence[int], low: int, high: int,
          rng: Optional[random.Random]) -> None:
    while low < high:
        if rng is not None:
            pivot_index = rng.randint(low, high)
            values[pivot_index], values[high] = values[high], values[pivot_index]
        pivot = _partition(values, low, high)
        if pivot - low < high - pivot:
            _sort(values, low, pivot - 1, rng)
            low = pivot + 1
        else:
            _sort(values, pivot + 1, high, rng)
            high = pivot - 1


def deterministic_quicksort(values: MutableSequence[int]) -> MutableSequence[int]:
    """Sort in place with the last element as pivot; return the same sequence."""
    _sort(values, 0, len(values) - 1, None)
    return values


def randomized_quicksort(values: MutableSequence[int],
                         rng: Optional[random.Random] = None) -> MutableSequence[int]:
    """Sort in place with a uniformly random pivot at every partition."""
    _sort(values, 0, len(values) - 1, rng if rng is not None else random.Random())
    return values
