from typing import List

def knapsack(s: int, w: List[int]) -> bool:
    return knapsack_helper(s, w, 0)

def knapsack_helper(s: int, w: List[int], index: int) -> bool:
    if s == 0:
        return True
    if s < 0 or index >= len(w):
        return False
    
    return knapsack_helper(s - w[index], w, index + 1) or knapsack_helper(s, w, index + 1)

s = 20
w = [14, 8, 7, 5, 3]

print(knapsack(s, w))