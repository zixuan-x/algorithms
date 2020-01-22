class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # This cannot use two pointers because you need to return indexes instead of values
        visited = {}
        
        for i, num in enumerate(nums):
            if target - num in visited:
                return [visited[target - num], i]
            else:
                visited[num] = i
                
        return [-1, -1]
            