# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        return self.dfs(root, 0)
        
    def dfs(self, root, preSum):
        if not root:
            return 0
        elif not root.left and not root.right:
            return preSum * 2 + root.val
        else:
            return self.dfs(root.left, preSum * 2 + root.val) + self.dfs(root.right, preSum * 2 + root.val)