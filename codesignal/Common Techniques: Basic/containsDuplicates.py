def containsDuplicates(a):
    visited = set()
    for num in a:
        if num in visited:
            return True
        visited.add(num)
    return False
