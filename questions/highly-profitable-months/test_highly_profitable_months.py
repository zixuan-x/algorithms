from typing import List

def highly_profitable_months(prices: List[int], k: int) -> int:
    count = 0
    increasing_length = 0
    last_price = float("-inf")
    for price in prices:
        if price > last_price:
            increasing_length += 1
        else:
            increasing_length = 1

        if increasing_length >= k:
                count += 1
        
        last_price = price

    return count

def test_highly_profitable_months():
    assert highly_profitable_months([5, 3, 5, 7, 8], 3) == 2
    assert highly_profitable_months([7, 2, 4, 5, 4, 3, 11, 9], 2) == 3
    assert highly_profitable_months([1, 1, 1, 1, 1], 1) == 5
    assert highly_profitable_months([1, 1, 1, 1, 1], 2) == 0

    