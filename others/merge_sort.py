# Merge sort: Paran Premaratne
from typing import List




def merge_sort(list: List[int]) -> List[int]:
    """
    Divide: Find the midpoint of the list and divide into sublists
    Conquer: Recursively sort the sublists created in previous step
    Combine: Merge the sorted sublists created in previous step
    """

    # Base case
    if len(list) <= 1:
        return list

    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)




