def mutateTheArray(n, a):
    b = [0] * n
    for i in range(n):
        left = a[i - 1] if i > 0 else 0
        right = a[i + 1] if i < n - 1 else 0
        b[i] = left + a[i] + right
    return b

print(mutateTheArray(5, [4, 0, 1, -2, 3]) == [4, 5, -1, 2, 1]) 