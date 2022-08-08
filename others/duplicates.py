from typing import List

def duplicates(array: List[int]) -> List[int]:
    """Docstring"""
    duplicates_arr = []

    for num in array:
        index = abs(num) - 1
        if array[index] < 0:
            duplicates_arr.append(index+1)
        else:
            array[index] = -array[index]

    return duplicates_arr

arr = [1, 2, 3, 4, 5, 6, 7, 2, 1]
print(duplicates(arr))
