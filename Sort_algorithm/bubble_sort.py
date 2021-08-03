from typing import List

target_list = [9, 3, 5, 1, 2, 9]

def bubble_sort(ls: List[int]) -> List[int]:
    """ bubble_sort """
    for i in range(len(ls) - 1):
        for j in range(len(ls) - 1):
            if ls[j] > ls[j + 1]:
                tmp = ls[j]
                ls[j] = ls[j + 1]
                ls[j + 1] = tmp
    
    return ls

k = bubble_sort(target_list)
print(k)
