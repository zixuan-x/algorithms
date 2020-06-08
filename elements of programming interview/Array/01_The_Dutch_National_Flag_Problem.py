# O(1) space, O(n) time
def dutch_flag_partition1(pivot_index, A):
    pivot = A[pivot_index]
    # First pass: group elements smaller than pivot.
    smaller = 0
    for i in range(len(A)):
        if A[i] < pivot:
            A[i], A[smaller] = A[smaller], A[i]
            smaller += 1

    # Second pass: group elements larger than pivot.
    larger = len(A) - 1
    for i in reversed(range(len(A))):
        if A[i] < pivot:
            break
        elif A[i] > pivot:
            A[i], A[larger] = A[larger], A[i]
            larger -= 1

def dutch_flag_partition2(pivot_index, A):
    pivot = A[pivot_index]
    smaller, equal, larger = 0, 0, len(A) - 1
    while equal <= larger:
        if A[equal] < pivot:
            A[equal], A[smaller] = A[smaller], A[equal]
            smaller, equal = smaller + 1, equal + 1
        elif A[equal] == pivot:
            equal += 1
        else:
            A[equal], A[larger] = A[larger], A[equal]
            larger = larger - 1



list = [0,1,1,0,2,0,0]
print(list)
dutch_flag_partition2(1, list)
print(list)

