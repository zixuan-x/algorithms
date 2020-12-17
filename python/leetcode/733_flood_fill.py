class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if not image or not image[0]:
            return image
        
        r = len(image)
        c = len(image[0]) if r else 0
        color = image[sr][sc]
        
        self.dfs(image, sr, sc, r, c, color, newColor)
        
        return image

    
    def dfs(self, image, x, y, r, c, color, newColor):
        if x < 0 or y < 0 or x >= r or y >= c:
            return
        if image[x][y] == newColor or image[x][y] != color:
            return
        image[x][y] = newColor
        
        for dx, dy in [[1,0], [-1,0], [0,1], [0,-1]]:
            self.dfs(image, x + dx, y + dy, r, c, color, newColor)