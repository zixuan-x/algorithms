'''
https://leetcode.com/problems/next-greater-element-iii/discuss/101824/Simple-Java-solution-(4ms)-with-explanation.
'''
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        nums = list(map(int, str(n)))
        # nums = [int(c) for c in str(n)]
        
        i = len(nums) - 1
        # find first digit that's smaller than its next digit
        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1
                
        # if in descending order, return -1
        if i == 0: return -1
        
        # find the smallest element behind i that's greater than i
        j = i
        while j + 1 < len(nums) and nums[j + 1] > nums[i - 1]:
            j += 1
        
        nums[i - 1], nums[j] = nums[j], nums[i - 1]
        
        # nums[i:] = list(reversed(nums[i:]))
        nums[i:] = reversed(nums[i:])
        
        res = int(''.join(map(str, nums)))
        
        # return res if (res >> 32) == 0 else -1
        return res if res <= (1 << 32 - 1) else -1
        
        
