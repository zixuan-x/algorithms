class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        arraySum, average = sum(A), sum(A) // 3
        if arraySum % 3 != 0:
            return False
        
        partSum, count = 0, 0
        for num in A:
            partSum += num
            if partSum == average:
                count += 1
                partSum = 0

        # > 3 also works because 2 parts with the same average can be merged and still have the same average
        return count >= 3  