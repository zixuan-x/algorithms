# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        queue = collections.deque([root])
        while queue:
            cur = queue.popleft()
            if not cur:
                return not any(queue)
            queue.append(cur.left)
            queue.append(cur.right)
        
        
        