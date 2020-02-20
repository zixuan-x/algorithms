class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        numSet = set(nums1)
        intersect = set()
        res = []
        for num in nums2:
            if num in numSet:
                intersect.add(num)
        return list(intersect)

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
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
                if not res or res[-1] != nums1[i]:
                    res.append(nums1[i])
                i += 1
                j += 1
        
        return res

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) < len(nums2):
            shortNums, longNums = nums1, nums2
        else:
            shortNums, longNums = nums2, nums1
        
        longNums.sort()
        res = set()
        
        for num in shortNums:
            if self.binarySearch(longNums, num) != -1:
                res.add(num)
        
        return list(res)
    
    def binarySearch(self, nums, target):
        left, right = 0, len(nums) - 1 
        
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid
            elif nums[mid] > target:
                right = mid
            else:
                return mid
        
        if nums[left] == target:
            return left
        elif nums[right] == target:
            return right
        else:
            return -1
                
