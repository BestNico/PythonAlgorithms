
from typing import List

target_list = [6, 3, 5, 1, 2, 9]

def selection_sort(target: List[int]) -> List[int]:
    """ selection_sort """
    for i in range(len(target) - 1):
        min_index = i

        for j in range(i+1, len(target)):
            if target[j] < target[min_index]:
                min_index = j

        tmp = target[i]
        target[i] = target[min_index]
        target[min_index] = tmp
    
    return target

new_list = selection_sort(target_list)
print(new_list)
