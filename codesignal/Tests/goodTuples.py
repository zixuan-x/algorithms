def goodTuples(array):
    count = 0
    for i in range(1, len(array) - 1):
        first, second, third = array[i - 1], array[i], array[i + 1]
        if (first == second and first != third) or (first != second and first == third) or (second == third and first != second):
            count += 1
    return count

print(goodTuples([4, 4, 6, 1, 2, 2, 2, 3]) == 3)
print(goodTuples([4, 6, 4, 1, 3, 4]) == 1)