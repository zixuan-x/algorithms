from typing import List
from collections import Counter

def coolFeatures(a: List[int], b: List[int], queries: List[List[int]]):
    a = Counter(a)
    result = []
    for query in queries:
        if len(query) == 3: # update
            _, index, value = query
            b[index] = value
        else:               # count
            count = 0
            target = query[1]
            for num in b:
                count += a.get(target - num, 0)
            result.append(count)
    return result

print(coolFeatures([1, 2, 3], [3, 4], [[1, 5], [1, 1, 1], [1, 5]]) == [2, 1])

