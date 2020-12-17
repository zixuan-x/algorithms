'''
- sort clips
- while maxReach < target end:
    - iterate -> all intervals with start <= maxReach
        - to get current max reach in one jump
    - if current max reach <= maxReach -> return -1
    - otherwise -> maxReach = current max reach
    - count += 1
'''
class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        clips.sort()
        i, maxReach, count = 0, 0, 0
        while maxReach < T:
            currentMaxReach = 0
            while i < len(clips) and clips[i][0] <= maxReach:
                currentMaxReach = max(currentMaxReach, clips[i][1])
                i += 1
            
            if currentMaxReach <= maxReach:
                return -1
            
            maxReach = currentMaxReach
            count += 1
        return count