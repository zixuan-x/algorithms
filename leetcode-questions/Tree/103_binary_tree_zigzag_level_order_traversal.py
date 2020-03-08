import collections

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
    [1:02] start
    BFS
    [1:06] solved
    """
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root:
            return res
        
        queue = collections.deque([root])
        leftToRight = True
        while queue:
            levelSize = len(queue)
            level = collections.deque()
            for i in range(levelSize):
                cur = queue.popleft()
                if leftToRight:
                    level.append(cur.val)
                else:
                    level.appendleft(cur.val)
                
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            leftToRight = not leftToRight
            res.append(list(level))
        
        return res