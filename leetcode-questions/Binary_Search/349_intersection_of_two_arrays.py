class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        numSet = set(nums1)
        intersect = set()
        res = []
        for num in nums2:
            if num in numSet:
                intersect.add(num)
        return list(intersect)