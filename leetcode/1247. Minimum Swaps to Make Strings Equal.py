class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        x1, x2, y1, y2 = 0, 0, 0, 0
        
        for i in range(len(s1)):
            c1, c2 = s1[i], s2[i]
            if c1 == c2:
                continue
            if c1 == 'x':
                x1 += 1
            else:
                y1 += 1
            if c2 == 'x':
                x2 += 1
            else:
                y2 += 1
                
        if (x1 + x2) % 2 != 0 or (y1 + y2) % 2 != 0:
            return -1
        
        return x1 // 2 + y1 // 2 + (x1 % 2) * 2
    