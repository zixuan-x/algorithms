# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Sea(object):
#    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
#
#class Point(object):
#	def __init__(self, x: int, y: int):
#		self.x = x
#		self.y = y

'''
[0"]: start
[12"]: Maximum Recursion Depth Exceeded
bugs:
1. points cannot be caompared directly
2. 要保证每次不会求解同样的问题，所以不能有两个自问题包含同样的点，特别是平分线上的点

[end] 
'''

class Solution(object):
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        count = 0
        if topRight.y >= bottomLeft.y and topRight.x >= bottomLeft.x and sea.hasShips(topRight, bottomLeft):
            if topRight.x == bottomLeft.x and topRight.y == bottomLeft.y:
                return 1
            midX, midY = (topRight.x + bottomLeft.x) // 2, (topRight.y + bottomLeft.y) // 2
            count += self.countShips(sea, Point(midX, topRight.y), Point(bottomLeft.x, midY + 1))
            count += self.countShips(sea, topRight, Point(midX + 1, midY + 1))
            count += self.countShips(sea, Point(midX, midY), bottomLeft)
            count += self.countShips(sea, Point(topRight.x, midY), Point(midX + 1, bottomLeft.y))
        return count