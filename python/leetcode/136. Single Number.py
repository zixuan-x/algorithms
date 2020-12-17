from collections import reduce
import operator

'''
XOR
'''
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for n in nums:
            result ^= n
        return result

'''
hash table:
'''
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counter = Counter(nums)
        for n in nums:
            if counter[n] == 1:
                return n
        return -1

'''
sum:
'''
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return 2 * sum(set(nums)) - sum(nums)

'''
reduce:
'''
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x ^ y, nums)

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(operator.xor, nums)