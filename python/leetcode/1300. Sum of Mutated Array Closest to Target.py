class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        arr.sort()
        prefixSum, n = 0, len(arr)
        i = 0
        while i < n and prefixSum + arr[i] * (n - i) < target:
            prefixSum += arr[i]
            i += 1
            
        if i == n:
            return arr[-1]
        
        result = (target - prefixSum) // (n - i)
        if abs(target - prefixSum - result * (n - i)) <= abs(target - prefixSum - (result + 1) * (n - i)):
            return result
        else:
            return result + 1