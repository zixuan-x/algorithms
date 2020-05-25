from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root: return res
        
        leftToRight = True
        queue = deque([root])
        while queue:
            levelSize = len(queue)
            levelNodes = deque()
            for _ in range(levelSize):
                node = queue.popleft()
                if leftToRight:
                    levelNodes.append(node.val)
                else:
                    levelNodes.appendleft(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            leftToRight = not leftToRight
            res.append(list(levelNodes))
        
        return res
            