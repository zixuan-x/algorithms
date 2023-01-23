# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        # n is guaranteed to be larger than or equal to 1
        left, right = 1, n
        while left + 1 < right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid
                # left = mid + 1 (also works)

        if isBadVersion(left): return left
        if isBadVersion(right): return right