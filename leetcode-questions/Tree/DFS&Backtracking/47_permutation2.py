class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        cur = []
        res = []
        self.permute(nums, cur, res, collections.Counter(nums))
        return res
        
    def permute(self, nums, cur, res, counter):
        if len(cur) == len(nums):
            res.append(list(cur))
        else:
            for num in counter:
                if counter[num] > 0:
                    cur.append(num)
                    counter[num] -= 1
                    self.permute(nums, cur, res, counter)
                    cur.pop()
                    counter[num] += 1