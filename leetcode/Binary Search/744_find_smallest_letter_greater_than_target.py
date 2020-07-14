class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left, right = 0, len(letters) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if letters[mid] <= target:
                left = mid
            else:
                right = mid
        
        # if target >= letters[right]:
        #     return letters[right + 1] if right + 1 < len(letters) else letters[0]
        # elif target >= letters[left]:
        #     return letters[right]
        # else:
        #     return letters[left]
        if target >= letters[left] and target < letters[right]:
            return letters[right]
        else:
            return letters[0]
        
#         while left <= right:
#             mid = (left + right) // 2
#             if letters[mid] <= target:
#                 left = mid + 1
#             else:
#                 right = mid - 1
            
#         return letters[left % len(letters)]
        