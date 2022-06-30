class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        count, n = 0, len(nums)
        for i in range(n - 1, 1, -1):
            l, r = 0, i - 1
            while l < r:
                # we need to find pairs with l + r > i
                if nums[l] + nums[r] <= nums[i]:
                    l += 1
                else:
                    count += r - l
                    r -= 1
        return count
                    