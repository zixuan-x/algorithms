class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        m, n = len(image), len(image[0])
        left = self.leftMost(image, 0, y, True)
        right = self.rightMost(image, y, n - 1, True)
        top = self.leftMost(image, 0, x, False)
        bottom = self.rightMost(image, x, m - 1, False)
        return (right - left + 1) * (bottom - top + 1)
        
    def leftMost(self, image, left, right, horizontal):
        while left + 1 < right:
            mid = (left + right) // 2
            if self.hasBlack(image, mid, horizontal):
                right = mid
            else:
                left = mid               
        if self.hasBlack(image, left, horizontal):
            return left
        else:
            return right
        
    def rightMost(self, image, left, right, horizontal):
        while left + 1 < right:
            mid = (left + right) // 2
            if self.hasBlack(image, mid, horizontal):
                left = mid
            else:
                right = mid       
        if self.hasBlack(image, right, horizontal):
            return right
        else:
            return left
            
    
    def hasBlack(self, image, mid, horizontal):
        if horizontal:
            return any(map(lambda x: x == '1',(image[i][mid] for i in range(len(image)))))
        else:
            return any(map(lambda x: x == '1',image[mid]))