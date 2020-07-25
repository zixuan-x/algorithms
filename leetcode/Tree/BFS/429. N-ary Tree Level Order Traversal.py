"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        
        result = []
        queue = deque([root])
        while queue:
            levelSize = len(queue)
            level = []
            for _ in range(levelSize):
                node = queue.popleft()
                level.append(node.val)
                if not node.children:
                    continue
                for child in node.children:
                    queue.append(child)
            result.append(level)
        return result