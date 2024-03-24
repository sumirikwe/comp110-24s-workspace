"""Functions that implement sorting algorithms."""

__author__ = ""

def insertion_sort(x: list[int]) -> None:
    """Basic insertion sort algorithm.
    Insert into an already sorted list."""
    idx: int = 0
    while idx < (len(x) - 1):
        unsort_idx: int = idx + 1
        current_elem: int = x[unsort_idx]
        
        while (unsort_idx > 0) and (current_elem < x[unsort_idx - 1]):
            x[unsort_idx] = x[unsort_idx - 1]
            unsort_idx -= 1
        
        x[unsort_idx] = current_elem
        idx += 1
    return None


def selection_sort(x: list[int]) -> None:
    """Basic selection sort algorithm. 
    Repeatedly find the minimum and swap it."""
    idx: int = 0
    while idx < len(x):
        min_idx: int = idx
        minimum: int = x[min_idx]
        inner_idx: int = idx + 1
        
        while inner_idx < len(x):
            if x[inner_idx] < minimum:
                min_idx = inner_idx
                minimum = x[inner_idx]
            inner_idx += 1

        if x[min_idx] != x[idx]:
            swap: int = x[idx]
            x[idx] = x[min_idx]
            x[min_idx] = swap

        idx += 1
    return None