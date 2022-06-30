# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        return self.dfs(root, 0)
        
    def dfs(self, root, prevSum):
        if not root:
            return 0
        elif not root.left and not root.right:
            return prevSum * 10 + root.val;
        else:
            return self.dfs(root.left, prevSum * 10 + root.val) + self.dfs(root.right, prevSum * 10 + root.val)