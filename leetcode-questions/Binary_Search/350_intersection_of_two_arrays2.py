class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        res = []
        
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                res.append(nums1[i])
                i += 1
                j += 1
        
        return res

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) < len(nums2):
            shortNums, longNums = nums1, nums2
        else:
            shortNums, longNums = nums2, nums1

        longNums.sort()
        shortNums.sort()
        start = 0
        res = []

        for num in shortNums:
            index = self.binarySearch(longNums, start, num)
            if index != -1:
                res.append(num)
                start = index + 1

        return res

    def binarySearch(self, nums, start, target):
        left, right = start, len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid
            else:
                right = mid
        
        if left < len(nums) and nums[left] == target:
            return left
        elif right < len(nums) and nums[right] == target:
            return right
        else:
            return -1