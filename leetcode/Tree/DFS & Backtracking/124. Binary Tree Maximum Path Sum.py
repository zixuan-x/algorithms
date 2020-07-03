# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        res = [float("-inf")]
        self.maxPath(root, res)
        return res[0]
        
        
    def maxPath(self, root, res):
        if not root:
            return 0
        
        left = max(self.maxPath(root.left, res), 0)
        right = max(self.maxPath(root.right, res), 0)
        
        res[0] = max(res[0], root.val + left + right)
        
        return max(root.val + left, root.val + right)