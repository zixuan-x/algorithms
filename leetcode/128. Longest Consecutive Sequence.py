'''
hash table:
'''
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result = 0
        sequence = {}  # {number: longest sequence it links to}
        for n in nums:
            if n not in sequence:
                left = sequence.get(n - 1, 0)
                right = sequence.get(n + 1, 0)
                
                length = left + right + 1
                sequence[n] = length 
                result = max(result, length)
                
                sequence[n - left] = length 
                sequence[n + right] = length
        return result

'''
union/find:
'''
class UnionSet:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.ranks = [1] * n
        
    def find(self, u):
        if self.parents[u] != u:
            self.parents[u] = self.find(self.parents[u])
        return self.parents[u]
    
    def union(self, u, v):
        ru, rv = self.find(u), self.find(v)
        if ru == rv:
            return False
        if self.ranks[ru] < self.ranks[rv]:
            self.parents[ru] = rv
        elif self.ranks[ru] > self.ranks[rv]:
            self.parents[rv] = ru
        else:
            self.parents[ru] = rv
            self.ranks[rv] += 1
        return True
        
    def maxGroupSize(self):
        count = [0] * len(self.parents)
        largest = 0
        for i in range(len(self.parents)):
            count[self.find(i)] += 1
            largest = max(largest, count[self.find(i)])
        return largest
        

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ufset = UnionSet(len(nums))
        valueToIndex = {} # {value: index}
        for i in range(len(nums)):
            if nums[i] in valueToIndex:
                continue
            valueToIndex[nums[i]] = i
            if nums[i] - 1 in valueToIndex:
                ufset.union(i, valueToIndex[nums[i] - 1])
            if nums[i] + 1 in valueToIndex:
                ufset.union(i, valueToIndex[nums[i] + 1])
        return ufset.maxGroupSize()
        