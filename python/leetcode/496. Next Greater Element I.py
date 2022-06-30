'''backward'''
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater_elements = {}
        stack = []
        for num in reversed(nums2):
            while stack and num >= stack[-1]:
                stack.pop()
            next_greater_elements[num] = stack[-1] if stack else -1
            stack.append(num)
        
        res = [-1] * len(nums1)
        for i in range(len(nums1)):
            res[i] = next_greater_elements[nums1[i]]
        return res