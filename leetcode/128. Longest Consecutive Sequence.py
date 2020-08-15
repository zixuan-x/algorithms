class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result = 0
        sequence = {}  # {number: longest sequence it links to}
        for n in nums:
            if n in sequence:
                continue
            left = sequence.get(n - 1, 0)
            right = sequence.get(n + 1, 0)
            
            length = left + right + 1
            sequence[n] = length
            result = max(result, length)
        
            
            sequence[n - left] = length
            sequence[n + right] = length
        return result