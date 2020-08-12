def cutRibbon(ribbons, k):
    maxLength = max(ribbons)
    left, right = 1, maxLength
    while left + 1 < right:
        mid = (left + right) // 2
        if isValidLength(ribbons, mid, k):
            left = mid
        else:
            right = mid - 1
    if isValidLength(ribbons, right, k):
        return right
    elif isValidLength(ribbons, left, k):
        return left
    else:
        return 0

def isValidLength(ribbons, curLength, k):
    validPieces = 0
    for ribbon in ribbons:
        validPieces += ribbon // curLength
    return True if validPieces >= k else False

print(cutRibbon([1, 2, 3, 4, 9], 5) == 3)
