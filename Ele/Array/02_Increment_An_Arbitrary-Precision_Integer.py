def plus_one1(A):
    for i in reversed(range(len(A))):
        if A[i] != 9:
            A[i] += 1
            break
        elif i == 0:
            A[i] = 0
            A.insert(0, 1)
        else:
            A[i] = 0
    return A

def plus_one2(A):
    A[-1] += 1
    for i in reversed(range(1, len(A))):
        if A[i] != 10:
            break
        A[i] = 0
        A[i - 1] += 1
    if A[0] == 10:
        # A[0] = 1
        # A.append(0)
        A[0] = 0
        A.insert(0, 1)
    return A

def plus_binary_string(b1, b2):
    

A = [9,9,9]
print(A)
print(plus_one2(A))
