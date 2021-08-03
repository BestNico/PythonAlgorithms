from typing import List

target_list = [1, 6, 3, 5, 1, 2, 9]

def insert_sort(ls: List[int]) -> List[int]:
    """ insert_sort """
    for i in range(1, len(ls)):
        while i >= 1:
            if ls[i] < ls[i - 1]:
                tmp = ls[i]
                ls[i] = ls[i - 1]
                ls[i - 1] = tmp
            i = i - 1
    
    return ls

k = insert_sort(target_list)
print(k)