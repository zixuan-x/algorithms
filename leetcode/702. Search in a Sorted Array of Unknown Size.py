# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        upper = 0
        while reader.get(upper) < target and reader.get(upper) != 2147483647:
            upper = 2 * upper + 1
        left, right = 0, upper
        while left + 1 < right:
            mid = (left + right) // 2
            if reader.get(mid) < target:
                left = mid
            elif reader.get(mid) > target:
                right = mid
            else:
                return mid
        
        if reader.get(left) == target:
            return left
        elif reader.get(right) == target:
            return right
        else:
            return -1