class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if x <= arr[0]:
            return arr[:k]
        if x >= arr[-1]:
            return arr[len(arr) - k:]
        
        left, right = 0, len(arr) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if arr[mid] <= x:
                left = mid
            elif arr[mid] > x:
                right = mid
        
        while k > 0:
            if left < 0:
                right += 1
            elif right >= len(arr):
                left -= 1
            elif abs(arr[left] - x) <= abs(arr[right] - x):
                left -= 1
            else:
                right += 1
            k -= 1
    
        return arr[left + 1:right]