def alternatingSort(a):
    left, right = 0, len(a) - 1
    flag = True
    while left < right:
        if flag:
            if a[left] >= a[right]:
                return False
            left += 1
            flag = not flag
        else:
            if a[left] <= a[right]:
                return False
            right -= 1
            flag = not flag
    return True

print(alternatingSort([1, 3, 5, 6, 4, 2]) == True)