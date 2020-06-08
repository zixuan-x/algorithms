from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root: return res
        
        queue = deque([root])
        while queue:
            levelSize = len(queue)
            levelNodes = []
            for i in range(levelSize):
                node = queue.popleft()
                levelNodes.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            res.append(levelNodes)
        
        return res
        