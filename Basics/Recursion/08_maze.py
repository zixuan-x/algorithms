from typing import List

def maze(map: List[List[str]], startX: int, startY: int, targetX: int, targetY: int, visited: List[List[bool]]) -> bool:
    row = len(map)
    column = len(map[0]) if row else 0

    if startX < 0 or startY < 0 or startX >= row or startY >= column or map[startX][startY] == 'X' or visited[startX][startY]:
        return False
    
    if startX == targetX and startY == startY:
        return True

    visited[startX][startY] = True

    return maze(map, startX + 1, startY, targetX, targetY, visited) or 
           maze(map, startX - 1, startY, targetX, targetY, visited) or 
           maze(map, startX, startY + 1, targetX, targetY, visited) or 
           maze(map, startX, startY - 1, targetX, targetY, visited)

# Refer PPT 

    
