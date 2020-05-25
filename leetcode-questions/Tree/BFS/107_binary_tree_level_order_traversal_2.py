from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        res = deque()
        if not root: return list(res)
        
        queue = deque([root])
        while queue:
            levelSize = len(queue)
            levelNodes = []
            for i in range(levelSize):
                node = queue.popleft()
                levelNodes.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
                    
            res.appendleft(levelNodes)
        
        return list(res)